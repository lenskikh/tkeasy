from tkeasy import *

def new():
    print("new")

def save():
    print("save")

def copy():
    print("copy")

tabs = {"File":{"New":new,"Save":save,"---":"---","Exit":"False"}, "Edit":{"Copy":copy}}

top_menu(tabs)

app_loop()