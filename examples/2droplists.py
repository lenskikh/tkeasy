from tkeasy import *

title(window="main",text="The first window")

def info():
    title(window="second",text="Info")
    label(window="second",text="Gender",
      background="green",colortext="white",row=0,column=0)
    label(window="second",text=memory["gender var"].get(),
      background="grey90",row=0,column=1)
    label(window="second",text="Age",
      background="green",colortext="white",row=1,column=0)    
    label(window="second",text=memory["age var"].get(),
      background="grey90",row=1,column=1)    

choices = ["=","Female","Male"]
dropdownlist(window="main",variable="gender var",choices=choices,
             default="Gender",row=0,column=0)

age = ["01-06","7-14","15-23","24-31","31-40","41-55","56-70","71-85","86-105"]
dropdownlist(window="main",variable="age var",choices=age,
             default="Age",row=1,column=0)

button(window="main",text="Get Info",
       command=info,row=2,column=0)
