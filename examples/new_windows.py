from tkeasy import *

#Will be changed in next releases
def windows():
    new_window("new_window")
    new_window("new_window2")
   
    
buttons(text="Click me",command=windows,row=0,column=0)
