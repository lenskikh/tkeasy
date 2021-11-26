from tkeasy import *

title("ListBox")
config(size="100x150")

def clear():
    clear_area("listbox")

def insert_to_listbox():
    text2 = ("AAA","BBB","CCC","DDD","FFFF")
    listbox_insert("listbox",text2)

text = ("1111","2222","3333","4444","5555")

button(text="Clear",command=clear,row=0,column=0)
listbox(name="listbox",height=5,width=5,row=1,column=0,text=text)
button(text="Insert",command=insert_to_listbox,row=2,column=0)

app_loop()
