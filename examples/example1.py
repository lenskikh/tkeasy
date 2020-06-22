from tkeasy import *


def info():
    text = memory["The first entry"].get()
    labels(text,"black","","white",3,0,"center")

title("Example 1")

labels("Entry field","black","","white",0,0,"center")

entryfield("The first entry",1,0)

buttons("Get info",info,2,0)

root.mainloop()
