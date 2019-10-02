import os, sys
from setuptools import setup, find_packages

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
    name='jupyterodps',
    version='0.0.1',
    description='Package for Jupyter using odps with magic command.',
    long_description=readme,
    author='Masahiro Ishii',
    author_email='marufeuille@gmail.com',
    install_requires=read_requirements(),
    url='https://github.com/marufeuille/jupyter-pyodps',
    license=license,
    packages = ['jupyter_odps'],
    py_modules = ['jupyter_odps']
)