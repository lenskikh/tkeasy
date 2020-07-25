from tkeasy import *

#root is default var
root.title("Entry and label")

def info():
    text = memory["The first entry"].get()
    labels(text=text,colortext="white",font="16",
           background="red",row=3,column=0,sticky="center")

labels(text="Entry field",colortext="black",font="14",
       background="white",row=0,column=0,sticky="center")

entryfield(identifier="The first entry",
           row=1,column=0)

button(text="Get info",command=info,row=2,
        column=0,sticky="right")


