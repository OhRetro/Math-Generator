#Utils

import ctypes
import os
from os import system, name

class Utils:
    #setTitle
    def setTitle(title):
        if name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            pass

    #consoleClear
    def clearConsole():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
