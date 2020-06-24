from tkeasy import *

title("Example 2")

def info():
    text1 = memory["entry 1"].get()
    labels(text1,"white","16","blue",4,0,"center")

    text2 = memory["entry 2"].get()
    labels(text2,"white","16","blue",5,0,"center")

    text3 = memory["entry 3"].get()
    labels(text3,"white","16","blue",6,0,"center")
    

entryfield("entry 1",0,0)
entryinsert("entry 1","First name","grey")

entryfield("entry 2",1,0)
entryinsert("entry 2","Second name","grey")

entryfield("entry 3",2,0)
entryinsert("entry 3","County","black")

buttons("Get info",info,3,0,"right")

#clear text when click in entry field
root.bind("<Button-1>", clearbyclick)
root.bind("<Key>", key)

root.mainloop()
