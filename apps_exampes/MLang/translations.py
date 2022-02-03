from tkeasy import *

title(text="Translate images")
config(size="500x300")


def show_info():
    text = get_info("area") 
    text = text.split(" ")
    for i in text:
        print(i)

text_area(name="area",width=60,height=15,row=0,column=0)

button(text="Convert",command=show_info,row=1,column=0)

app_loop()