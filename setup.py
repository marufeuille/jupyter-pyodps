import os, sys
from setuptools import setup, find_packages
from odps import ODPS

from magic.odps import OdpsMagic

__version__ = '0.0.1'

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='odps-jupyter',
    version='0.0.1',
    description='Package for Jupyter using odps with magic command.',
    long_description=readme,
    author='Masahiro Ishii',
    author_email='marufeuille@gmail.com',
    install_requires=read_requirements(),
    url='https://github.com/marufeuikke/jupyter-pyodps',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

def load_ipython_extension(ipython):
    params = {}
    with open("/home/jovyan/.aliyun_profile") as f:
        for item in f.read().strip().split("\n"):
            key, param = item.split("=",1)
            params[key] = param
    myodps = ODPS(params["AccessKeyId"], params['AccessKeySecret'], params['Project'], endpoint=params['Endpoint'])
    magic = OdpsMagic(ipython, myodps)
    ipython.register_magics(magic)