from tkeasy import *

#move a window by shortcut ctrl+left click of a mouse
advanced().bind("<Control-B1-Motion>", move_window)

#if can't find something in the wrapper, use advanced() in tkinter methods
Spinbox(advanced(), from_=0, to=10).grid(row=0,column=0)

app_loop()
