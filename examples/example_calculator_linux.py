from tkeasy import *

title("Calc")
config(size="290x260",background="white")

the_first_frame = {"name_of_frame":"first_frame","x":27,"y":10,
                   "border_thickness":1,"border_color":"black",
                   "background":"#7cc5ba","padx":7,"pady":7}

entry(frame=the_first_frame,name="entry 1",width=27,row=1,column=0)
focus("entry 1")

the_second_frame={"name_of_frame":"second_frame","x":27,"y":60,
                  "border_thickness":1,"border_color":"black",
                  "background":"#7cc5ba","padx":5,"pady":5}

screen = ""

def update(number):
    global screen
    screen+=number
    clear_area("entry 1")
    insert_text(name="entry 1",text=screen,color="black")

def result():
    #You can use entry field for input digit from keyboard
    from_screen = get_info("entry 1").strip()
    clear_area("entry 1")
    total = eval(from_screen)
    insert_text(name="entry 1",text=total,color="black")

def shortcut(event):
    result()

def AC():
    global screen
    screen = ""
    clear_area("entry 1")
    insert_text(name="entry 1",text=screen,color="black")

button(frame=the_second_frame,text=" AC ",command=AC,colortext="black",background="#edce54",row=0,column=0)

button(frame=the_second_frame,text="  7  ",command=lambda:update("7"),row=1,column=0)
button(frame=the_second_frame,text="  8  ",command=lambda:update("8"),row=1,column=1)
button(frame=the_second_frame,text="  9  ",command=lambda:update("9"),row=1,column=2)

button(frame=the_second_frame,text="  4  ",command=lambda:update("4"),row=2,column=0)
button(frame=the_second_frame,text="  5  ",command=lambda:update("5"),row=2,column=1)
button(frame=the_second_frame,text="  6  ",command=lambda:update("6"),row=2,column=2)

button(frame=the_second_frame,text="  1  ",command=lambda:update("1"),row=3,column=0)
button(frame=the_second_frame,text="  2  ",command=lambda:update("2"),row=3,column=1)
button(frame=the_second_frame,text="  3  ",command=lambda:update("3"),row=3,column=2)

button(frame=the_second_frame,text="  0  ",command=lambda:update("0"),row=4,column=0)
button(frame=the_second_frame,text="  .  ",command=lambda:update("."),row=4,column=1)
button(frame=the_second_frame,text="  =  ",colortext="white",background="red",command=result,row=4,column=2)

button(frame=the_second_frame,text="  /  ",command=lambda:update("/"),row=1,column=4)
button(frame=the_second_frame,text="  x  ",command=lambda:update("*"),row=2,column=4)
button(frame=the_second_frame,text="  -  ",command=lambda:update("-"),row=3,column=4)
button(frame=the_second_frame,text="  +  ",command=lambda:update("+"),row=4,column=4)

#press enter for get result
advanced().bind("<Return>", shortcut)

app_loop()
