from tkeasy import *

title("wordpad")

def new_file():
    text_area_clear("area 2")
    
def open_in_menu():
    select_file()
    print(get_info("file"))

def save():
    name_for_save = save_file()
    text_file = open(name_for_save, 'w')
    text_file.write(get_info("area 2"))
    text_file.close()

def copy():
    selected = text_area_select("area 2")
    clipboard_in(selected)

def cut():
    selected = text_area_select("area 2")
    clipboard_in(selected)
    delete_selected("area 2")

def paste():
    paste_text("area 2")

tabs = {"File":{"New":new_file,"Open":open_in_menu,"Save":save,"Save as":save,"Close":new_file,"---":"---","Exit":quit},
"Edit":{"Undo":"False","---":"---","Cut":cut,"Copy":copy,"Paste":paste,"Delete":"False","Select All":"False"},
"Help":{"Help Index":"False","About...":"False","Help":"False"}}

top_menu(tabs)

text_area(name="area 2", row=0,column=0)

app_loop()
