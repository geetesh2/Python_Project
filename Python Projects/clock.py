from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")
root.geometry('350x200')

def time():
    string = strftime('%I:%M:%S %p')

label = Label(root,font=("ds-digital",80),background="black",foreground="cyan")
label.pack(anchor='center')

root.mainloop()
