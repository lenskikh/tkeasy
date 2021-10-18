from tkeasy import *

def new():
    print("new")

def save():
    print("save")

def copy():
    print("copy")

tabs = {"File":{"New":"False","Open":"False","Save":"False","Save as":"False","Close":"False","---":"---","Exit":quit},
"Edit":{"Undo":"False","---":"---","Cut":"False","Copy":"False","Paste":"False","Delete":"False","Select All":"False"},
"Help":{"Help Index":"False","About...":"False","Help":"False"}}

top_menu(tabs)

app_loop()