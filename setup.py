import os
from odps import ODPS

from magic.odps import OdpsMagic

__version__ = '0.0.1'

def load_ipython_extension(ipython):
    params = {}
    with open("/home/jovyan/.aliyun_profile") as f:
        for item in f.read().strip().split("\n"):
            key, param = item.split("=",1)
            params[key] = param
    myodps = ODPS(params["AccessKeyId"], params['AccessKeySecret'], params['Project'], endpoint=params['Endpoint'])
    magic = OdpsMagic(ipython, myodps)
    ipython.register_magics(magic)