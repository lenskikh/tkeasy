from tkeasy import TKeasy

gui = TKeasy()

def show_info():
    def show_info2():
        gui.msg_box("Text area and entry",
                    f'You wrote {second_window.get_info("entry2")},{second_window.get_info("textarea")}')

    #use random for reopen
    second_window = TKeasy()
    second_window.config(size="660x484")
    
    second_window.Title("The second window")
    second_window.label(text="The second window")
    second_window.entry(name="entry2",row=1,column=0)
    second_window.insert_text(name="entry2",text="entry text here",color="gray")
    second_window.text_area(name="textarea",row=2,column=0)
    second_window.insert_text_area(name="textarea",text="enter some text here",color="gray")
    second_window.button(text="Show Info",command=show_info2,row=3,column=0)


gui.button(text="Open the second window",command=show_info)
gui.loop()
