from tkeasy import TKeasy

gui = TKeasy()

gui.config(size="250x130")

def info():
    gui.msg_box_warning("Title - Sliders data","Velocity = " + str(gui.get_info("scale 1")) +
                        "\n" + "Chrominance = " + str(gui.get_info("scale 2")))

gui.Title("Sliders")

gui.label(text="Velocity")
#horizontal scale by default    
gui.slider(name="scale 1",orient="horizontal",column=1)

gui.label(text="Chrominance",row=2)
#horizontal scale by default    
gui.slider(name="scale 2",orient="horizontal",row=2,column=1)
gui.button(text="get slider values",command=info,row=3,column=1)

gui.loop()
