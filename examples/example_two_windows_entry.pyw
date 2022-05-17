from tkeasy import *

def info():
    msg_box_warning("INFO 1",get_info("entry 1"))

def info2():
    msg_box_warning("INFO 2",get_info("entry 2"))

frame_1 = {"name_of_frame":"frame_1","x":0,"y":0,"border_thickness":1,
              "border_color":"#7cc5ba", "background":"lightyellow","padx":0,"pady":0}

frame_2 = {"name_of_frame":"frame_2","x":0,"y":0,"border_thickness":1,
              "border_color":"#7cc5ba", "background":"#7cc5ba","padx":0,"pady":0}

#The first window
title(text="First window")
config(size="168x90")

label(frame=frame_1,text="Provide your info (1)",sticky="right",row=0,column=0)
entry(frame=frame_1,name="entry 1",sticky="right",row=1,column=0)
button(frame=frame_1,text="Get Info",command=info,sticky="right",row=2,column=0)

#The second window
title(window="second",text="Second window")
config(window="second",size="168x90")

label(window="second",frame=frame_2,text="Provide your info (2)",
      colortext="black",background="lightyellow",sticky="center",
      row=0,column=0)
entry(window="second",frame=frame_2,name="entry 2",sticky="center",
           row=1,column=0)
button(window="second",frame=frame_2,text="Get Info",sticky="center",
       command=info2,row=2,column=0)

app_loop()
