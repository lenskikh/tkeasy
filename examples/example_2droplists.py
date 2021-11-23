from tkeasy import *
import random

title(text="The first window")



def info():
    second = str(random.random())
    frame2 = {"name_of_frame":str(random.random()),
              "x":5,"y":5,"border_thickness":1,
              "border_color":"#7cc5ba",
              "background":"white",
              "padx":5,"pady":5}
    
    title(window=second,text="Info")
    config(window=second,size="160x78",background="white")
    
    label(window=second,frame=frame2,text=" Gender ",background="green",colortext="white",row=0,column=0)
    label(window=second,frame=frame2,text=get_info("gender var"),
      background="grey90",row=0,column=1)
    label(window=second,frame=frame2,text=" Age ",
      background="green",colortext="white",row=1,column=0)    
    label(window=second,frame=frame2,text=get_info("age var"),
      background="grey90",row=1,column=1)    

choices = ["=","Female","Male"]
dropdown_list(variable="gender var",choices=choices,
             default="Gender",row=0,column=0)

age = ["01-06","7-14","15-23","24-31","31-40","41-55","56-70","71-85","86-105"]
dropdown_list(variable="age var",choices=age,
             default="Age",row=1,column=0)

button(text="Get Info",
       command=info,row=2,column=0)

#you need use it if run code in vsc
app_loop()
