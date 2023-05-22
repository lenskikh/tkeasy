from tkeasy import TKeasy

gui = TKeasy() #the first window
gui2 = TKeasy()#the second window

def info():
    gui.msg_box_warning("INFO 1",gui.get_info("from_entry"))

def info2():
    gui2.msg_box_warning("INFO 2",gui2.get_info("entry 2"))

#The first window
gui.Title("The first window")
gui.config(size="168x90")

gui.label(text="Provide your info (1)")
gui.entry(row=1)
gui.button(text="Get Info",command=info,row=2)

#The second window
gui2.Title("The second window")
gui2.config(size="168x90")

gui2.label(text="Provide your info (2)",fg="black",bg="lightyellow")
gui2.entry(name="entry 2", row=1)
gui2.button(text="Get Info",command=info2,row=2,)

gui.loop()
gui2.loop()
