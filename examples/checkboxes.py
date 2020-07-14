from tkeasy import *

def info():
    print(memory["checkbox 1"].get())
    print(memory["checkbox 2"].get())

labels(text="What kind of fruit do you like?",row=0,column=0)    
checkbox("checkbox 1", text="Apple",row=1,column=0)
checkbox("checkbox 2", text="Banan",row=2,column=0)
buttons(text="show info",command=info,row=3,column=0)
