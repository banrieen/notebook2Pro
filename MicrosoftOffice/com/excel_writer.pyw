#!/usr/bin/env python

from tkinter import Tk
from time import sleep
from tkinter import messagebox
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app : showwarning(app, "Exit? ")
RANGE = range(3, 8)

def excel_writer():
    app = "Excel"
    x1 = win32.gencache.EnsureDispatch("%s.Application" % app)
    ss = x1.Workbooks.Add()
    sh = x1.ActiveSheet
    x1.Visable = True
    sleep(1)

    sh.Cells(1, 1).Value = "Python-to-%s Demo" % app
    sleep(1)

    for i in RANGE:
        sh.Cells(1, i).Value = "Line %d" % i
        sleep(1)

    sh.Cells(I+2,1).Value = "填充-填充！"
    warn(app)
    ss.Close(False)
    x1.Application.Quit()

    if __name__ == "__mian__":
        Tk().withdraw()
        excel()
