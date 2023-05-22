from tkeasy import TKeasy

gui = TKeasy()

#update x with every press of a button
x = 0

def update():
    global x
    x+=1
    gui.label(text=x, row = 0)

gui.button(text="+1", row = 1, padx = 5, command=update)

gui.loop()
