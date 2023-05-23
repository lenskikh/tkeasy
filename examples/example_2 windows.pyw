from tkeasy import TKeasy

gui = TKeasy()

gui.Title("The first window")
gui.config(size="300x300")

gui2 = TKeasy()

gui2.Title("The second window")
gui2.config(size="300x300")

#packing the first window
gui.loop()
#packing the second window
gui2.loop()
