from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Print a char")

def keydown(event):
    text2 = f'Key was pressed = {event.char}' 
    gui.label(text = text2, row = 1)

gui.entry(name="ent", width = 30, padx = 5, pady = 5)
gui.hotkey("<KeyPress>",command=keydown)


gui.loop()
