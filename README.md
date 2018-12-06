
# cmdprogress

[![PyPI version shields.io](https://img.shields.io/pypi/v/cmdprogress.svg)](https://pypi.python.org/pypi/cmdprogress/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/cmdprogress.svg)](https://pypi.python.org/pypi/cmdprogress/)
[![PyPI license](https://img.shields.io/pypi/l/cmdprogress.svg)](https://pypi.python.org/pypi/cmdprogress/)

Python Command Line Progress Bars

![Multi Bar](https://raw.githubusercontent.com/luciancooper/cmdprogress/master/multi_demo.gif)

### Contents
* [Installation](#installation)
* [Usage](#usage)

# Installation

Use `pip` via [PyPi](https://pypi.org)

```bash
pip install cmdprogress
```

**Or** use `git`

```bash
git clone git://github.com/luciancooper/cmdprogress.git cmdprogress
cd cmdprogress
python setup.py install
```

# Usage

There are a couple of ways to use a python multibar.
```python

from cmdprogress.multi import MultiBar

bar = MultiBar(lvl=2)
for i in bar.iter(range(5)):
    for j in bar.iter(range(10)):
        # do some work
        pass

```


```python

from cmdprogress.multi import MultiBar

bar = MultiBar(5,lvl=2)
for x in range(5):
    for i in bar.iter(range(10)):
        # do some work
        pass

```


```python

from cmdprogress.multi import MultiBar

bar = MultiBar(5,10)
for x in bar:
    # x will be the tuple (i,j)
    # do some work
    pass

```
