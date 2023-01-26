#!/usr/bin/python
# !/usr/bin/env/python
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

# Zródło:
# msessage dialog:
# https://www.geeksforgeeks.org/create-a-yes-no-message-box-in-python-using-tkinter/
#
# zarządzanie parametrami wej. skryptu
# https://www.geeksforgeeks.org/command-line-option-and-argument-parsing-using-argparse-in-python/



# Python program to create
# yes/no message box


import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import argparse


def call(AppName):
    res = mb.askquestion('Potwierdzenie uruchomienia aplikacji.',
                         f'Czy iruchomić aplikcję {AppName} ?')
    return True if res == "yes" else False
    # if res == 'yes' :
    #     return True
    # else :
    #     return False

def main(args):
    if len(args) > 1:
        param = args[1]
        appname = param.split("=")[0]
        apppath = param.split("=")[1]
        print(f"appname: {appname}")
        print(f"apppath: {apppath}")

        root = Tk()
        root.title(appname)
        # root.geometry("10x10")
        # root.resizable(height=None, width=None) # nie działa !!!
        root.resizable(False, False)
        # root.resizable(False)
        if call(appname):
            os.system(f'"{apppath}"')
        else:
            ...
        root.destroy()
    else:
        print(" - brak parametru\nparametr: etykieta aplikacji=scieżka dostępu do aplikacji")
    return 0


if "main" in dir():
    import sys
    sys.exit(main(sys.argv))
else:
    print("STOPPED BEFORE EXECUTION!!!")
