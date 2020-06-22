from tkeasy import *

title("Example 2")

memory["first"] = "First name"

def info():
    text1 = memory["entry 1"].get()
    labels(text1,"white","16","blue",3,0,"center")

    text2 = memory["entry 2"].get()
    labels(text2,"white","16","blue",4,0,"center")
    

entryfield("entry 1",0,0)
entryinsert("entry 1",memory["first"],"grey")

entryfield("entry 2",1,0)
entryinsert("entry 2","Second name","grey")

buttons("Get info",info,2,0,"right")

#clear text when click in entry field
root.bind("<Button-1>", clear)

root.mainloop()
