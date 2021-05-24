from tkeasy import *

config(border="False")

def help():
    label(window="second",text="Press ctrl and left click of a mouse for move the first window",
          wrap="250",row=0,column=0)

tabs = {"File":{"Exit":quit},"About":{"Help":help}}
top_menu(tabs)


#move a window by shortcut ctrl+left click of a mouse
advanced().bind("<Control-B1-Motion>", move_window)

#if can't find something in the wrapper, use advanced() in tkinter methods
Spinbox(advanced(), from_=0, to=10).grid(row=0,column=0)

app_loop()
