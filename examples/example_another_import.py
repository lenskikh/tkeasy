from tkeasy import entry,button,get_info,app_loop

def frominput():
    print(get_info("entry 1"))

entry(name="entry 1",row=0,column=0)

button(text='from input',command=frominput,
    row=1,column=0,sticky="center")

app_loop()
