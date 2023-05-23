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

## What's new in this version?

1. Each widget supports all default widget options of TKinter. You take any parameter from the Tkinter documentation and just use it.
2. Creating a second window or frame is now easier, more logical and clearer. You will be able to open a second window after closing without any problem.
3. Some options are already used by default. If your row or column is zero, then you can leave it. If your program is small, consists of two widgets, for example, a temperature converter, then this approach reduces the code. Or you use one vertical column equal to zero, then you can only specify a row. Other values such as pady are None. 
<br />
Since the standard library is used, there are no issues with creating an exe

## Your fisrt GUI program
```python
from tkeasy import TKeasy
gui = TKeasy()

gui.Title("The first window")
gui.config(size="300x100", bg = "white")
gui.label(text="The first window", bg = "white")
gui.loop()
```
![Screenshot](/screenshots/thefirst.png)

## How to get information from a widget? 

**Use get_info(name)**<br />

If you use several widgets such as entry, for understand which one to take information from, you need to give a name in each widget inside the brackets. See an example below.

```python
from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Input")

def info():
    gui.msg_box_warning("INFO", gui.get_info("ent1"))

gui.entry(name="ent1",width=20, padx = 5, pady =5)
gui.button(text="Button",command=info,row=1)

gui.loop()
```

## Window Configuration

config(size="1x2+3+4") <br />
1 - width<br />
2 - hight <br />
3 - position by X<br />
4 - postion by  Y<br />
config(size="widthxhight+posX+posY") <br /><br />

Color of background, you can use hex colors<br />
config(bg="lightgreen")<br /><br />

Icon of a window<br />
config(icon="icon.ico")<br /><br />

Border of a window<br />
config(border = "False")

```python
from tkeasy import TKeasy

gui = TKeasy()

gui.Title("ICON")
gui.config(size="50x150+400+100")
gui.config(bg="lightgreen")
gui.config(icon="icon.ico")
gui.config(border = "False")

gui.loop()
```
