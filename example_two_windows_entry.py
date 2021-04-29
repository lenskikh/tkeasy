from tkeasy import *

def info():
    print(get_info("entry 1"))

def info2():
    print(get_info("entry 2"))

#The first window
title(text="First window")
geometry(size="196x100")
label(text="Provide your info (1)", background="grey90",sticky="right",row=0,column=0)
entry(name="entry 1",sticky="right",row=1,column=0)
button(text="Get Info",command=info,sticky="right",row=2,column=0)

#The second window
title(window="second",text="Second window")
label(window="second",text="Provide your info (2)",
      colortext="white",background="green",sticky="center",
      row=0,column=0)
entry(window="second",name="entry 2",sticky="center",
           row=1,column=0)
button(window="second",text="Get Info",sticky="center",
       command=info2,row=2,column=0)

app_loop()
