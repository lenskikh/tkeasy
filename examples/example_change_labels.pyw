from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Change labels")

lables = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
i = 0

def info():
    global i
    try:
        gui.label(text=lables[i],row=0,column=0)
        i+= 1
    except:
        i = 0
gui.label(text="Hello World !",row=0,column=0)
gui.button(text="Change labels",command=info,row=1,column=0)


gui.loop()
