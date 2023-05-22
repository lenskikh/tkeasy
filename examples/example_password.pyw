from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Check passwords")

gui.config(size="300x100")

def match_password():
    if gui.get_info("ent") != gui.get_info("ent2"):
        gui.clear_area("ent2")
        gui.msg_box_warning("warning","The password doesn't match!")
    else:
        gui.photo(file="check.png",column=2)  
        gui.photo(file="check.png",row=1,column=2) 

gui.label(text="Password")
gui.label(text="Confirm password", row=1)

gui.entry(name="ent",show = "*", column=1)
gui.entry(name="ent2",show = "*", row=1, column=1)

gui.button(text="Check password",command=match_password, row=2,column=1)

gui.loop()
