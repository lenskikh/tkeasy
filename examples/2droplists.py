from tkeasy import *

title("2 droplists")

def info():
    text1 = memory["entry 1"].get()
    labels(text=text1,colortext="white",font="16",
           background="grey",row=0,column=1,sticky="center")

    text2 = memory["entry 2"].get()
    labels(text=text2,colortext="white",font="16",
           background="grey",row=1,column=1,sticky="center")

    gender = memory["gender var"].get()
    labels(text=gender,colortext="white",font="16",
           background="grey",row=2,column=1,sticky="center")

    age = memory["age var"].get()
    labels(text=age,colortext="white",font="16",
           background="grey",row=3,column=1,sticky="center")     

entryfield(identifier="entry 1",row=0,column=0)
entryinsert(identifier="entry 1",text="First name",colortext="black")

entryfield(identifier="entry 2",row=1,column=0)
entryinsert(identifier="entry 2",text="Second name",colortext="black")

choices = ["=","Female","Male"]
dropdownlist(choices=choices,variable="gender var",
             default="Gender",row=2,column=0)

age = ["01-06","7-14","15-23","24-31","31-40","41-55","56-70","71-85","86-105"]
dropdownlist(choices=age,variable="age var",
             default="Age",row=3,column=0)

buttons(text="Get info",command=info,
        row=4,column=1,sticky="right")

#clear text when click in entry field
root.bind("<Button-1>", clearbyclick)
root.bind("<Key>", key)

root.mainloop()
