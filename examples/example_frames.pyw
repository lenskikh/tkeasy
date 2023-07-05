from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Big Title")
gui.config(size = "500x300")

def pr(event):
    print ("test")

#press enter and hold, move the mouse    
gui.hotkey("<Return>",command=gui.move_window)

gui.frames (frame = "frame 1", x= 0, y = 0,
            highlightthickness = 1,
            highlightbackground = "green",
            padx = 5,
            pady = 5)

gui.label (text = "Mens Necklace",
           wrap = 150, height = 2,
           font = "Arial", background = "white",
           fg = "green", justify = "left",row = 0)

gui.label (text = "Woman Necklace",
           wrap = 150, height = 2,
           font = "Arial", background = "white",
           fg = "red", justify = "center",row = 1)

file = gui.image_file("button.png")
gui.button (image = file, text = "Button", border = 0, command = False, row = 2)

gui.button (text = "info 2", command = False, row = 3)
gui.checkbox (name = "chk 1", text = "check 1", row = 4)

gui.frames (frame = "frame 2", x= 150, y = 0,
            background = "#FF00FF",
            highlightthickness = 1,
            highlightbackground = "blue")

gui.label (text = "Second frame",
           wrap = 150, height = 2,
           font = "Arial", background = "yellow",
           fg = "Blue")

gui.label (text = "Second frame 2",
           wrap = 150, height = 2,
           font = "Arial", background = "yellow",
           fg = "Blue", justify = "center",row = 1)


gui.loop()


