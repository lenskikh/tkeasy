from tkeasy import *

title("Input")

def info():
    print(get_info("ent1"))  #entry

entry(name="ent1",width=20,row=1,column=0,
      sticky="left",padx=5,pady=5)

button(text="Button",command=info,row=11,column=0,sticky="left",padx=5,pady=5)

app_loop()
