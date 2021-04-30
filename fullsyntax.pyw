from tkeasy import *

title("Full syntax")

def info():
   print(get_info("ent1"))  #entry
   print(get_info("ch1"))   #checkbox
   print(get_info("ch2"))   #checkbox
   print(get_info("ch3"))   #checkbox
   print(get_info("scale")) #slider
   

config(size="600x300+500+200", bgcolor="brown",icon="icon.ico")
#config(size="600x300+500+200", bgcolor="brown",border="False")

label(text="Fill the form",colortext="white",background="#34423f",justification="right",font=14,wrap="300",row=0,column=0,sticky="left",padx=5,pady=5)

entry(name="ent1",width=40,row=1,column=0,sticky="left",padx=5,pady=5)

checkbox(name="ch1",text="checkbox 1",row=2,column=0,sticky="left",padx=5,pady=5)
checkbox(name="ch2",text="checkbox 2",row=3,column=0,sticky="left",padx=5,pady=5)
checkbox(name="ch3",text="checkbox 3",row=4,column=0,sticky="left",padx=5,pady=5)

slider(name="scale",row=5,column=0,sticky="left",padx=5,pady=5)

button(text="Button",command=info,row=6,column=0,sticky="left",padx=5,pady=5)

app_loop()


