# Jupyter extension for PyOdps

## Install

```bash
$ pip install git+https://github.com/marufeuille/jupyter-pyodps
```

## Usage

In your notebook, load module.

```
%load_ext maxcompute
```

and Using like this.

```sql
%%odps
DESC test2
```