
# cmdprogress

[![PyPI version shields.io](https://img.shields.io/pypi/v/cmdprogress.svg)](https://pypi.python.org/pypi/cmdprogress/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/cmdprogress.svg)](https://pypi.python.org/pypi/cmdprogress/)
[![PyPI license](https://img.shields.io/pypi/l/cmdprogress.svg)](https://pypi.python.org/pypi/cmdprogress/)

Cross Platform Python Command Line Progress Bars

**MacOS**

![Multi Bar](https://raw.githubusercontent.com/luciancooper/cmdprogress/master/multi_demo.gif)

**Windows**

**Linux**

### Contents
* [Installation](#installation)
* [ProgBar](#ProgBar)
* [MultiBar](#MultiBar)
* [Acknowledgements](#Acknowledgements)

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

## Usage

this project consists of two instantiatable classes: `ProgBar` and `MultiBar`

# ProgBar

There are two ways to use a `ProgBar`

Either give it a length when you instantiate the object, and then directly loop through it

```python
from cmdprogress.bar import ProgBar

bar = ProgBar(max=5)
for x in bar:
    # x = (0 .. 5)
    # do some work
```

Or do not provide it a length when you instantiate it, instead provide it an iterable to wrap

```python
from cmdprogress.bar import ProgBar

bar = ProgBar()
for x in bar.iter(range(5)):
    # x = (0 .. 5)
    # do some work
```


# MultiBar

There are 3 ways to use a `MultiBar`.

```python
from cmdprogress.multi import MultiBar

bar = MultiBar(lvl=2)
for i in bar.iter(range(5)):
    for j in bar.iter(range(10)):
        # do some work

```


```python
from cmdprogress.multi import MultiBar

bar = MultiBar(5,lvl=2)
for x in range(5):
    for i in bar.iter(range(10)):
        # do some work

```


```python
from cmdprogress.multi import MultiBar

bar = MultiBar(5,10)
for x in bar:
    # x will be the tuple (i,j)
    # do some work

```


## Acknowledgements

 - This project depends on [colorama](https://pypi.org/project/colorama/) to work in the Windows Command Line
 - Shoutout to this [stack overflow answer](https://stackoverflow.com/a/10455937)
