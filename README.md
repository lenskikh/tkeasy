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
##What's new in this version?

1. Each widget supports all default widget options of TKinter. You take any parameter from the Tkinter documentation and just use it.
2. Creating a second window or frame is now easier, more logical and clearer. You will be able to open a second window after closing without any problem.
3. Some options are already used by default. If your row or column is zero, then you can leave it. If your program is small, consists of two widgets, for example, a temperature converter, then this approach reduces the code. Or you use one vertical column equal to zero, then you can only specify a row. Other values such as pady are None. 

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