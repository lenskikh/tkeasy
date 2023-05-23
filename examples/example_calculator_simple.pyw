from tkeasy import *

gui = TKeasy()

gui.Title("Calc")
gui.config(size="205x250",bg="white")

gui.frames (frame = "frame 1", x= 21, y = 10,
            highlightthickness = 1,
            highlightbackground = "green",
            padx = 5,
            pady = 5)

gui.entry(name="entry 1",width=25)
gui.focus("entry 1")

screen = ""

def update(number):
    global screen
    screen+=number
    gui.clear_area("entry 1")
    gui.insert_text(name="entry 1",text=screen,color="black")

def result():
    #You can use entry field for input digit from keyboard
    from_screen = gui.get_info("entry 1").strip()
    gui.clear_area("entry 1")
    total = eval(from_screen)
    gui.insert_text(name="entry 1",text=total,color="black")

def shortcut(event):
    result()

def AC():
    global screen
    screen = ""
    gui.clear_area("entry 1")
    gui.insert_text(name="entry 1",text=screen,color="black")

gui.frames (frame = "frame 2", x= 20, y = 50,
            background = "lightgreen",
            highlightthickness = 1,
            highlightbackground = "black",
            padx = 5, pady = 5)

gui.button(text=" AC ",command=AC,fg="black",bg="#edce54",pady = 5, row=0,column=0)

gui.button(text="  7  ",command=lambda:update("7"),pady = 5, padx = 5, row=1,column=0)
gui.button(text="  8  ",command=lambda:update("8"),pady = 5, padx = 5, row=1,column=1)
gui.button(text="  9  ",command=lambda:update("9"),pady = 5, padx = 5, row=1,column=2)

gui.button(text="  4  ",command=lambda:update("4"),pady = 5, padx = 5, row=2,column=0)
gui.button(text="  5  ",command=lambda:update("5"),pady = 5, padx = 5, row=2,column=1)
gui.button(text="  6  ",command=lambda:update("6"),pady = 5, padx = 5, row=2,column=2)

gui.button(text="  1  ",command=lambda:update("1"),pady = 5, padx = 5, row=3,column=0)
gui.button(text="  2  ",command=lambda:update("2"),pady = 5, padx = 5, row=3,column=1)
gui.button(text="  3  ",command=lambda:update("3"),pady = 5, padx = 5, row=3,column=2)

gui.button(text="  0  ",command=lambda:update("0"),pady = 5, padx = 5, row=4,column=0)
gui.button(text="  .  ",command=lambda:update("."),pady = 5, padx = 5, row=4,column=1)
gui.button(text="  =  ",fg="white",bg="red",command=result,row=4,column=2)

gui.button(text="  /  ",command=lambda:update("/"),pady = 5, padx = 5, row=1,column=4)
gui.button(text="  x  ",command=lambda:update("*"),pady = 5, padx = 5, row=2,column=4)
gui.button(text="  -  ",command=lambda:update("-"),pady = 5, padx = 5, row=3,column=4)
gui.button(text="  +  ",command=lambda:update("+"),pady = 5, padx = 5, row=4,column=4)

#press enter for get result
gui.hotkey("<Return>", shortcut)

gui.loop()
