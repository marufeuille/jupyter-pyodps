from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)
from IPython.core.magic import (register_line_magic, register_cell_magic)
from io import StringIO

from odps import ODPS
import pandas as pd

@magics_class
class ODPSMagic(Magics):
    
    def __init__(self, shell, odps):
        super(ODPSMagic, self).__init__(shell)
        self.odps = odps

    @cell_magic
    def odps(self, line, cell):
        sql = StringIO(cell).getvalue()

        result = []
        
        column = []
        fields = []

        with self.odps.execute_sql(sql).open_reader() as reader:
            if sql[0:4].upper() == "DESC":
                field_flag = False
                idx = 1
                for record in reader:
                    for field in record:
                        if field[1][0:2] == "+-":
                            continue
                        if field_flag:
                            x = field[1][1:-1].split("|")
                            column.append("FieldName-{}".format(idx))
                            fields.append(x[0].strip())
                            column.append("FieldType-{}".format(idx))
                            fields.append(x[1].strip())
                            idx += 1
                        else:
                            for item in field[1][1:-1].strip().split("|"):
                                x = item.split(":", 1)
                                if x[0].strip() == "Field":
                                    field_flag = True
                                    break
                                if len(x) == 1:
                                    continue
                                column.append(x[0].strip())
                                fields.append(x[1].strip() if len(x) == 2 else "")
                return pd.DataFrame([fields], columns=column)
            else:
                for record in reader:
                    c = []
                    f = []
                    for field in record:
                        c.append(field[0])
                        f.append(field[1])
                    if len(column) == 0:
                        column = c
                    fields.append(f)
        
        return pd.DataFrame(fields, columns=column)
    
def load_ipython_extension(ipython):
    params = {}
    with open("/home/jovyan/.aliyun_profile") as f:
        for item in f.read().strip().split("\n"):
            key, param = item.split("=",1)
            params[key] = param
    myodps = ODPS(params["AccessKeyId"], params['AccessKeySecret'], params['Project'], endpoint=params['Endpoint'])
    magic = ODPSMagic(ipython, myodps)
    ipython.register_magics(magic)