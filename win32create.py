from tkinter import *

def cWindow(title):
    global root
    root = Tk()
    root.title(title)
def runRoot():
    root.mainloop()
def bgColor(color):
    root.configure(background = color)
def winSize(x,y):
    x = str(x)
    y = str(y)
    z = x+"x"+y
    root.geometry(z)
def entry(loc,color):
    ent = Entry(root, fg = color, justify = loc)
    ent.pack()
def button(text,color):
    rage = Button (root, text = text)
    rage.pack()
