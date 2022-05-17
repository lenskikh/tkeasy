from tkeasy import *

title("Full syntax")
frame_one = {"name_of_frame":"1","x":0,"y":0,"border_thickness":1,
              "border_color":"#7cc5ba", "background":"#7cc5ba","padx":0,"pady":0}

def info():
    print(get_info("ent1"))  #entry
    print(get_info("ch1"))   #checkbox
    print(get_info("ch2"))   #checkbox
    print(get_info("ch3"))   #checkbox
    print(get_info("scale")) #slider
    print(get_info("radiobox"))
    print(get_info("area 1"))

def open_in_menu():
    print(select_file())

config(size="258x700+500+200",background="#7cc5ba",icon="icon.ico")
#config(size="600x300+500+200",background="brown",icon="icon.ico",border="False")

label(frame=frame_one,text=" Fill the form ",colortext="white",background="brown",justification="left",font=14,wrap="300",row=0,column=0,sticky="left",padx=5,pady=5)

entry(frame=frame_one,name="ent1",width=40,row=1,column=0,sticky="left",padx=5,pady=5)

checkbox(frame=frame_one,name="ch1",text="checkbox 1",background="#7cc5ba",activebg="red",row=2,column=0,sticky="left",padx=5,pady=5)
checkbox(frame=frame_one,name="ch2",text="checkbox 2",background="#7cc5ba",activebg="red",row=3,column=0,sticky="left",padx=5,pady=5)
checkbox(frame=frame_one,name="ch3",text="checkbox 3",background="#7cc5ba",activebg="red",row=4,column=0,sticky="left",padx=5,pady=5)

slider(frame=frame_one,name="scale",background="brown",row=5,column=0,sticky="left",padx=5,pady=5)

radiobox(frame=frame_one,text="choice 1",background="#7cc5ba",activebg="yellow",sticky="left",row=6,column=0,padx=5,pady=5)
radiobox(frame=frame_one,text="choice 2",background="#7cc5ba",activebg="yellow",sticky="left",row=7,column=0,padx=5,pady=5)
radiobox(frame=frame_one,text="choice 3",background="#7cc5ba",activebg="yellow",sticky="left",row=8,column=0,padx=5,pady=5)

text_area(frame=frame_one,name="area 1",width=30,height=20,row=10,column=0,padx=5,pady=5)

button(frame=frame_one,text="Button",command=info,row=11,column=0,sticky="left",padx=5,pady=5)

app_loop()


