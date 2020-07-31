from tkeasy import *

title(window="main",text="Text area")

def show_info():
    print(memory["area"].get("1.0", 'end'))
    
textareascroll(window="main",name="area",row=0,column=0)
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut blandit neque vitae metus pretium mattis. Fusce lobortis ac ligula at molestie. Sed quam urna, mollis quis egestas vitae, faucibus id massa. Aliquam tempus posuere efficitur. Donec auctor molestie odio quis porta. Nulla nec feugiat eros. Nam vel varius lacus. Mauris pulvinar tortor sed metus aliquam facilisis. Nulla facilisi. Etiam ut purus venenatis, tincidunt orci ac, egestas nibh. Nam sed est non dolor lacinia venenatis sit amet vel purus. Maecenas eleifend vestibulum nulla, sit amet scelerisque purus consectetur vitae. Duis sollicitudin ultricies dui, vitae pharetra sapien. Curabitur ultricies scelerisque efficitur." 
instertextarea("area",text,"grey")
button(window="main",text="Show Info",command=show_info,row=1,column=0)
