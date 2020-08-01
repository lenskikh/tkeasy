from tkeasy import *

def info():
    print(get_info("checkbox 1"))
    print(get_info("checkbox 2"))

label(window="main",text="What a fruit do you like?",row=0,column=0)

checkbox(window="main",name="checkbox 1", text="Apple",
         row=1,column=0,sticky = "left")

checkbox(window="main",name="checkbox 2", text="Banan",
         row=2,column=0,sticky = "left")

button(window="main",text="show info",
       command=info,row=3,column=0)
