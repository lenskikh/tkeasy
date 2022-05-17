from tkeasy import entry,button,get_info,msg_box_warning,app_loop

def frominput():
    msg_box_warning("Info",get_info("entry 1"))

entry(name="entry 1",row=0,column=0)

button(text='from input',command=frominput,
    row=1,column=0,sticky="center")

app_loop()
