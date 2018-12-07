from .core import ProgCLI,ProgCLIError
from collections import deque
from datetime import timedelta
from math import ceil
from time import time

#-------------------------------[bar]---------------------------------------------------------------#

class ProgBar(ProgCLI):
    width = 32
    max = None
    prefix = ''
    suffix = ' {0: 2.0f}% ({1.inx}/{1.max}) {1._timestr_}'
    bar_padding = '|%s|'
    ma_window = 10 # Simple Moving Average window

    def __init__(self,**kwargs):
        self.inx = 0
        super().__init__(**kwargs)
        self._ma = deque(maxlen=self.ma_window)
        self._sts,self._ts = None,None

    # ----- Timing ----- #

    @property
    def _timestr_(self):
        elapsed = timedelta(seconds=int(time()-self._sts))
        eta = ""
        if len(self._ma) > 0:
            avg = sum(self._ma)/len(self._ma)
            eta = " ETA:{}".format(timedelta(seconds=int(ceil(avg * self.remaining))))
        return f"{elapsed}{eta}"

    @property
    def elapsed(self):
        return int(time()-self._sts)

    # -------- index --------- #

    def incInx(self,n=1): # next
        now = time()
        if n>0: self._ma.append((now-self._ts)/n)
        self._ts = now
        self.inx+=n
        return self

    def setInx(self,i):
        self.inx = i
        return self

    # -------- core --------- #



    def start(self):
        self._ma.clear()
        self._sts = time()
        self._ts = self._sts
        self.hide_cursor()
        return self

    def finish(self):
        print(file=self.out)
        self.show_cursor()
        return self

    # -------- iter --------- #

    def iter(self,it):
        if self.max == None:
            try:
                self.max = len(it)
            except TypeError:
                pass
        def wrapper():
            try:
                self.start().update()
                for x in it:
                    yield x
                    self.incInx().update()

            finally:
                self.finish()
        return wrapper()

    # -------- __iter__ --------- #

    def __iter__(self):
        if self.max == None:
            raise ProgCLIError("A maximum has not been provided to progress bar")
        if self.inx == 0:
            self.start().update()
        return self

    def __next__(self):
        if self.inx<self.max:
            i = self.inx
            self.incInx().update()
            return i
        self.finish()
        raise StopIteration()

    # ------------ Progress -------------- #

    @property
    def remaining(self):
        return max(self.max-self.inx,0)

    @property
    def progress(self):
        return min(1,self.inx/self.max)

    # ------------ WriteLnMixin -------------- #

    @property
    def _barstr_(self):
        filled_len = self.width * self.progress
        nfull = int(filled_len)                      # Number of full chars
        nempty = self.width - nfull                  # Number of empty chars
        phase = int((filled_len - nfull) * len(self.fill))    # Phase of last char
        current = self.fill[phase] if phase > 0 else ''
        return self.fill[-1]*nfull+current+self.fill[0]*max(0,nempty-len(current))

    def update(self):
        line = self.prefix.format(self)+(self.bar_padding%self._barstr_)+self.suffix.format(self.progress*100,self)
        self.clear_line()
        print(line, end='', file=self.out)
        self.out.flush()
