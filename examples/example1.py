from tkeasy import *


def info():
    text = memory["The first entry"].get()
    labels(text=text,colortext="white",
           background="red",row=3,
           column=0,sticky="center")

labels(text="Entry field",colortext="black",
       background="white",row=0,column=0)

entryfield("The first entry",row=1,column=0)

buttons(text="Get info",command=info,row=2,column=0,sticky="right")
