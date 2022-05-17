from tkeasy import *

def color():
    color = colorpicker()
    msg_box_warning("PATH","Color is " + color)

button(text="Choose color", command=color,
        row=0,column=0,padx=5,pady=5)

app_loop()