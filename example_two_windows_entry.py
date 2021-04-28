from tkeasy import *

def info():
    print(get_info("entry 1"))

def info2():
    print(get_info("entry 2"))

#The first window
title(text="First window")
geometry(size="196x100")
label(text="Provide your info", background="grey90",row=0,column=0)
entry(name="entry 1", row=1,column=0)
button(text="Get Info", command=info,row=2,column=0)

#The second window
title(window="second",text="Second window")
label(window="second",text="Provide your info",
      colortext="white",background="green",
      row=0,column=0)
entry(window="second",name="entry 2",
           row=1,column=0)
button(window="second",text="Get Info",
       command=info2,row=2,column=0)

app_loop()