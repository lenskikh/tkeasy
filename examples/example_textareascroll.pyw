from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Text area")
gui.config(size="270x200")

def show_info():
    print(gui.get_info("from_text_area"))
    
gui.text_area_scroll(height=10, width=30)
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut blandit neque vitae metus pretium mattis. Fusce lobortis ac ligula at molestie. Sed quam urna, mollis quis egestas vitae, faucibus id massa. Aliquam tempus posuere efficitur. Donec auctor molestie odio quis porta. Nulla nec feugiat eros. Nam vel varius lacus. Mauris pulvinar tortor sed metus aliquam facilisis. Nulla facilisi. Etiam ut purus venenatis, tincidunt orci ac, egestas nibh. Nam sed est non dolor lacinia venenatis sit amet vel purus. Maecenas eleifend vestibulum nulla, sit amet scelerisque purus consectetur vitae. Duis sollicitudin ultricies dui, vitae pharetra sapien. Curabitur ultricies scelerisque efficitur." 
gui.insert_text_area("text_area_scroll", text,fg="grey")
gui.button(text="Show Info", command=show_info,row=1)

gui.loop()
