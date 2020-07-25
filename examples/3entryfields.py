from tkeasy import *

#root is default var of Tk
root.title("Three entries")
root.geometry("200x300")

def info():
    text1 = memory["entry 1"].get()
    labels(text=text1,colortext="white",font="16",
           background="blue",row=4,column=0,sticky="center")

    text2 = memory["entry 2"].get()
    labels(text=text2,colortext="white",font="16",
           background="blue",row=5,column=0,sticky="center")

    text3 = memory["entry 3"].get()
    labels(text=text3,colortext="white",font="16",
           background="blue",row=6,column=0,sticky="center")
    

entryfield(identifier="entry 1",row=0,column=0)
entryinsert(identifier="entry 1",text="First name",colortext="grey")

entryfield(identifier="entry 2",row=1,column=0)
entryinsert(identifier="entry 2",text="Second name",colortext="grey")

entryfield(identifier="entry 3",row=2,column=0)
entryinsert(identifier="entry 3",text="County",colortext="black")

button(text="Get info",command=info,
        row=3,column=0,sticky="right")

#clear text when click in entry field
root.bind("<Button-1>", clearbyclick)
root.bind("<Key>", key)
