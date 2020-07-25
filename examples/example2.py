from tkeasy import *

#root is default var of Tk
root.title("Three entries")

def info():
    text1 = memory["entry 1"].get()
    labels(text=text1,colortext="white",
           background="blue",row=4,
           column=0,sticky="center")

    text2 = memory["entry 2"].get()
    labels(text=text2,colortext="white",
           background="blue",row=5,
           column=0,sticky="center")

    text3 = memory["entry 3"].get()
    labels(text=text3,colortext="white",
           background="blue",row=6,
           column=0,sticky="center")
    

entryfield("entry 1",row=0,column=0)
entryinsert("entry 1","First name","grey")

entryfield("entry 2",row=1,column=0)
entryinsert("entry 2","Second name","grey")

entryfield("entry 3",row=2,column=0)
entryinsert("entry 3","County","black")

button(text="Get info",command=info,row=3,
        column=0,sticky="right")

#clear text when click in entry field
root.bind("<Button-1>", clearbyclick)
root.bind("<Key>", key)
