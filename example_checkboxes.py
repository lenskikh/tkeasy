from tkeasy import *

config(background="white")

def info():
    print(get_info("checkbox 1"))
    print(get_info("checkbox 2"))

label(text="What a fruit do you like?",background="white",activebg="white",row=0,column=0)

checkbox(name="checkbox 1", text="Apple",background="white",activebg="white",
         row=1,column=0,sticky = "left")

checkbox(name="checkbox 2", text="Banan",background="white",activebg="white",
         row=2,column=0,sticky = "left")

button(text="show info",background="white",activebg="white",
       command=info,row=3,column=0)

app_loop()
