from tkeasy import *

def show_info():
    choice = get_info("radioBox")
    if choice == "None":
        msg_box_warning("warning","Choose something, please")
    else:
        msg_box("Your choice",f'Your choice is {choice}')

radiobox(text="Apple",row=0,column=0)
radiobox(text="Melon",row=1,column=0,value="weight = 2kg")
radiobox(text="Lemon",row=2,column=0)
button(text="Show Info",command=show_info,row=3,column=0)

app_loop()