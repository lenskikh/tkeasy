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
from tkeasy import TKeasy
gui = TKeasy()

gui.Title("The first window")
gui.config(size="300x100", bg = "white")
gui.label(text="The first window", bg = "white")
gui.loop()
```
![Screenshot](/screenshots/thefirst.png)