from tkeasy import TKeasy
gui = TKeasy()

gui.Title("The first window")
gui.config(size="300x100", bg = "white")
gui.label(text="The first window", bg = "white")
gui.loop()
