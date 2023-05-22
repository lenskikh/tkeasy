from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Spin Boxes")

def getspin():
    gui.msg_box_warning("spin 1","spin 1 = " + gui.get_info("spin") +
                        "\n" + "spin 2 = " + gui.get_info("spin2"))


gui.spinbox(name="spin",from_to="0-10",padx = 10, pady = 10)
gui.spinbox(name="spin2",from_to="20-30",padx = 10, row=1)

gui.button(text="GET INFO",command=getspin,row=3)

gui.loop()
