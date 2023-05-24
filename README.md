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

Border of a window. If you don't specify "False", it will default to the standard window border width.<br />
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

## The second window
```python
from tkeasy import TKeasy

gui = TKeasy()

gui.Title("The first window")
gui.config(size="300x300")

gui2 = TKeasy()

gui2.Title("The second window")
gui2.config(size="300x300+300+400")

#packing the first window
gui.loop()
#packing the second window
gui2.loop()
```

## The second frame

What are frames for? Frame allows you to pack widgets at specific coordinates. A frame has own grid. The most striking example is a calculator. In the first frame, you show the screen where the numbers are displayed. In the second frame you have buttons with numbers. <br />

![Screenshot](/screenshots/calc.png)<br />

**How to work with frames?**<br />

First you specify the first frame, prescribe its parameters. Then you enumerate the widgets. At the end, open the second frame and list new widgets there. See example below. <br />
```python
from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Frames")
gui.config(size="205x250",bg="white")

gui.frames (frame = "frame 1", x= 21, y = 10,
            highlightthickness = 1,
            highlightbackground = "black",
            padx = 5,
            pady = 5)

gui.label(text="the first frame", bg = "#f5dc4b")

gui.frames (frame = "frame 2", x= 21, y = 50,
            highlightthickness = 1,
            highlightbackground = "black",
            background = "#cadb66",
            padx = 5,
            pady = 5)

gui.label(text="the second frame", bg = "white")

gui.loop()
```

## Top menu

The top menu is a dictionary - tabs{} <br />
See the image below to see how it works.<br />
![Screenshot](/screenshots/topmenu.jpg)<br />

Remember that on the Mac operation system, the menu is not located in the window itself. The topmenu will be on top of your screen.<br />
![Screenshot](/screenshots/menubar_mac.jpg)<br />