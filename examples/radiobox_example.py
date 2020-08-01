from tkeasy import *

def show_info():
    choice = getinfo("radioBox")
    if choice == "None":
        msgboxwarning("warning","Choose something, please")
    else:
        msgbox("Your choice",f'Your choice is {choice}')

radiobox(window="main",text="Apple",row=0,column=0)
radiobox(window="main",text="Melon",row=1,column=0,value="weight = 2kg")
radiobox(window="main",text="Lemon",row=2,column=0)
button(window="main",text="Show Info",command=show_info,row=3,column=0)
