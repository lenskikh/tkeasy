from tkeasy import *
import random

def show_info():
    #use random for reopen
    second_window=str(random.random())
    
    title(window=second_window,text="The second window")
    label(window=second_window,text="The second window",row=0,column=0)
    entry(window=second_window,name="entry2",row=1,column=0)
    insert_text(window=second_window,name="entry2",text="entry",color="gray")
    text_area(window=second_window,name="textarea",row=2,column=0)
    insert_text_area(window=second_window,name="textarea",text="text area",color="gray")
              
button(text="Show Info",command=show_info,row=0,column=0)
app_loop()
