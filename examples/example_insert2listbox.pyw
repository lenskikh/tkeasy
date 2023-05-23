from tkeasy import TKeasy

gui = TKeasy()

gui.Title("ListBox")
gui.config(size="50x150+400+100")
gui.config(bg="lightgreen")
gui.config(icon="icon.ico")
gui.config(border = "False")

def clear():
    gui.clear_area("Listbox")

def insert_to_listbox():
    text2 = ("AAA","BBB","CCC","DDD","FFFF")
    gui.listbox_insert("Listbox",text2)

text = ("1111","2222","3333","4444","5555")

gui.button(text="Clear",command=clear,row=0,column=0)
gui.listbox(height=5,width=5,row=1,column=0)
gui.listbox_insert(name= "Listbox", text = text)

gui.button(text="Insert",command=insert_to_listbox,row=2,column=0)

gui.loop()
