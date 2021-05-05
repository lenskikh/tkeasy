from tkeasy import *

title("Full syntax")

def info():
   print(get_info("ent1"))  #entry
   print(get_info("ch1"))   #checkbox
   print(get_info("ch2"))   #checkbox
   print(get_info("ch3"))   #checkbox
   print(get_info("scale")) #slider
   print(get_info("radiobox"))
   print(get_info("area 1"))
   print(text_area_select("area 1"))

def open_in_menu():
    select_file()
    print(get_info("file"))

config(size="300x600+500+200",background="lightblue",icon="icon.ico")
#config(size="600x300+500+200",background="brown",icon="icon.ico",border="False")

top_menu_demo()

label(text=" Fill the form ",colortext="white",background="brown",justification="left",font=14,wrap="300",row=0,column=0,sticky="left",padx=5,pady=5)

entry(name="ent1",width=40,row=1,column=0,sticky="left",padx=5,pady=5)

checkbox(name="ch1",text="checkbox 1",background="lightblue",activebg="lightblue",row=2,column=0,sticky="left",padx=5,pady=5)
checkbox(name="ch2",text="checkbox 2",background="lightblue",activebg="lightblue",row=3,column=0,sticky="left",padx=5,pady=5)
checkbox(name="ch3",text="checkbox 3",background="lightblue",activebg="red",row=4,column=0,sticky="left",padx=5,pady=5)

slider(name="scale",background="brown",row=5,column=0,sticky="left",padx=5,pady=5)

radiobox(text="choice 1",background="lightblue",activebg="lightblue",sticky="left",row=6,column=0,padx=5,pady=5)
radiobox(text="choice 2",background="lightblue",activebg="lightblue",sticky="left",row=7,column=0,padx=5,pady=5)
radiobox(text="choice 3",background="lightblue",activebg="lightblue",sticky="left",row=8,column=0,padx=5,pady=5)

separator(column_length=1,padx=5,pady=5)

text_area(name="area 1",row=10,column=0,padx=5,pady=5)

button(text="Button",command=info,row=11,column=0,sticky="left",padx=5,pady=5)

app_loop()


