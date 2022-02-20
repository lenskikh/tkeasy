from tkeasy import *

title(text="Text area")
config(size="270x200")

def show_info():
    print(get_info("area"))
    
text_area_scroll(name="area",height=10,width=30,row=0,column=0)
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut blandit neque vitae metus pretium mattis. Fusce lobortis ac ligula at molestie. Sed quam urna, mollis quis egestas vitae, faucibus id massa. Aliquam tempus posuere efficitur. Donec auctor molestie odio quis porta. Nulla nec feugiat eros. Nam vel varius lacus. Mauris pulvinar tortor sed metus aliquam facilisis. Nulla facilisi. Etiam ut purus venenatis, tincidunt orci ac, egestas nibh. Nam sed est non dolor lacinia venenatis sit amet vel purus. Maecenas eleifend vestibulum nulla, sit amet scelerisque purus consectetur vitae. Duis sollicitudin ultricies dui, vitae pharetra sapien. Curabitur ultricies scelerisque efficitur." 
insert_text_area("area",text,"grey")
button(text="Show Info",command=show_info,row=1,column=0)

app_loop()
