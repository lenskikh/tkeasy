from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Frames")
gui.config(size="205x250",bg="white")

gui.frames (frame = "frame 1", x= 21, y = 10,
            highlightthickness = 1,
            highlightbackground = "black",
            padx = 5,
            pady = 5)

gui.label(text="the first frame", bg = "#f5dc4b")

gui.frames (frame = "frame 2", x= 21, y = 50,
            highlightthickness = 1,
            highlightbackground = "black",
            background = "#cadb66",
            padx = 5,
            pady = 5)

gui.label(text="the second frame", bg = "white")

gui.loop()
