from tkeasy import *

def show_info():
    choice = get_info("radiobox")
    if choice == "None":
        msg_box_warning("warning","Choose something, please")
    else:
        msg_box("Your choice",f'Your choice is {choice}')

radiobox(frame="1",x=70,y=3,text="an Apple",row=0,column=0)
radiobox(frame="2",x=70,y=30,text="a Melon",row=1,column=0,value="weight = 2kg")
radiobox(frame="2",x=70,y=30,text="a Lemon",row=2,column=0)
button(text="Show Info",command=show_info,row=3,column=0)

app_loop()
