from tkeasy import TKeasy

gui = TKeasy()

gui.config(border="False")

def help():
    gui.label(text="Press ctrl + left click of the mouse for move window",
          wrap="200",row=0,column=0)

tabs = {"File":{"Exit":quit},"About":{"Help":help}}
gui.top_menu(tabs)

#move a window by shortcut ctrl+left click of the mouse
gui.hotkey("<Control-B1-Motion>", gui.move_window)

gui.loop()
