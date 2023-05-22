from tkeasy import TKeasy

gui = TKeasy()

def new():
    print("new")

def save():
    print("save")

def copy():
    print("copy")

tabs = {"File":{"New":new,"Open":lambda:print("Open"),"Save":save,"Save as":"False","Close":"False","---":"---","Exit":quit},
"Edit":{"Undo":"False","---":"---","Cut":"False","Copy":copy,"Paste":"False","Delete":"False","Select All":"False"},
"Help":{"Help Index":"False","About...":"False","Help":"False"}}

gui.top_menu(tabs)

gui.loop()
