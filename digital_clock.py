from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")
root.resizable(0,0)

def time():
    string = strftime('%H:%M:%S  %p')
    Label.config(text=string)
    Label.after(1000,time)

Label = Label(root,font=("ds-digital",50,'bold'),background="black",foreground="cyan")
Label.pack(anchor='center')

time()

mainloop()
