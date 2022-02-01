from tkeasy import *

title("Check passwords")

config(size="300x100")

def keydown(event):
    #focus checks which the entry field is using
    focus = advanced().focus_get()
    password(event,focus,"ent","password")
    password(event,focus,"ent2","confirm password")

def match_password():
    if get_password("password") != get_confirm_password("confirm password"):
        clear_area(name="ent2")
        msg_box_warning("warning","The password doesn't match!")
        clear_confirm_password()
    else:
        photo(file="check.png",row=0,column=2)  
        photo(file="check.png",row=1,column=2) 

def clear_forms(event):
    clear_area(name="ent") 
    clear_area(name="ent2") 
    clear_password()
    clear_confirm_password()

label(text="Password",sticky="left",row=0,column=0)
label(text="Confirm password",sticky="left",row=1,column=0)

entry(name="ent",row=0,column=1)
entry(name="ent2",row=1,column=1)

hotkey("<KeyPress>",command=keydown)
hotkey("<BackSpace>",command=clear_forms)

button(text="Check password",command=match_password, row=2,column=1)

app_loop()