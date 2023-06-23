from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Text area")
gui.config(size="246x245", transparent = 0.9)

def show_info():
    gui.msg_box_warning("FROM TEXT AREA",gui.get_info("area").strip())

image = gui.image_file("button.png")

gui.label(text="Enter some text and press button 'Show info'", sticky='nswe', pady = 5)    
gui.text_area(name="area",height=10,width=30,row=1)
gui.button(text="Show Info",image=image, borderwidth=0, compound="center", command=show_info,row=2)

gui.loop()
