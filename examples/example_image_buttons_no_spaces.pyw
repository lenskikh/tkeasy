from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Buttons")
gui.config(size="246x245")

def show_info(name):
    gui.msg_box_warning("Button clicked", f"{name} was clicked")

image = gui.image_file("noborderbutton.png")

#Do not use text, compound mode give a pixel between buttons
gui.button(image=image, borderwidth=0,  highlightthickness=0, command=lambda:show_info("Button 1"), row=0, column = 0)
gui.button(image=image, borderwidth=0,  highlightthickness=0,  command=lambda:show_info("Button 2"), row=0, column = 1)

gui.loop()
