from tkeasy import TKeasy

gui = TKeasy()

def color():
    color = gui.colorpicker()
    gui.msg_box_warning("PATH","Color is " + color)

gui.button(text="Choose color", command=color)

gui.loop()