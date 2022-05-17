from tkeasy import *

title("Check passwords")

config(size="300x100")

def match_password():
    if get_info("ent") != get_info("ent2"):
        clear_area(name="ent2")
        msg_box_warning("warning","The password doesn't match!")
        print(get_info("ent"))
    else:
        photo(file="check.png",row=0,column=2)  
        photo(file="check.png",row=1,column=2) 

label(text="Password",sticky="left",row=0,column=0)
label(text="Confirm password",sticky="left",row=1,column=0)

entry(name="ent",asterisks="*",row=0,column=1)
entry(name="ent2",asterisks="*",row=1,column=1)

button(text="Check password",command=match_password, row=2,column=1)

app_loop()