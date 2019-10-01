from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)
from IPython.core.magic import (register_line_magic, register_cell_magic)
from io import StringIO

from odps import ODPS

@magics_class
class ODPSMagic(Magics):
    
    def __init__(self, shell, odps):
        super(ODPSMagic, self).__init__(shell)
        self.odps = odps

    @cell_magic
    def odps(self, line, cell):
        sio = StringIO(cell).getvalue()

        result = []
        with self.odps.execute_sql(sio).open_reader() as reader:
            for record in reader:
                result.append(record)
        return result
    
def load_ipython_extension(ipython):
    params = {}
    with open("/home/jovyan/.aliyun_profile") as f:
        for item in f.read().strip().split("\n"):
            key, param = item.split("=",1)
            params[key] = param
    myodps = ODPS(params["AccessKeyId"], params['AccessKeySecret'], params['Project'], endpoint=params['Endpoint'])
    magic = ODPSMagic(ipython, myodps)
    ipython.register_magics(magic)