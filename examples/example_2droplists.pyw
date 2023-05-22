from tkeasy import TKeasy

gui = TKeasy()

gui.Title("The first window")
gui.config(bg = "white")


def info():
    gui2 = TKeasy()
    gui2.Title("Info")
    gui2.config(size="160x78", bg = "white")
    
    gui2.label(text=" Gender ",background="green",fg ="white")
    gui2.label(text=gui.get_info("gender_var"),bg ="grey90",column=1)
    gui2.label(text=" Age ",background="green",fg ="white",row=1)    
    gui2.label(text=gui.get_info("age_var"), bg ="grey90",row=1,column=1)    
    gui2.label(text=" Hair color ",background="green",fg ="white",row=2)    
    gui2.label(text=gui.get_info("hair"), bg ="grey90",row=2,column=1)        

choices = ["genger","Female","Male"]
gui.dropdown_list(variable="gender_var",choices=choices, bg="green", fg = "white")

age = ["age","01-06","7-14","15-23","24-31","31-40","41-55","56-70","71-85","86-105"]
gui.dropdown_list(variable="age_var",choices=age,row=1,bg="red", fg = "white")

hair = ["color hair","brown hair","red hair","blonde hair","gray hair"]
gui.dropdown_list(variable="hair",choices=hair,row=2,bg="yellow", fg = "black")

gui.button(text="Get Info",command=info,row=3, bg  = "lightgreen")

#you need use it if run code in vsc
gui.loop()
