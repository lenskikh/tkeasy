from tkeasy import *

title(text="Text area")

top_menu_demo()

def show_info():
    print(get_info("area").strip())
    
text_area(name="area",row=0,column=0)
button(text="Show Info",command=show_info,row=1,column=0)

app_loop()