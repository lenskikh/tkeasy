from tkeasy import *
import random

def show_info():
    #use random for reopen
    second_window=str(random.random())
    frame2 = {"name_of_frame":str(random.random()),"x":0,"y":0,"border_thickness":1,
              "border_color":"#7cc5ba", "background":"#7cc5ba","padx":5,"pady":5}

    config(window=second_window,size="260x232")
    
    title(window=second_window,text="The second window")
    label(window=second_window,frame=frame2,x=2,y=2,text="The second window",row=0,column=0)
    entry(window=second_window,frame=frame2,x=2,y=10,name="entry2",row=1,column=0)
    insert_text(window=second_window,name="entry2",text="entry",color="gray")
    text_area(window=second_window,frame=frame2,x=6,y=80,name="textarea",row=2,column=0)
    insert_text_area(window=second_window,name="textarea",text="text area",color="gray")
              
button(text="Show Info",command=show_info,row=0,column=0)
app_loop()
