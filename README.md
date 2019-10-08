# Jupyter extension for PyOdps

## Install

```bash
$ pip install git+https://github.com/marufeuille/jupyter-pyodps
```

## Setup
### load key from Environment Variable

You set environment variable bellow.

```
AccessKeyId=XXXX
AccessKeySecret=XXX
Project=YOUR_MAXCOMPUTE_PROJECT
Endpoint=http://service.ap-northeast-1.maxcompute.aliyun.com/api(for JP)
```

### load key from file
write config file to ~/.aliyun_profile

```
AccessKeyId=XXXX
AccessKeySecret=XXX
Project=YOUR_MAXCOMPUTE_PROJECT
Endpoint=http://service.ap-northeast-1.maxcompute.aliyun.com/api(for JP)
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