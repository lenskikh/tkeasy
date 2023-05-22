from turtle import width
from tkeasy import TKeasy

gui = TKeasy()

gui.Title("wordpad")
gui.config(size="250x170")

def new_file():
    gui.clear_area("area 2")
    
def open_in_menu():
    selected = gui.select_file()
    with open(selected, 'r', encoding = 'utf-8') as filehandle:
        read_file = filehandle.read()

    gui.insert_text_area(name = "area 2", text = read_file)

def save():
    name_for_save = gui.save_file()
    text_file = open(name_for_save, 'w')
    text_file.write(gui.get_info("area 2"))
    text_file.close()

def copy():
    selected = gui.text_area_select("area 2")
    gui.clipboard_in(selected)

def cut():
    selected = gui.text_area_select("area 2")
    gui.clipboard_in(selected)
    gui.delete_selected("area 2")

def paste():
    gui.paste_text("area 2")

tabs = {"File":{"New":new_file,"Open":open_in_menu,"Save":save,"Save as":save,"Close":new_file,"---":"---","Exit":quit},
"Edit":{"Undo":"False","---":"---","Cut":cut,"Copy":copy,"Paste":paste,"Delete":"False","Select All":"False"},
"Help":{"Help Index":"False","About...":"False","Help":"False"}}

gui.top_menu(tabs)

gui.text_area(name="area 2",width=30,height=10,row=0,column=0)

gui.loop()
