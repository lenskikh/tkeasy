from tkeasy import *

def info():
    print(memory["checkbox 1"].get())
    print(memory["checkbox 2"].get())
    print(memory["entry2"].get())

labels(text="What kind of fruit do you like?",row=0,column=0)    
checkbox("checkbox 1", text="Apple",row=1,column=0,sticky = "left")
checkbox("checkbox 2", text="Banan",row=2,column=0,sticky = "left")
entryfield("entry2",row=3,column=0)
button(text="show info",command=info,row=4,column=0)
