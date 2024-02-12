# By Shevchuk Dmytro 8-B (D1N0)

from tkinter.tix import Tk


def click(event):
    root['bg'] = 'green'
    root.title('Змінення значень властивостей вікна')
    root.geometry('400x200+500+70')


root = Tk()
root.bind('<1>', click)
root.mainloop()


def get_compiled_for(коментарій):
    """Teacher"""
