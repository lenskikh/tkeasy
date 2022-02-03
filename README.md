[Russian / Русская документация](#Russian)

# tkeasy
Wrapper of tkinter giving an easier way to build a gui interface. GUI Development does not have to be difficult nor painful.</br>
![Screenshot](/screenshots/droplist.png)

## Installation
Type in terminal or cmd</br>
<code>git clone https://github.com/lenskikh/tkeasy.git</code></br>
Run any file with name "example"

On Arch linux install tk first
    ```python
    sudo pacman -S tk
    ```
<br />
On Ubuntu
    ```python
    sudo apt-get install python3-tk 
    ```

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

* **title**<br/>
    title(window,text)<br/>
    > text = "New Title"<br/>
    > window (*optional*) = "name"<br/>
    ```python
    from tkeasy import *
    title(text="Title")
    app_loop()
    ``` 
* **size of window and background color**<br/>
    config(window,size,bgcolor,border)<br/>
    > size (*optional*) = "500x500"<br/>
    > window (*optional*) = "name"<br/>
    > background(*optional*) = "color"<br/>
    > border(*optional*) = "False". "True" by default.<br/>
    ```python
    from tkeasy import *
    config(size="300x300",bgcolor="white")
    app_loop()
    ```
    OR
    ```python
    from tkeasy import *
    config('200x150+400+300')
    app_loop()
    ```
    > 400 shifted on X-axis and 300 shifted on Y-axis

* **return values** <br />
    get_info("name")<br />
    Any name should be unique.<br />
    How do I get information from a text field? Give the field a unique name that will not be repeated in other widgets. For example "text area 01". Therefore, if you want to get information from this field, use get_info("text area 01"). The only exception applies only to the radio box. The radio box always has a name "radiobox" get_info("radiobox")

* **button**<br/>
    button(window,text,command,sticky,padx,pady,row,column)<br/>
    > window (*optional*) = "name"<br/>
    > text="text" - text of button<br/>
    > command=somedef - appeal to function in your code (*Without brackets and quotation marks. See examples in code*)<br/>
    > background - background color of button. *Unfortunately, it doesn't work on mac os*<br/>
    > colortext - text color of button<br/> 
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/>
    > padx (*optional*) = 2 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 2 (*Number. Without brackets and quotation marks*)
    ```python
    from tkeasy import *
    def show_info():
        print("button pressed")
    button(text="Show Info",background="#7cc5ba",colortext="white",command=show_info,row=0,column=0)
    app_loop()
    ```
    ![Screenshot](/screenshots/button.png)

* **label**<br/>
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
    > padx (*optional*) = 2 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 2 (*Number. Without brackets and quotation marks*)    
    ```python
    from tkeasy import *
    label(text="Label text",row=0,column=0)
    app_loop()
    ```
    ![Screenshot](/screenshots/label.png)

* **checkboxes**<br/>
    checkbox(window,name,text,row,column,sticky,padx,pady)<br/>
    > window (*optional*) = "name"<br/>
    > name = "name" - name of checkbox<br/>
    > text = "text" - text of checkbox<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 2 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 2 (*Number. Without brackets and quotation marks*) 
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

* **radiobox**<br/>
    radiobox(window,text,value,row,column,sticky,padx,pady)<br/>
    > Radiobox by default is not selected<br/>
    > window (*optional*) = "name"<br/>
    > text = "text" - text for radiobox<br/>
    > value (*optional*) = "value". If value in not set then text of radiobox is default value<br />
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 2 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 2 (*Number. Without brackets and quotation marks*)     
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

* **spinbox**<br/>
    spinbox(window,name,from_to,row,column,sticky,padx,pady)<br/>
    > window (*optional*) = "name"<br/>
    > name = "name" - unique name for get_info<br/>
    > from_to = range between two digits. Use a dash in the range "0-10"<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 2 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 2 (*Number. Without brackets and quotation marks*)   
    ```python 
    from tkeasy import *

    def getspin():
        print(get_info("spin"))
        print(get_info("spin2"))

    spinbox(name="spin",from_to="0-10",row=0,column=0,padx=10,pady=10)
    spinbox(name="spin2",from_to="20-30",row=1,column=0,padx=10,pady=10)

    button(text="GET INFO",command=getspin,row=3,column=0)

    app_loop()    
    ```
    ![Screenshot](/screenshots/spinbox.PNG)

* **dropdown list**<br/>
    dropdown_list(window,variable,choices,default,row,column,sticky,padx,pady)<br/>
    > window (*optional*) = "name"<br/>
    > variable = "variable"<br /> 
    > choices = list should assign in your code. For example: choices = ("One","Two","Three")<br/>
    > default = "default" - Setting the default value. For example "One" from your list choices<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 2 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 2 (*Number. Without brackets and quotation marks*)     
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

* **file browse dialog**<br/>
    **select_file()**<br/>
    Gives the full path<br/>
    > command=select_file<br/>
    > Use button method and in the command point out select_file
    ```python
    from tkeasy import *

    title(text="Ask file")

    def showfile():
        print (select_file())

    label(text="ASK FILE",colortext="white",
        background="BLUE",row=0,column=0)

    button(text="FILE BROWSER",
        command=showfile,row=1,column=0)

    app_loop()
    ```
    ![Screenshot](/screenshots/file.jpg)

    **select_file_name()**<br/>
    Gives only the file name without the full path<br/>
    ```python
    from tkeasy import *

    print(select_file_name())

    app_loop()
    ```

* **folder browse dialog**<br/>
    select_folder()<br/>
    > command=select_folder
    > Use button method and in the command point out select_folder
    ```python
    from tkeasy import *

    title(text="Ask Folder")
    config(size="50x60")

    def askfolder():
        print(select_folder())

    label(text="ASK FOLDER",colortext="white",
        background="green",row=0,column=0)

    button(text='CHOOSE FOLDER',command=askfolder,
        row=1,column=0)

    app_loop()
    ```
    ![Screenshot](/screenshots/folder.png)

* **Save file dialog**<br/>
    save_file()<br/>
    The user can save information from the document, for this we need to find out the name of the file where he wants to save. It is better to use for the top menu.
    ```python
    from tkeasy import *

    print(save_file()) 
    app_loop()   
    ```

* **one-line text input**<br/>
    entry(window,name,row,column,sticky,padx,pady)<br/>
    > window (*optional*) = "name"<br/>
    > name = "name" - name of entry<br/>
    > width = The length of the entry widget<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 2 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 2 (*Number. Without brackets and quotation marks*) 
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

* **multi-line text input**<br/>
    text_area(name,row,column,sticky,padx,pady)<br/>
    > text_area_scroll(name,row,column,sticky,padx,pady)<br/>
    > scroll looks ugly on some OS, use text_area() if text is short.<br/>
    > window (*optional*) = "name"<br/>    
    > name = "name" - name of text area<br/>
    > height = "height" - size of text area by height<br/>
    > width = "width" - size of text area by width<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 2 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 2 (*Number. Without brackets and quotation marks*) 
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
    > color (optional) = "#323648" color of text. Black color text by default.
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

* **focus**<br />
    You can set the focus on a widget.<br />
    ```python 
    focus(name_of_widget)
    ```

* **scroll-able output**<br/>
    Use two methods for scroll-able output<br/>
    method text_area_scroll() and method insert_text_area()
    ```python 
    text_area_scroll(name="area output",row=0,column=0)
    insert_text_area(name="area output",text="some text",color = "black")
    ``` 

* **Select text**<br />
    Get data from selected text in text area.
    ```python
    text_area_select()
    ``` 

* **Clear data**<br />
    Clear data in text area or listbox.
    ```python
    clear_area(name="")
    ```

* **Clipboard_in**<br />
    clipboard_in(selected)<br />
    See wordpad.py You can find out how it works.
    ```python
    selected = text_area_select(name) #Get selected text from text_area
    clipboard_in(selected) #Copy selected text to clipboard
    ```

* **Delete selected text**<br />
    ```python
    delete_selected("name of text_area")
    ```
    Select a text and delete it<br />

* **Paste text**<br />
    ```python
    paste_text("name of text_area")
    ```
    Paste text from clipboard

* **Frames** <br/>
    Frames allow you to arrange widgets in any order<br/>
    For example, you place a horizontal long widget, and shorter widgets under it in another frame.<br/>
    ![Screenshot](/screenshots/calc.png)<br/>
    In windows and mac, frames have a different measurement system. Therefore, the program that you wrote in windows on the mac needs to be changed by specifying other values for the length of the widget, frame and window.<br/>
    The values of the frame parameters are passed through the dictionary.<br/>
    ```python
    the_first_frame = {"name_of_frame":"first_frame","x":27,"y":10,
                   "border_thickness":1,"border_color":"black",
                   "background":"#7cc5ba","padx":5,"pady":5}
    ```
    Then at the beginning of each widget you insert the dictionary name
    ```python
    button(frame=the_first_frame,text=" AC ",command=AC,colortext="black",background="#edce54",row=0,column=0)
    ```
    Wherever you want to apply the same frame, you use the same name. The wrapper recognizes the repetition and will use it from the previously specified dictionary.<br/>
    > name_of_frame - name of frame. Only the frame name is required, all other parameters are optional.<br/>
    Specify coordinates where the frame starts from. <br/>
    > x(*optional*) - shift by horizontal. 0 by default<br/>
    > y(*optional*) - shift by vertical. 0 by default<br/>
    > border_thickness(*optional*) - thickness of frame. None by default<br/>
    > border_color(*optional*) - color of border. None by default<br/>
    > background(*optional*) - color of background. None by default<br/>
    > padx(*optional*) - offset from widgets by x. 1 by default <br/>
    > pady(*optional*) - offset from widgets by y. 1 by default<br/>


* **multiple windows** <br/>
    Unlimited number of windows can be open at the same time.<br/>
    Add "window" in the second and third window. The first window should be without window="the first window". See example example_two_windows_entry.py Otherwise, you will get three windows. For the second window to work correctly, it is necessary to specify the frame in the second window.
    ```python
    from tkeasy import *
    import random

    def show_info():
            #Random is used as a solution to reopen the window.
            win=str(random.random())
            frame_one = {"name_of_frame":str(random.random())}
            
            title(window=win,text="The second window")
            label(window=win,frame=frame_one,text="The second window",row=0,column=0)
            entry(window=win,frame=frame_one,name="entry2",row=1,column=0)
            insert_text(window=win,name="entry2",text="entry",color="gray")
            text_area(window=win,frame=frame_one,name="textarea",row=2,column=0)
            insert_text_area(window=win,name="textarea",text="text area",color="gray")
                
    button(text="Show Info",command=show_info,row=0,column=0)
    app_loop()
    ```
    ![Screenshot](/screenshots/w.png)

* **clickable text**<br/>
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
    
* **clickable images**<br/>
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
    > padx (*optional*) = 2 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 2 (*Number. Without brackets and quotation marks*)    
    ![Screenshot](/screenshots/sliders.png)

* **Top menu**<br/>
    See example_topmenu.py If you need the whole code.<br />
    ```json
    tabs = {"File":{"New":"False","Open":"False","Save":"False","Save as":"False","Close":"False","---":"---","Exit":quit},
    "Edit":{"Undo":"False","---":"---","Cut":"False","Copy":"False","Paste":"False","Delete":"False","Select All":"False"},
    "Help":{"Help Index":"False","About...":"False","Help":"False"}}
    ```
    ![Screenshot](/screenshots/topmenu.jpg)

    On the mac, the menu will appear in the toolbar<br />
    ![Screenshot](/screenshots/menubar_mac.jpg)

* **color picker**<br />
    ```python
    from tkeasy import *

    def color():
        color = colorpicker()
        print(color)

    button(text="Choose color", command=color,
            row=0,column=0,padx=5,pady=5)

    app_loop()
    ```
    ![Screenshot](/screenshots/colorpicker.png)

* **Listbox**<br />
    A list box is a graphical control element that allows the user to select one or more items from a list contained within a static, multiple line text box. The user clicks inside the box on an item to select it.<br />
    ```python
    from tkeasy import *
    import os
    import glob

    text = glob.glob("*.*")
    listbox(name="listbox",height=30,width=35,row=1,column=0,text=text)

    app_loop()

    ```
    ![Screenshot](/screenshots/listbox.png)

* **listbox_item_selected**<br />    
    With this method, you can get the data where the cursor is.
    ```python
    listbox(name="listbox",height=30,width=35,row=0,column=0,text=text)
    listbox_item_selected("listbox")
    ```
* **Advanced mode**<br />  
    Using the advanced mode you can create original tkinter widgets.
    ```python
    from tkeasy import *

    Label(advanced(), text="Test", relief=RAISED ).pack()

    app_loop()
   ```

* **hotkeys**<br/>
    ```python
    hotkey("<Return>",command)
    ```
    For the second window
    ```python
    hotkey(window="win",frame="frame_one",key="<Return>",command=command)
    ```

    Summary of the most common events with some keypress names explained:<br />
    ```
    <Button-1> Button 1 is the leftmost button, button 2 
        is the middle button (where available), and 
        button 3 the rightmost button.

    <B1-Motion> The mouse is moved, with mouse button 1 
        being held down (use B2 for the middle 
        button, B3 for the right button). 

    <ButtonRelease-1> Button 1 was released. This is probably a 
        better choice in most cases than the Button event, because 
        if the user accidentally presses the button, they can 
        move the mouse off the widget to avoid setting off the event.

    <Double-Button-1>Button 1 was double clicked. 
        You can use Double or Triple as prefixes.

    <Return> The user pressed the Enter key.
    ```

    ```python
    #Print any key that was pressed in entry field
    from tkeasy import *

    def keydown(event):
        print ('Key was pressed = ', event.char)

    entry(name="ent",row=0,column=0)
    hotkey("<KeyPress>",command=keydown)

    app_loop()
    ```

* **Password widget**<br />  
This widget allows you to insert asterisks instead of letters.<br/>
    > focus - Set the focus so that the widget understands where to insert the asterisks<br/>
    > entry_name - entry name of field that you gonna use for password <br/>
    > password_name. - Use only "password" or "confirm password"<br/>
![Screenshot](/screenshots/password_asterisks.png)<br/>
See code in example_password.py

* **clear password**<br />   
    ```python  
    clear_password()
    ```
    Erases the password from memory

* **clear confirm password**<br />  
    ```python  
    clear_confirm_password()
    ```
    Erases the confirm password from memory

* **Get a password**<br /> 
    Retrieves the user's password from memory<br /> 
    password = get_info("password")<br />

* **Get the confirmed password**<br /> 
    Retrieves the user's confirmed password from memory<br /> 
    confirm password = get_info("confirm password")<br />

* **quit**<br/>
    For destroy window.
    ```python
    button(text='Quit',command=quit,
        row=0,column=0,sticky="center")
    ```
* **app_loop()**<br/>
    Add app_loop() at the end of an app. If the app is launched from terminal, it will immediately close without app_loop() 


# Russian
## Что такое tkeasy
**tkeasy** – это обертка встроенной gui-библиотеки tkinter без внешних зависимостей. Это означает, что tkeasy может работать на любой сборке python. 
Основная мысль, сделать написание графического интерфейса, как можно проще. Но так как приходиться придерживаться идеи без зависимостей, то имеются некоторые ограничения. Например, поддерживаются только изображения в формате gif и png. В связи с этим данная обертка подходит под написание небольших приложений, однако, если вы планируете создавать нечто серьезное, то автор добавил такую возможность. Об этом ниже.

## Установка
Установите git https://git-scm.com/</br>
Затем наберите в командной строке (или в терминале)</br>
<code>git clone https://github.com/lenskikh/tkeasy.git</code></br>
Примеры смотрите в файлах, которые начинаются с "example"</br>

На Arch Linux нужно доустановить tk, например, на Manjaro
    ```
    sudo pacman -S tk
    ```
<br />
На Ubuntu 
    ```python
    sudo apt-get install python3-tk 
    ```

## Ваша первая GUI программа
```python
from tkeasy import *

title("The first window")
label(text="The first window",row=0,column=0)
app_loop()
```
![Screenshot](/screenshots/thefirst.png)

title - заголовок окна</br>
label - текстовой виджет, после скобок text="ваш текст", далее расположение виджета, в данной обертке есть только одна возможность - по сетке, которая состоит из рядов row и колонок column. Сетка выбрана из-за наиболее предсказуемого поведения.
app_loop() необходим, если мы запускаем программу из терминала, он не дает ей закрыться сразу после запуска.

## Ваша вторая GUI программа
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

В данной программе мы используем виджет radiobox и button. Чтобы собрать информацию со всех виджетов, мы используем функцию show_info на которую ссылается кнопка в command=show_info, то есть после command мы делаем ссылку на функцию. В самой функции мы собираем информацию при помощи get_info(), который отвечает за сбор информации со всех виджетов. После скобок мы указываем название виджета, которое придумываем сами. Например, если мы берем с виджета input и называем его entry, то получится get_info("entry"). Для радиобокса предусмотрено стандартное название get_info("radioBox"), так как каждый радиобокс уникален. 

* **Импорт**<br/>
    Во всех примерах используется 
    ```python
    from tkeasy import *
    ``` 
    Однако, в среде профи это считается плохой практикой. Если вас это не напрягает, можете использовать import *<br/>
    Под хорошей практикой подразумевается импорт самых необходимых частей. Обязательные к импорту всегда будут get_info,app_loop, далее через запятую вы перечисляете необходимые виджеты. Смотрите пример ниже
    ```python
    from tkeasy import entry,button,get_info,app_loop
    ``` 

## Доступные виджеты:

* **title**<br/>
    title(window,text)<br/>
    Заголовок окна<br/>
    > text = "Текст заголовка"<br/>
    > window (*необязательно*) = "name". window используется для отрытия новых окн. Если у вас нет таковых, то не указываете window, как в примере ниже.<br/>
    ```python
    from tkeasy import *
    title(text="Title")
    app_loop()
    ``` 

* **размер окна, цвет фона, толщина рамки**<br/>
    config(window,size,bgcolor,border)<br/>
    config() - общие настройки приложения
    > size (*необязательно*) = "500x500"<br/>
    Размер окна, опционально (т.е. указывать не обязательно). Размер указывается через знак х. Первое значение - горизонталь, второе - вертикаль. size="100x200". Вы также можете указать месторасположения окна, первое значение по горизонтале, второе вертикаль. Расположение обозначается знаком + config(size="300x200+700+700")<br/>
    > window (*необязательно*) = "name"<br/>
        window используется для отрытия новых окн. Если у вас нет таковых, то не указывайте.<br/>
    > background(*необязательно*) = "color"<br/>
        Цвет общего фона в приложении.<br/>
    > border(*необязательно*) = "False". Значение "True" по умолчанию.<br/>
        Наличие рамки вокруг окна.
    ```python
    from tkeasy import *
    config(size="300x300",bgcolor="white")
    app_loop()
    ```
    ИЛИ
    ```python
    from tkeasy import *
    config('200x150+400+300')
    app_loop()
    ```

* **Движение окна по горячей клавише, расширенный режим**<br/>
    Расширенный режим advanced(), позволяет расширять функционал не предусмотренный оберткой.<br/>
    move_window - для движения окна<br/>
    ```python
    from tkeasy import *

    config(border="False")
    advanced().bind("<Control-B1-Motion>", move_window)
    app_loop()
    ```
    При отсутствии рамки, нет возможности передвигать окно, данный код позволяет двигать окно по зажатию клавиши ctrl

* **Сбор информации с виджетов.** <br />
    get_info("имя виджета")<br />
    Каждому виджету вы даете уникальное имя по которому get_info("") их находит. Исключение "radiobox". Например, вы желаете получить информацию из текстового виджета entry далее в name="даёте имя"
    ```python
    (name="entry 1",row=0,column=0)
    ```
    Вместо entry 1, вы можете придумать что-то другое, например, entry_field. В get_info("") вы пишите имя поля, которое вы придумали, например get_info("entry 1") или get_info("entry_field").
    ```python
    from tkeasy import *

    def frominput():
    #выведет инфу с текстового поля entry 1
        print(get_info("entry 1"))

    entry(name="entry 1",row=0,column=0)

    button(text='from input',command=frominput,
        row=1,column=0,sticky="center")
    ```
    
* **Виджет button (кнопка).** <br />
    После заполнения информации в виджетах, пользователь нажимает на кнопку, которая ссылается на функцию, где get_info() собирает информацию со всех виджетов.
    button(window,text,command,sticky,padx,pady,row,column)
    > window (*необязательно*) = "имя"<br/>
    > text="text" - текст на кнопке<br/>
    > command=somedef - ссылка на функцию (*Без скобок и кавычек*)<br/>
    > sticky (*необязательно*) = приклеивание кнопки внутри ячейки сетки. Укажите "left" или "right" или "center"<br/>
    > padx (*необязательно*) = отступ от виджета, добавляет пространство по горизонтале.<br/>
    > pady (*необязательно*) = отступ от виджета, добавляет пространство по вертикале.<br/>
    > row = номер ряда расположения виджета в сетке<br/>
    > column = номер колонки расположения виджета в сетке<br/>

* **Виджет label (этикетка)**<br/>
    label(window,text,colortext,background,label_font,row,column,sticky,padx,pady)<br/>
    Виджет для публикации текста<br/>
    > window (*необязательно*) = "имя". window используется для отрытия новых окн. Если у вас нет таковых, то не указываете window".<br/>
    > text="text" - текст, который будет опубликован<br/>
    > colortext (*необязательно*) = "red" (Можете писать цвет в HEX или просто писать название цвета "black" или "green")<br/>
    > background (*необязательно*) = "#241e14" (Можете писать цвет в HEX)<br/>
    > font (*необязательно*) = "Times", 13 (шрифт указываете в кавычках, лучше использовать тот, который есть на большинстве компьютеров. После запятой указываете размер шрифта)<br/>
    > justify (*необязательно*) = выравнивание текста в текстовом виджете, "center" по умолчанию<br/>
    > wrap (*необязательно*) =  переносы в текстовом виджете, 600 пикселей по умолчанию<br/>
    > row = номер ряда расположения виджета в сетке<br/>
    > column = номер колонки расположения виджета в сетке<br/>
    > sticky (*необязательно*) = приклеивание кнопки внутри ячейки сетки. Укажите "left" или "right" или "center"<br/> 
    > padx (*необязательно*) = отступ от виджета, добавляет пространство по горизонтале.<br/>
    > pady (*необязательно*) = отступ от виджета, добавляет пространство по вертикале    
    ```python
    from tkeasy import *
    label(text="Label text",row=0,column=0)
    app_loop()
    ```
    ![Screenshot](/screenshots/label.png)

* **Виджет чекбокс**<br/>
    checkbox(window,name,text,row,column,sticky,padx,pady)<br/>
    Данный виджет используется, чтобы сделать галочками какие-то выборы. В отличие от радиобокса выбор не является уникальным. Их может быть несколько.<br/>
    > window (*необязательно*) = "имя". window используется для отрытия новых окн. Если у вас нет таковых, то не указываете window".<br/>
    > name = "имя" - укажите имя чекбокса по которому get_info() его найдет, чтобы забрать информацию с него<br/>
    > text = "текст", который будет отображаться напротив чекбокса<br/>
    > row = номер ряда расположения виджета в сетке<br/>
    > column = номер колонки расположения виджета в сетке<br/>
    > sticky (*необязательно*) = приклеивание кнопки внутри ячейки сетки. Укажите "left" или "right" или "center"<br/> 
    > padx (*необязательно*) = отступ от виджета, добавляет пространство по горизонтале.<br/>
    > pady (*необязательно*) = отступ от виджета, добавляет пространство по вертикале  
    ```python
    checkbox(name="checkbox 1", text="Apple",row=0,column=0,sticky = "left")
    checkbox(name="checkbox 2", text="Banan",row=0,column=0,sticky = "left")
    ```
    Полный пример
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

* **Виджет радиобокс**<br/>
    radiobox(window,text,value,row,column,sticky,padx,pady)<br/>
    Используется для обозначения уникального выбора<br/>
    > По умолчанию ни один радиобокс не выбран.<br/>
    > window (*необязательно*) = "имя". window используется для отрытия новых окн. Если у вас нет таковых, то не указываете window".<br/>
    > text = "текст", который будет отображаться напротив радиобокса<br/>
    > value (*необязательно*) = "значение". Вы можете указать значение в радиобоксе и получать информацию по нему, а не по тексту. Смотрите пример ниже. Если значение не указано, то информация будет получена по тексту<br />
    > row = номер ряда расположения виджета в сетке<br/>
    > column = номер колонки расположения виджета в сетке<br/>
    > sticky (*необязательно*) = приклеивание кнопки внутри ячейки сетки. Укажите "left" или "right" или "center"<br/> 
    > padx (*необязательно*) = отступ от виджета, добавляет пространство по горизонтале.<br/>
    > pady (*необязательно*) = отступ от виджета, добавляет пространство по вертикале     
    ```python
    radiobox(text="Apple",row=0,column=0)
    radiobox(text="Melon",row=1,column=0,value="weight = 2kg")
    ```
   
    Полный пример
    ```python
    from tkeasy import *

    def show_info():
        #Радиобоксу не нужно давать имя для get_info(), по умолчанию используется "radiobox"
        choice = get_info("radiobox")
        print(choice)

    radiobox(text="Apple",row=0,column=0)
    radiobox(text="Melon",row=1,column=0,value="weight = 2kg")
    radiobox(text="Lemon",row=2,column=0)
    button(text="Show Info",command=show_info,row=3,column=0)

    app_loop()
    ```
    ![Screenshot](/screenshots/radio.png)

* **Виджет Спинбокс**<br/>
    spinbox(window,name,from_to,row,column,sticky,padx,pady)<br/>
    Спинбокс виджет, который позволяет нам выбирать из фиксированного набора значений цифрового типа.<br/>
    > window (*необязательно*) = "имя". window используется для отрытия новых окн. Если у вас нет таковых, то не указываете window".<br/>
    > name = "имя" по которому get_info() найдет значение, чтобы забрать информацию с этого виджета<br/>
    > from_to = укажите границу. Например, from_to="0-10" будет предложенно пользователю  выбрать от 0 до 10<br/>
    > row = номер ряда расположения виджета в сетке<br/>
    > column = номер колонки расположения виджета в сетке<br/>
    > sticky (*необязательно*) = приклеивание кнопки внутри ячейки сетки. Укажите "left" или "right" или "center"<br/> 
    > padx (*необязательно*) = отступ от виджета, добавляет пространство по горизонтале.<br/>
    > pady (*необязательно*) = отступ от виджета, добавляет пространство по вертикале   
    ```python 
    from tkeasy import *

    def getspin():
        print(get_info("spin"))
        print(get_info("spin2"))

    spinbox(name="spin",from_to="0-10",row=0,column=0,padx=10,pady=10)
    spinbox(name="spin2",from_to="20-30",row=1,column=0,padx=10,pady=10)

    button(text="GET INFO",command=getspin,row=3,column=0)

    app_loop()    
    ```
    ![Screenshot](/screenshots/spinbox.PNG)

* **Дропдаун лист виджет**<br/>
    dropdown_list(window,variable,choices,default,row,column,sticky,padx,pady)<br/>
    Дроплист виджет(или «выпадашка») — элемент графического интерфейса пользователя (выпадающий / раскрывающийся список), дающий возможность юзеру выбрать одно из нескольких существующих значений параметра.<br/>
    > window (*необязательно*) = "имя". window используется для отрытия новых окн. Если у вас нет таковых, то не указываете window".<br/>
    > variable = "имя" по которому get_info() найдет значение, чтобы забрать информацию с этого виджета<br /> 
    > choices = список для дроплиста, здесь вы указываете варианты, которые будут предложены пользователю. Например: choices = ("One","Two","Three")<br/>
    > default = вариант, который пользователь видит по умолчанию. <br/>
    > row = номер ряда расположения виджета в сетке<br/>
    > column = номер колонки расположения виджета в сетке<br/>
    > sticky (*необязательно*) = приклеивание кнопки внутри ячейки сетки. Укажите "left" или "right" или "center"<br/> 
    > padx (*необязательно*) = отступ от виджета, добавляет пространство по горизонтале.<br/>
    > pady (*необязательно*) = отступ от виджета, добавляет пространство по вертикале    
    ```python
    fruits = ["Apple","Pear","Banana","Kiwi"]
    dropdown_list(variable="fruits var",choices=age,default="Chose fruit",row=0,column=0)
    ```

    Полный пример
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

* **Файловый диалог виджет**<br/>
    select_file()<br/>
    Данный виджет используется для вызова файлового диалога, который позволяет пользователю указать на файл.<br/>
    > command=select_file<br/>
    > Обращение к select_file() происходит через функцию, смотрите пример ниже
    ```python
    from tkeasy import *

    title(text="Ask file")

    def showfile():
        print (select_file())

    label(text="ASK FILE",colortext="white",
        background="BLUE",row=0,column=0)

    button(text="FILE BROWSER",
        command=showfile,row=1,column=0)

    app_loop()
    ```
    ![Screenshot](/screenshots/file.jpg)

* **Виджет - браузер папок**<br/>
    select_folder()<br/>
    Данный виджет используется для вызова браузера папок, который позволяет пользователю указать на папку(фолдер).<br/>
    > command=select_folder<br/>
    > Use button method and in the command point out select_folder
    ```python
    from tkeasy import *

    title(text="Ask Folder")
    config(size="50x60")

    def askfolder():
        print(select_folder())

    label(text="ASK FOLDER",colortext="white",
        background="green",row=0,column=0)

    button(text='CHOOSE FOLDER',command=askfolder,
        row=1,column=0)

    app_loop()
    ```
    ![Screenshot](/screenshots/folder.png)

* **Диалог - сохранить файл**<br/>
    save_file()<br/>
    Пользователь может сохранить информацию с документа, для этого нам нужно узнать название файла, куда он хочет сохранить. Лучше использовать для верхнего меню. Смотрите пример wordpad.py где показано как использовать эту функцию. 
    ```python
    from tkeasy import *

    print(save_file()) 
    app_loop()   
    ```

* **Однострочный ввод**<br/>
    entry(window,name,row,column,sticky,padx,pady)<br/>
    Виджет - однострочное поле ввода. Используется для ввода информации. 
    > window (*необязательно*) = "имя". window используется для отрытия новых окн. Если у вас нет таковых, то не указываете window".<br/>
    > name = "имя" по которому get_info() найдет значение, чтобы забрать информацию с этого виджета<br/>
    > row = номер ряда расположения виджета в сетке<br/>
    > column = номер колонки расположения виджета в сетке<br/>
    > sticky (*необязательно*) = приклеивание кнопки внутри ячейки сетки. Укажите "left" или "right" или "center"<br/> 
    > padx (*необязательно*) = отступ от виджета, добавляет пространство по горизонтале.<br/>
    > pady (*необязательно*) = отступ от виджета, добавляет пространство по вертикале   
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

* **Мультистрочный ввод**<br/>
    text_area(name,row,column,sticky,padx,pady)<br/>
    Виджет, который ожидает ввод больше чем в одну строку. 
    > window (*необязательно*) = "имя". window используется для отрытия новых окн. Если у вас нет таковых, то не указываете window".<br/>
    > name = "имя" по которому get_info() найдет значение, чтобы забрать информацию с этого виджета<br/>
    > width = ширина текстового поля<br/>
    > heigth = высота текстового поля<br/>
    > row = номер ряда расположения виджета в сетке<br/>
    > column = номер колонки расположения виджета в сетке<br/>
    > sticky (*необязательно*) = приклеивание кнопки внутри ячейки сетки. Укажите "left" или "right" или "center"<br/> 
    > padx (*необязательно*) = отступ от виджета, добавляет пространство по горизонтале.<br/>
    > pady (*необязательно*) = отступ от виджета, добавляет пространство по вертикале 
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
    > text_area_scroll(name,row,column,sticky,padx,pady)<br/>
    Текстовое поле со скролом. К сожалению, на некоторых системах скрол работает медленно и ужасно.

* **Вставка текста в однострочное поле**<br />
    Можно заранее вставить текст в однострочное поле ввода. Окрасив текст в серый цвет, можно использовать это как подсказку для пользователя.
    insert_text(name,text,color)<br />
    > name = введите имя, которое вы уже использовали при создании виджета entry. Так обертка будет точно знать в какое поле вставлять<br/>
    > text = текст, который вы хотите добавить<br/>
    > color(необязательно) = "#323648" цвет текста в HEX или просто используйте его название, например, color = "gray". Если color не указать, то черный по умолчанию.
    ```python 
    from tkeasy import *

    entry(name="firstname",row=0,column=0)
    insert_text(name="firstname",text="First name",color = "gray")

    entry(name="secondname",row=1,column=0)
    insert_text(name="secondname",text="Second name",color = "gray")

    app_loop()
    ```
    ![Screenshot](/screenshots/insert.png)

* **Многострочный вывод**<br/>
    Вы можете вставить текст в многострочное окно. Cначала надо создать текстовое поле со скролом method text_area_scroll() затем вставить текст при помощи method insert_text_area()<br/>
    В некоторых операционных системах скролл работает медленно<br/>
    ```python 
    text_area_scroll(name="area output",row=0,column=0)
    insert_text_area(name="area output",text="some text",color = "black")
    ```

* **Выделенный текст**<br />
    Можно получить участок выделенного текста при помощи text_area_select() В многострочном вводе пользователь может выделить текст, виджет может увидеть какой именно участок выделен. Смотрите пример в wordpad.py<br />

* **Очистка текста в многострочном выводе**<br />
    Используется для создания нового документа. Смотрите пример в wordpad.py<br />
    text_area_clear()<br />

* **Очистка от текста в однострочном окне**<br />
    ```python
    clear_area(name="")
    ```
    name укажите имя поля, которое хотите отчистить

* **Копирование в буфер обмена**<br />
    Выделенный текст можно скопировать в буфер обмена. Смотрите пример в wordpad.py<br />
    clipboard_in(selected)<br />
    ```python
    selected = text_area_select(name) #Получение текста с выделенного участка
    clipboard_in(selected) #Копирование его в буфер обмена
    ```

* **Удаление выделенного текста**<br />
    Смотрите пример в wordpad.py<br />
    ```python
    delete_selected("name of text_area")
    ```

* **Вставка текста из буфера обмена**<br />
    Смотрите пример в wordpad.py<br />
    ```python
    paste_text("name of text_area")
    ```
* **Фреймы** <br/>
    Фреймы позволяют расположить виджеты в любом порядке, вы можете их даже наслаивать друг на друга.<br/>
    Например, в калькуляторе длинный горизонтальный виджет (экран) располагается над несколькими маленькими короткими(кнопками).<br/>
    ![Screenshot](/screenshots/calc.png)<br/>
    На макоси действует другая система измерения, поэтому фреймы поедут. На макоси нужно будет переверстать приложение указав другие размеры фреймов.<br/>
    Параметры для фрейма передаются через словарь.<br/>
    ```python
    the_first_frame = {"name_of_frame":"first_frame","x":27,"y":10,
                   "border_thickness":1,"border_color":"black",
                   "background":"#7cc5ba","padx":5,"pady":5}
    ```
    В начале каждого виджета указываете имя словаря. Можно не указывать все параметры. Достаточно имя фрейма и его размеры.
    ```python
    button(frame=the_first_frame,text=" AC ",command=AC,colortext="black",background="#edce54",row=0,column=0)
    ```
    Все виджеты, что должны войти во фрейм, должны в начале содержать его имя в виде словаря<br/>
    > name_of_frame - словарь открывается с имени фрейма. Это единственный обязательный параметр. Все остальное необязательно к указанию.<br/>
    Укажите расположение фрейма. Начало фрейма идёт от левого верхнего угла. <br/>
    > x(*необязателен*) - сдвиг по горизонтале. 0 по умолчанию <br/>
    > y(*необязателен*) - сдвиг по вертикале. 0 по умолчанию.<br/>
    > border_thickness(*необязателен*) - толщина рамки фрейма. None по умолчанию.<br/>
    > border_color(*необязателен*) - цвет рамки фрейма. None по умолчанию.<br/>
    > background(*необязателен*) - цвет фона фрейма. None по умолчанию.<br/>
    > padx(*необязателен*) - отступ от виджетов по горизонтале. 1 по умолчанию<br/>
    > pady(*необязателен*) - отступ от виджетов по вертикале. 1 по умолчанию<br/>

* **Многооконный режим** <br/>
    Вы можете создавать неограниченное количество окн<br/>
    Для первого окна нет необходимости использовать параметр "window". Иначе будет создано лишнее пустое окно по умолчанию. Параметр "window" используется только для новых окн. Для нового окна в начале каждого виджета пропишите параметр "window". Однако, чтобы избежать потерю состояния окна после закрытия его пользователем, необходимо использовать random.random(), как показано в примере ниже. Иначе, после закрытия окна, пользователь не сможет его открыть заново по кнопке, если у вас предусмотрен такой функционал, как показано в примере ниже.
    Смотрите пример в example_muilti_window_frames.py Для правильной работы второго окна необходимо указывать фрейм во втором окне.  
    ```python
    from tkeasy import *
    import random

    def show_info():
            #Пока приходиться использовать random для повторного открытия окн.
            win=str(random.random())
            frame_one = {"name_of_frame":str(random.random())}
            
            title(window=win,text="The second window")
            label(window=win,frame=frame_one,text="The second window",row=0,column=0)
            entry(window=win,frame=frame_one,name="entry2",row=1,column=0)
            insert_text(window=win,name="entry2",text="entry",color="gray")
            text_area(window=win,frame=frame_one,name="textarea",row=2,column=0)
            insert_text_area(window=win,name="textarea",text="text area",color="gray")
                
    button(text="Show Info",command=show_info,row=0,column=0)
    app_loop()
    ```
    ![Screenshot](/screenshots/w.png)

* **Линкованный текст**<br/>
    Вы можете сделать текст кликабельным. <br/>
    label_click()
    ```python
    label(text="Link 1",row=0,column=0)
    label_click().bind("<Button-1>",lambda url:msg_box("Clicked","Link 1"))

    label(text="Link 2",row=1,column=0)
    label_click().bind("<Button-1>",lambda url:msg_box("Clicked","Link 2"))
    ```
    ![Screenshot](/screenshots/labelclick.png)

* **Изображения**<br />
    Так как обертка опирается только на встроенные либы, то поддерживаются только два формата: gif, png. Лучше использовать png для хорошего качества, альфа-каналы поддерживаются, можно использовать прозрачные png
    Также второе ограничение, изображения не открываются во втором или третьем окне, это связано из-за недоделки стандартной библиотеки tkinter. Нельзя использовать анимированные gif и png, будет показываться только последний кадр.<br />
    > photo(window,file,row,column)
    ```python
    photo("1.png",0,0)
    photo("2.png",1,0)
    ```
    ![Screenshot](/screenshots/photo.png)
    
* **Кликабельные изображения**<br/>
    Изображения можно сделать кликабельными<br />
    > photo_click()
    ```python
    photo(file="1.png",row=0,column=0)
    photo_click().bind("<Button-1>",lambda url:
                    msg_box(title="Clicked",message="Picture 1"))
    ```
* **Виджет - ползунки**<br />
    Горизонтальное расположение ползунков (слайдеров) сделаны по умолчанию. <br />
    slider(window,name,pos,row,column,sticky,padx,pady)<br />
    > window (*необязательно*) = "имя". window используется для отрытия новых окн. Если у вас нет таковых, то не указываете window".<br/>
    > name = "имя" по которому get_info() найдет значение, чтобы забрать информацию с этого виджета<br/>
    > pos = поставьте "vertical" если хотите сделать ползунки вертикальными<br/>
    > row = номер ряда расположения виджета в сетке<br/>
    > column = номер колонки расположения виджета в сетке<br/>
    > sticky (*необязательно*) = приклеивание кнопки внутри ячейки сетки. Укажите "left" или "right" или "center"<br/> 
    > padx (*необязательно*) = отступ от виджета, добавляет пространство по горизонтале.<br/>
    > pady (*необязательно*) = отступ от виджета, добавляет пространство по вертикале     
    ![Screenshot](/screenshots/sliders.png)

* **Вверхнее меню**<br/>
    Смотрите пример в example_topmenu.py<br />
    Меню строится на вложенном словаре. Первое значение, то что будет в названии таба, далее вложенный словарь, где ключ - это название под табом, а его значение ссылка на функцию. В данный момент указанно "False", что означает пропустить. <br />
    ```json
    tabs = {"File":{"New":"False","Open":"False","Save":"False","Save as":"False","Close":"False","---":"---","Exit":quit},
    "Edit":{"Undo":"False","---":"---","Cut":"False","Copy":"False","Paste":"False","Delete":"False","Select All":"False"},
    "Help":{"Help Index":"False","About...":"False","Help":"False"}}
    ```
    ![Screenshot](/screenshots/topmenu.jpg)

    На макоси меню располагается в тулбаре. Будьте внимательны!<br />
    ![Screenshot](/screenshots/menubar_mac.jpg)

* **Пипетка для выбора цвета**<br />
    Вызывает диалог выбора цвета и позволяет получить значение выбранного цвета.<br />
    ```python
    from tkeasy import *

    def color():
        color = colorpicker()
        print(color)

    button(text="Choose color", command=color,
            row=0,column=0,padx=5,pady=5)

    app_loop()
    ```
    ![Screenshot](/screenshots/colorpicker.png)

* **hotkeys**<br/>
    Горячие клавиши, указываете горячую клавишу и ссылку на функцию.
    ```python
    hotkey("<Return>",command)
    ```
    
    Для второго окна, нужно указать название окна, и фрейм.
    ```python
    hotkey(window="win",frame="frame_one",key="<Return>",command=command)
    ```

    Этот код выводит любое нажатие клавиши в поле entry
    ```python
    from tkeasy import *

    def keydown(event):
        print ('Key was pressed = ', event.char)

    entry(name="ent",row=0,column=0)
    hotkey("<KeyPress>",command=keydown)

    app_loop()
    ```

    Некоторые популярные ивенты:<br />
    ```
    "<Button-1>" левое нажатие клавиши

    "<B1-Motion>" удерживание левой клавиши мыши. B2 колесо мыши и B3 правая клавиша мыши. 

    "<ButtonRelease-1>" Если левая клавиша мыши была отпущена

    "<Double-Button-1>" Двойное нажатие левой клавиши мыши
    Triple - тройное нажатие.

    <Return> клавиша Enter.
    ```

* **Пароль - виджет**<br />  
    Вводит звездочки в поле для пароля<br/>
    > focus - Установите фокус, чтобы виджет понимал в каком поле данный момент вводится пароль<br/>
    > entry_name - Укажите имя поля ввода куда виджет будет вставлять звездочки<br/>
    > password_name. - Используйте две переменных для пароля "password" or "confirm password"
    ![Screenshot](/screenshots/password_asterisks.png)<br/>
   Полный код смотрите в example_password.py

* **Стереть пароль**<br />   
    ```python
    clear_password()
    ```  
    Стирает пароль из памяти

* **Стереть подтвержденный пароль**<br />  
    ```python
    clear_confirm_password()
    ```
    Стирает подтвержденный пароль из памяти. 

* **Получить пароль**<br /> 
    Получить пароль из памяти <br /> 
    ```python
    password = get_info("password")
    ```

* **Получить подтвержденный пароль**<br /> 
    Получить подтвержденный пароль из памяти<br /> 
    ```python
    confirm password = get_info("confirm password")
    ```
    
* **Завершение**<br/>
    Выход, закрытие приложения. Часто используется для вверхнего меню <br/>
    > quit
    ```python
    button(text='Quit',command=quit,
        row=0,column=0,sticky="center")
    ```
* **app_loop()**<br/>
    В конце программы всегда добавляйте app_loop() Если запускаете из консоли, то без app_loop() она закроется сразу после запуска.