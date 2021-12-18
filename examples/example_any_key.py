from tkeasy import *

def keydown(event):
    print ('Key was pressed = ', event.char)

entry(name="ent",row=0,column=0)
hotkey("<KeyPress>",command=keydown)

app_loop()
