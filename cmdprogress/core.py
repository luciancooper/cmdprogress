import sys
import os

if sys.platform.startswith('win'):
    import colorama
    colorama.init()

if os.name == 'nt':
    #import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),("visible", ctypes.c_byte)]


class ProgCLIError(Exception):
    pass


class ProgCLI():

    out = sys.stderr

    themes = {
        'smooth': (' ', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█'),
        'pixel':('⡀', '⡄', '⡆', '⡇', '⣇', '⣧', '⣷', '⣿'),
        'shady':(' ', '░', '▒', '▓', '█'),
        'squares':('▢','▣'), # 9634,9635
        'circles':('◯','◉'), # 9711,9673
        'charge':('∙','█'), # 8729,9608
        'basic':(' ','#'),
    }

    fill = themes['basic'] if os.name=='nt' else themes['smooth']

    def __init__(self,theme=None,**kwargs):
        if not self.out.isatty():
            raise ProgCLIError("ProgCLI must be used within a command line interface")
        if theme != None:
            self.fill = self.themes[theme.lower()]
        for k,v in kwargs.items():
            setattr(self,k,v)

    # -------- core --------- #

    def update(self):
        return self

    def start(self):
        return self

    def finish(self):
        return self

    # ----- Hide / Show Cursor ----- #

    def hide_cursor(self):
        if os.name == 'nt':
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = False
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif os.name == 'posix':
            #sys.out.write("\033[?25l")
            #sys.out.flush()
            print('\x1b[?25l', end='', file=self.out)

    def show_cursor(self):
        if os.name == 'nt':
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = True
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif os.name == 'posix':
            #sys.out.write("\033[?25h")
            #sys.out.flush()
            print('\x1b[?25h', end='', file=self.out)

    def clear_line(self):
        print('\r\x1b[K', end='', file=self.out)

    def line_up(self):
        print('\x1b[1A', end='', file=self.out)

    # ----- Enter / Exit ----- #

    def __enter__(self):
        self.hide_cursor()
        return self

    def __exit__(self, type, value, tb):
        self.show_cursor()
