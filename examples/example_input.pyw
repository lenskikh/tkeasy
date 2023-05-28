from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Input")

def info():
    gui.msg_box_warning("INFO", gui.get_info("ent1"))

gui.entry(name="ent1",width=31, padx = 5, pady =5)

gui.button(text="Button",command=info,row=1)

gui.loop()
