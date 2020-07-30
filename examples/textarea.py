from tkeasy import *

title(window="main",text="Text area")

def show_info():
    print(memory["area"].get("1.0", 'end'))
    
textarea(window="main",name="area",row=0,column=0)
button(window="main",text="Show Info",command=show_info,row=1,column=0)
