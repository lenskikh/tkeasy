from tkeasy import *

title("Change labels")

lables = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
i = 0

def info():
    global i
    try:
        label(text=lables[i],row=0,column=0)
        i+= 1
    except:
        i = 0
label(text="Hello World !",row=0,column=0)
button(text="Change labels",command=info,row=1,column=0)


app_loop()
