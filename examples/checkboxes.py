from tkeasy import *

def info():
    print(memory["checkbox 1"].get())
    print(memory["checkbox 2"].get())

label(window="main",text="What kind of fruit do you like?",row=0,column=0)

checkbox(window="main",name="checkbox 1", text="Apple",
         row=0,column=0,sticky = "left")

checkbox(window="main",name="checkbox 2", text="Banan",
         row=1,column=0,sticky = "left")

button(window="main",text="show info",
       command=info,row=3,column=0)
