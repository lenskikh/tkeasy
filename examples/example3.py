from tkeasy import *

title("Example 3")

memory["first"] = "First name"

def info():
    text1 = memory["entry 1"].get()
    labels(text1,"white","16","grey",0,1,"center")

    text2 = memory["entry 2"].get()
    labels(text2,"white","16","grey",1,1,"center")

    gender = memory["gender var"].get()
    labels(gender,"white","16","grey",2,1,"center")

    age = memory["age var"].get()
    labels(age,"white","16","grey",3,1,"center")     

entryfield("entry 1",0,0)
entryinsert("entry 1",memory["first"],"black")

entryfield("entry 2",1,0)
entryinsert("entry 2","Second name","black")

choices = ["=","Female","Male"]
dropdownlist(choices,"gender var","Gender",2,0)

age = ["01-06","7-14","15-23","24-31","31-40","41-55","56-70","71-85","86-105"]
dropdownlist(age,"age var","Age",3,0)

buttons("Get info",info,4,1,"right")

#clear text when click in entry field
root.bind("<Button-1>", clear)
root.bind("<Key>", key)

root.mainloop()
