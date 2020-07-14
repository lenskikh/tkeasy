from tkeasy import *

def show_info():
    print(radioBox.get())

radiobox(default="Melon",text="Apple",row=0,column=0)
radiobox(text="Melon",row=1,column=0)
radiobox(text="Lemon",row=2,column=0)
buttons(text="Show Info",command=show_info,row=3,column=0)
