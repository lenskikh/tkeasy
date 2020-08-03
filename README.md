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
title(window="first window",text="The first window")
label(window="first window",text="The first window",row=0,column=0)
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

radiobox(window="main",text="Apple",row=0,column=0)
radiobox(window="main",text="Melon",row=1,column=0,value="weight = 2kg")
radiobox(window="main",text="Lemon",row=2,column=0)
button(window="main",text="Show Info",command=show_info,row=3,column=0)
```
![Screenshot](/screenshots/radiobox.png)