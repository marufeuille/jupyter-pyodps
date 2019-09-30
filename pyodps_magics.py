from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)
from IPython.core.magic import (register_line_magic, register_cell_magic)
import pandas as pd
from io import StringIO
import os

from odps import ODPS

@magics_class
class PyOdpsMagic(Magics):
    "PyOdps Magics"
    
    def __init__(self, shell, odps):
        super(PyOdpsMagic, self).__init__(shell)
        self.odps = odps

    @cell_magic
    def pyodps(self, line, cell):
        sio = StringIO(cell).getvalue()

        result = []
        with self.odps.execute_sql(sio).open_reader() as reader:
            for record in reader:
                result.append(record)
        return result

def load_ipython_extension(ipython):
    access = os.environ['AccessKeyId'] if 'AccessKeyId' in os.environ else ""
    secret = os.environ['SecretAccessKey'] if 'SecretAccessKey' in os.environ else ""
    project = os.environ['Project'] if 'Project' in os.environ else ""
    endpoint = os.environ['Endpoint'] if 'Endpoint' in os.environ else ""
    myodps = ODPS(access, secret, project, endpoint=endpoint)
    magic = PyOdpsMagic(ipython, myodps)
    ipython.register_magics(magic)