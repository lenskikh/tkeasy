# tkeasy
## Wrapper for tkinter giving an easier way to build a gui interface. GUI Development does not have to be difficult nor painful.</br>
Author - Mikhail Lenskikh</br>
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

* title
    > method title()<br/>
    > text = "New Title"<br/>
    > window (*optional*) = "name"<br/>
    ```python
    title(text="Title")
    ``` 
* geometry
    > method geometry()<br/>
    > size = "300x300"<br/>
    > window (*optional*) = "name"<br/>
    ```python
    geometry(size="300x300")
    or
    geometry('200x150 + 400 + 300') 
    ```
    > 400 shifted on X-axis and 300 shifted on Y-axis
* button
    > method button()<br/>
    > window (*optional*) = "name"<br/>
    > text="text" - text of button<br/>
    > command=somedef - appeal to function in your code (*Without brackets and quotation marks. See examples in code*)<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/>
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*)
    ```python
    button(text="Show Info",command=show_info,row=0,column=0)
    ```
* label
    > method label()<br/>
    > window (*optional*) = "name"<br/>
    > text="text" - text of label<br/>
    > colortext (*optional*) = "red" (You can use hex color instead)<br/>
    > background (*optional*) = "#241e14" (You can use hex color)<br/>
    > font (*optional*) = "Times", 13 (font in quotation marks, size of font after comma)<br/>
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*)    
    ```python
    label(text="Label text",row=0,column=0)
    ```
* checkboxes
    > method checkbox()<br/>
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
* radiobox
    > method radiobox()<br/>
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
* dropdown list
    > method dropdown_list()<br/>
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
* file browse
    > method select_file<br/>
    > command=select_file<br/>
    > Use button method and in the command point out select_file
    ```python
    button(text="FILE BROWSER", command=select_file,row=0,column=0)
    ```
* folder browse
    > method select_folder<br/>
    > command=select_folder
    > Use button method and in the command point out select_folder
    ```python
    button(text='FOLDER BROWSER',command=select_folder,row=0,column=0,sticky="center")
    ```
* one-line text input
    > method entry()<br/>
    > window (*optional*) = "name"<br/>
    > name = "name" - name of entry<br/>   
    > row = 0 (*Number. Without brackets and quotation marks*)<br/>
    > column = 0 (*Number. Without brackets and quotation marks*)<br/>
    > sticky (*optional*) = "left" or "right" or "center" Сhoose one<br/> 
    > padx (*optional*) = 5 (*Number. Without brackets and quotation marks*)<br/>
    > pady (*optional*) = 5 (*Number. Without brackets and quotation marks*) 
    ```python   
    entry(name="entry 1",row=0,column=0)
    ```  
* multi-line text input
* insert text in input field
* scroll-able output
* multiple windows - unlimited number of windows can be open at the same time
* clickable text
* images
* clickable images
* scale/slider (horizontal by default) 
* return values (get_info)