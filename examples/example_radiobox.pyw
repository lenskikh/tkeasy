from tkeasy import TKeasy

gui = TKeasy()

def show_info():
    choice = gui.get_info("radiobox")
    if choice == "None":
        gui.msg_box_warning("warning","Choose something, please")
    else:
        gui.msg_box("Your choice",f'Your choice is {choice}')

gui.radiobox(text="Apple", sticky = "w")
gui.radiobox(text="Melon", sticky = "w", row=1)
gui.radiobox(text="Lemon", sticky = "w", row=2)
gui.button(text="Show Info",command=show_info, padx = 5, row=3)

gui.loop()
