from tkeasy import *

#update x with every press of a button
x = 0

def update():
    global x
    x+=1
    print(x)

button(text="+1",command=update,row=0,column=0)

app_loop()
