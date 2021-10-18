from tkeasy import *

def getspin():
    print(get_info("spin"))
    print(get_info("spin2"))

spinbox(name="spin",from_to="0-10",row=0,column=0,padx=10,pady=10)
spinbox(name="spin2",from_to="20-30",row=1,column=0,padx=10,pady=10)

button(text="GET INFO",command=getspin,row=3,column=0)

app_loop()
