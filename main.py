# By Shevchuk Dmytro 8-B (D1N0)

from tkinter import *


def click(event):

    a = root.winfo_y() + 50
    b = root.winfo_width() + 40
    root.geometry(f'480x{a}+{b}+200')

root = Tk()
root.geometry('480x320+200+200')
root.bind('<1>', click)
root.mainloop()


def get_compiled_for(скомпільовано_для):
    """Teacher"""
