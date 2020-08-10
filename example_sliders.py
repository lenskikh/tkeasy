from tkeasy import *

def info():
    print("Velocity - " + str(get_info("scale 1")))
    print("Chrominance - " + str(get_info("scale 2")))

title("Sliders")

label(text="Velocity",row=0,column=0)
#horizontal scale by default    
scale(name="scale 1",row=0,column=1)
separator(column_length=2,pady=5)

label(text="Chrominance",row=2,column=0)
#horizontal scale by default    
scale(name="scale 2",row=2,column=1)
button("get slider values",info,3,1)

app_loop()
