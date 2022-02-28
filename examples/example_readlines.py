from tkeasy import *

title(text="Cards")

config(size="230x100+500+300",background="white")

frame1 = {"name_of_frame":"first_frame","background":"white","border_thickness":1,"border_color":"green","x":13,"y":5}
frame2 = {"name_of_frame":"second_frame","background":"white","x":10,"y":50}

filename = "words.txt"
i = 0

with open(filename) as f:
    content = f.readlines()

def next_word():
    global i
    try:
        label(frame=frame1,text=content[i].strip(),background="white",width=12,row=0,column=0)
    except:
        label(frame=frame1,text="End of file",background="white",width=12,row=0,column=0)
    i+=1

button(frame=frame2,text="Next word",command=next_word,row=1,column=0)

app_loop()