#ask folder - gui widget
from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Ask Folder")

def askfolder():
    gui.msg_box_warning("PATH",gui.select_folder())

gui.label(text="ASK FOLDER",fg="white", background="green", padx = 5)

gui.button(text='CHOOSE FOLDER',command=askfolder, padx = 5, row=1,column=0)

gui.loop()
