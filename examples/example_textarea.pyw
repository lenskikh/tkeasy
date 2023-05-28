from tkeasy import *

gui = TKeasy()

gui.Title("Text area")
gui.config(size="246x200")

def show_info():
    gui.msg_box_warning("FROM TEXT AREA",gui.get_info("area").strip())
    
gui.text_area(name="area",height=10,width=30,)
gui.button(text="Show Info",command=show_info,row=1)

gui.loop()
