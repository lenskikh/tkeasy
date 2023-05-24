from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Top Menu")
gui.config(size="250x170")

tabs = {"File":{"New":"False","Open":"False"}}

gui.top_menu(tabs)

gui.loop()
