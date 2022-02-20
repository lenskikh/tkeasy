from tkeasy import *

title(text="Text area")
config(size="250x200")

def show_info():
    print(get_info("area").strip())
    
text_area(name="area",height=10,width=30,row=0,column=0)
button(text="Show Info",command=show_info,row=1,column=0)

app_loop()
