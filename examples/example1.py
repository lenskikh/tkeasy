from tkeasy import *


def info():
    text = memory["The first entry"].get()
    labels(text,"white","16","red",3,0,"center")

labels("Entry field","black","14","white",0,0,"center")

entryfield("The first entry",1,0)

buttons("Get info",info,2,0,"right")

root.mainloop()
