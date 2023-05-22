#ask folder - gui widget
from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Ask file")

def showfile():
    gui.msg_box_warning("PATH",gui.select_file())

gui.label(text="ASK FILE", fg="white", background="BLUE", padx = 5, pady = 5,)

gui.button(text="FILE BROWSER", command=showfile, padx = 5, row=1, column=0)

gui.loop()
