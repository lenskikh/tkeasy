# tkeasy
Wrapper of tkinter giving an easier way to build a gui interface. GUI Development does not have to be difficult nor painful.</br>
![Screenshot](/screenshots/droplist.png)

## Installation
Type in terminal or cmd</br>
<code>git clone https://github.com/lenskikh/tkeasy.git</code></br>
Run any file with name "example"

## Your fisrt GUI program
```python
from tkeasy import *
title("The first window")
label(text="The first window",row=0,column=0)
app_loop()
```
![Screenshot](/screenshots/thefirst.png)

## Your second GUI program
```python
from tkeasy import *

def show_info():
    choice = get_info("radioBox")
    if choice == "None":
        msg_box_warning("warning","Choose something, please")
    else:
        msg_box("Your choice",f'Your choice is {choice}')

radiobox(text="Apple",row=0,column=0)
radiobox(text="Melon",row=1,column=0,value="weight = 2kg")
radiobox(text="Lemon",row=2,column=0)
button(text="Show Info",command=show_info,row=3,column=0)
app_loop()
```
![Screenshot](/screenshots/radiobox.png)

## Features of tkeasy include:

* **title**
    title(window,text)<br/>
    > text = "New Title"<br/>
    > window (*optional*) = "name"<br/>
    ```python
    from tkeasy import *
    title(text="Title")
    app_loop()
    ``` 
* **size of window and background color**
    config(window,size,bgcolor,border)<br/>
    > size (*optional*) = "500x500"<br/>
    > window (*optional*) = "name"<br/>
    > background(*optional*) = "color"<br/>
    > border(*optional*) = "False". "True" by default.<br/>
    ```python
    from tkeasy import *
    geometry(size="300x300",bgcolor="white")
    app_loop()
    ```
    OR
    ```python
    from tkeasy import *
    geometry('200x150+400+300')
    app_loop()
    ```
    > 400 shifted on X-axis and 300 shifted on Y-axis

* **return values** <br />
    get_info("name")<br />
    Any name should be unique.<br />
    How do I get information from a text field? Give the field a unique name that will not be repeated in other widgets. For example "text area 01". Therefore, if you want to get information from this field, use get_info("text area 01"). The only exception applies only to the radio box. The radio box always has a name "radiobox" get_info("radiobox")

* **button**
    button(window,text,command,sticky,padx,pady,row,column)<br/>
    > window (*optional*) = "name"<br/>
    > text="text" - text of button<br/>
    > command=somedef - appeal to function in your code (*Without brackets and quotation marks. See examples in code*)<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/>
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*)
    ```python
    from tkeasy import *
    def show_info():
        print("button pressed")
    button(text="Show Info",command=show_info,row=0,column=0)
    app_loop()
    ```
    ![Screenshot](/screenshots/button.png)

* **label**
    label(window,text,colortext,background,label_font,row,column,sticky,padx,pady)<br/>
    > window (*optional*) = "name"<br/>
    > text="text" - text of label<br/>
    > colortext (*optional*) = "red" (You can use hex color instead)<br/>
    > background (*optional*) = "#241e14" (You can use hex color)<br/>
    > font (*optional*) = "Times", 13 (font in quotation marks, size of font after comma)<br/>
    > justify (*optional*) = alignment for text in label, "center" by default<br/>
    > wrap (*optional*) =  wrap for text, 600 by default<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*)    
    ```python
    from tkeasy import *
    label(text="Label text",row=0,column=0)
    app_loop()
    ```
    ![Screenshot](/screenshots/label.png)

* **checkboxes**
    checkbox(window,name,text,row,column,sticky,padx,pady)<br/>
    > window (*optional*) = "name"<br/>
    > name = "name" - name of checkbox<br/>
    > text = "text" - text of checkbox<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*) 
    ```python
    checkbox(name="checkbox 1", text="Apple",row=0,column=0,sticky = "left")
    checkbox(name="checkbox 2", text="Banan",row=0,column=0,sticky = "left")
    ```
    The whole example
    ```python
    from tkeasy import *

    def info():
        print(get_info("checkbox 1"))
        print(get_info("checkbox 2"))

    label(text="What a fruit do you like?",row=0,column=0)

    checkbox(name="checkbox 1", text="Apple",
            row=1,column=0,sticky = "left")

    checkbox(name="checkbox 2", text="Banan",
            row=2,column=0,sticky = "left")

    button(text="show info",
        command=info,row=3,column=0)

    app_loop()
    ```
    ![Screenshot](/screenshots/checkbox.png)

* **radiobox**
    radiobox(window,text,value,row,column,sticky,padx,pady)<br/>
    > Radiobox by default is not selected<br/>
    > window (*optional*) = "name"<br/>
    > text = "text" - text for radiobox<br/>
    > value (*optional*) = "value". If value in not set then text of radiobox is default value<br />
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*)     
    ```python
    radiobox(text="Apple",row=0,column=0)
    radiobox(text="Melon",row=1,column=0,value="weight = 2kg")
    ```
   
    The whole example
    ```python
    from tkeasy import *

    def show_info():
        choice = get_info("radiobox")
        print(choice)

    radiobox(text="Apple",row=0,column=0)
    radiobox(text="Melon",row=1,column=0,value="weight = 2kg")
    radiobox(text="Lemon",row=2,column=0)
    button(text="Show Info",command=show_info,row=3,column=0)

    app_loop()
    ```
    ![Screenshot](/screenshots/radio.png)

* **dropdown list**
    dropdown_list(window,variable,choices,default,row,column,sticky,padx,pady)<br/>
    > window (*optional*) = "name"<br/>
    > variable = "variable"<br /> 
    > choices = list should assign in your code. For example: choices = ("One","Two","Three")<br/>
    > default = "default" - Setting the default value. For example "One" from your list choices<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*)     
    ```python
    fruits = ["Apple","Pear","Banana","Kiwi"]
    dropdown_list(variable="fruits var",choices=age,default="Chose fruit",row=0,column=0)
    ```

    The whole example
    ```python
    from tkeasy import *

    def info():  
        print(get_info("age var"))
        
    age = ["24-31","31-40","41-55","56-70","71-85"]
    dropdown_list(variable="age var",choices=age,
                default="Age",row=1,column=0)

    button(text="Get Info",
        command=info,row=2,column=0)

    app_loop()
    ```    
    ![Screenshot](/screenshots/droplist.jpg)

* **file browse**
    select_file<br/>
    > command=select_file<br/>
    > Use button method and in the command point out select_file
    ```python
    from tkeasy import *

    def show_info():
        choice = get_info("radiobox")
        print(choice)

    radiobox(text="Apple",row=0,column=0)
    radiobox(text="Melon",row=1,column=0,value="weight = 2kg")
    radiobox(text="Lemon",row=2,column=0)
    button(text="Show Info",command=show_info,row=3,column=0)

    app_loop()
    ```
    ![Screenshot](/screenshots/file.jpg)

* **folder browse**
    select_folder<br/>
    > command=select_folder
    > Use button method and in the command point out select_folder
    ```python
    from tkeasy import *

    def readname():
        print(get_info("folder"))

    button(text='FOLDER BROWSER',command=select_folder,
        row=0,column=0,sticky="center")

    button(text="Print Name Of Folder",
        command=readname,row=1,column=0,
        sticky="center")

    app_loop()
    ```
    ![Screenshot](/screenshots/folder.png)

* **one-line text input**
    entry(window,name,row,column,sticky,padx,pady)<br/>
    > window (*optional*) = "name"<br/>
    > name = "name" - name of entry<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*) 
    ```python   
    from tkeasy import *

    def frominput():
        print(get_info("entry 1"))

    entry(name="entry 1",row=0,column=0)

    button(text='from input',command=frominput,
        row=1,column=0,sticky="center")

    app_loop()
    ```  
    ![Screenshot](/screenshots/inputline.PNG)

* **multi-line text input**
    text_area(name,row,column,sticky,padx,pady)<br/>
    > text_area_scroll(name,row,column,sticky,padx,pady)<br/>
    > scroll looks ugly on some OS, use text_area() if text is short.<br/>
    > window (*optional*) = "name"<br/>    
    > name = "name" - name of text area<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*) 
    ```python 
    from tkeasy import *

    title(text="Text area")

    def show_info():
        print(get_info("area").strip())
        
    text_area(name="area",row=0,column=0)
    button(text="Show Info",command=show_info,row=1,column=0)

    app_loop()
    ```
    ![Screenshot](/screenshots/area.png)

    or
    ```python 
    text_area_scroll(name="area",row=0,column=0)
    ```
    Adds a scroll to the right. Use it if the text is long.

* **insert text in input field**<br />
    Adds text to a text field. Can be used as hints for the user.
    insert_text(name,text,color)<br />
    > name = "name" - name of text area that you are used before<br/>
    > text = "text" which you want to insert in a text area<br/>
    > color = "#323648" color of text
    ```python 
    from tkeasy import *

    entry(name="firstname",row=0,column=0)
    insert_text(name="firstname",text="First name",color = "gray")

    entry(name="secondname",row=1,column=0)
    insert_text(name="secondname",text="Second name",color = "gray")

    app_loop()
    ```
    ![Screenshot](/screenshots/insert.png)

* **insert text in text area field**<br />
    ```python 
    from tkeasy import *
    
    text_area(name="area",row=0,column=0)
    insert_text_area(name="area",text="Second name",color = "gray")

    app_loop()
    ```
    ![Screenshot](/screenshots/insert2.png)

* **scroll-able output**<br/>
    Use two methods for scroll-able output<br/>
    method text_area_scroll() and method insert_text_area()
    ```python 
    text_area_scroll(name="area output",row=0,column=0)
    insert_text_area(name="area output",text="some text",color = "black")
    ```     
* **multiple windows** <br/>
    Unlimited number of windows can be open at the same time<br/>
    Add "window" in the second and third window. The first window should be without window="the first window". See example example_two_windows_entry.py Otherwise, you will get three windows.
    ```python
    from tkeasy import *
    import random

    def show_info():
            #Random is used as a solution to reopen the window.
            win=str(random.random())
            title(window=win,text="The second window")
            label(window=win,text="The second window",row=0,column=0)
            entry(window=win,name="entry2",row=1,column=0)
            insert_text(window=win,name="entry2",text="entry",color="gray")
            text_area(window=win,name="textarea",row=2,column=0)
            insert_text_area(window=win,name="textarea",text="text area",color="gray")
              
    button(text="Show Info",command=show_info,row=0,column=0)
    app_loop()
    ```
    ![Screenshot](/screenshots/w.png)

* **clickable text**
    label_click()
    ```python
    label(text="Link 1",row=0,column=0)
    label_click().bind("<Button-1>",lambda url:msg_box("Clicked","Link 1"))

    label(text="Link 2",row=1,column=0)
    label_click().bind("<Button-1>",lambda url:msg_box("Clicked","Link 2"))
    ```
    ![Screenshot](/screenshots/labelclick.png)

* **images**<br />
    Support format gif and png only. Animated gif is not supported. Use png format for good quality. Unfortunately, due to the way tkinter works, you can't use images in the second window or in the third window. <br />
    > photo(window,file,row,column)
    ```python
    photo("1.png",0,0)
    photo("2.png",1,0)
    ```
    ![Screenshot](/screenshots/photo.png)
* **clickable images**
    photo_click()
    ```python
    photo(file="1.png",row=0,column=0)
    photo_click().bind("<Button-1>",lambda url:
                    msg_box(title="Clicked",message="Picture 1"))
    ```
* **sliders**<br />
    (horizontal by default) <br />
    slider(window,name,pos,row,column,sticky,padx,pady)<br />
    > window (*optional*) = "name"<br/>
    > name = "name" - name of slider<br/>
    > pos = "vertical" if want to change position of a slider<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/>
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*)    
    ![Screenshot](/screenshots/sliders.png)
* **separator**<br/>
    separator line<br/>
    separator(window,column_length,padx,pady)<br/>
    > window (*optional*) = "name"<br/>
    > column_length = 1<br/>
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*)    
    ```python
    from tkeasy import *
    separator(column_length=1)
    app_loop()
    ```
    ![Screenshot](/screenshots/separator.png)

* **Top menu**<br/>
    See example_topmenu.py If you need a code.
    ![Screenshot](/screenshots/topmenu.jpg)
* app_loop()
    Add app_loop() at the end of an app. If the app is launched from terminal, it will immediately close without app_loop() 