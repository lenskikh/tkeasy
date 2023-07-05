from tkeasy import TKeasy

gui = TKeasy()

def info():
    gui.msg_box("Checkbox 1",gui.get_info("checkbox 1"))
    gui.msg_box("Checkbox 2",gui.get_info("checkbox 2"))
    gui.msg_box("Checkbox 3",gui.get_info("checkbox 3"))

gui.label(text="What a fruit do you like?")

gui.checkbox(name="checkbox 1", sticky = "w", text="Apple",row=1)

gui.checkbox(name="checkbox 2", sticky = "w", text="Banan",row=2)

gui.checkbox(name="checkbox 3", sticky = "w", text="Orange",row=3)

gui.button(text="show info",command=info,row=4)

gui.loop()
