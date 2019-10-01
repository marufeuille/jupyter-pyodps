from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)
from IPython.core.magic import (register_line_magic, register_cell_magic)
from io import StringIO

@magics_class
class OdpsMagic(Magics):
    
    def __init__(self, shell, odps):
        super(PyOdpsMagic, self).__init__(shell)
        self.odps = odps

    @cell_magic
    def odps(self, line, cell):
        sio = StringIO(cell).getvalue()

        result = []
        with self.odps.execute_sql(sio).open_reader() as reader:
            for record in reader:
                result.append(record)
        return result