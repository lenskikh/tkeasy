import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import tkinter.messagebox

memory = {"filename":"", "key TAB":""}
#radioBox = tk.StringVar()

#clear entry if text inside field used as prompting
#when you click in entry field, a text inside text will be cleared
def clearbyclick(event):    
    try: #if user click outside field we'll get error message
        memoryForClear = str(memory[window].focus_get())
        if memoryForClear in memory["key TAB"]:
            pass #entry field was cleared
        elif "TAB" in memory["key TAB"]:
            pass
        else:
            memory[window].focus_get().delete(0, tk.END)
            memory["key TAB"]+= memoryForClear
    except:
        pass

#if press TAB key a text inside entry will be cleared
def key(event):
    char = str(event.char)
    if char == '\t':
        memory["key TAB"]+="TAB"

#new window
def new_window(window):
    if window not in memory:
        memory[window] = tk.Tk()

def title(window,text):
    new_window(window)
    memory[window].title(text)

def geometry(window,size):
    new_window(window)
    memory[window].geometry(size)    

def alignment(**kwargs):
    try:
        sticky = kwargs["sticky"]
        if sticky == "right":
            sticky = tk.E
        elif sticky == "left":
            sticky = tk.W
        elif sticky == "center":
            sticky = tk.EW        
    except KeyError:
        sticky = tk.EW       

    return sticky

#for label                                            
def colortext(**kwargs):
    try:
        colortext = kwargs["colortext"]
    except KeyError:
        colortext = "black"
    return colortext

#for label
def background(**kwargs):
    try:
        background = kwargs["background"]
    except KeyError:
        background = "white"
    return background

def padx(**kwargs):
    try:
        padx = kwargs["padx"]
    except KeyError:
        padx = 2
    return padx

def pady(**kwargs):
    try:
        pady = kwargs["pady"]
    except KeyError:
        pady = 2
    return pady

def selectfile():
    memory["filename"] = filedialog.askopenfilename(initialdir = os.getcwd()+"./",
                                            title = "Select file")

def selectfolder():
    memory["filename"] = filedialog.askdirectory(initialdir = os.getcwd()+"./",
                                            title = "Select folder")   

def button(window,text,command,row,column,**kwargs):  
    new_window(window) 
    tk.Button(memory[window], 
        text = text,
        command = command).grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))
   
def label(window,text,row,column,**kwargs):   
    new_window(window)
    tk.Label(memory[window], 
        text = text,
        fg = colortext(**kwargs),
        bg = background(**kwargs)).grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))
  
def entryfield(window,name,row,column,**kwargs):
    new_window(window)
    memory[name] = tk.Entry(memory[window])
    memory[name].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))
    
def entryinsert(name,text,colortext):
    memory[name].insert(0,text)
    memory[name].config(fg=colortext)

def checkbox(identifier,text,**kwargs):
    new_window(window)
    memory[identifier] = tk.IntVar()
    memory[text] = tk.Checkbutton(memory[window],
        text = text,
        variable = memory[identifier])
    memory[text].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def radiobox(**kwargs):
    new_window(window)
    #it's give way not use default var in next times
    try:
        memory["default"] = kwargs["default"]
    except:
        pass

    #if value is used
    if kwargs.get("value"):
        value = kwargs["value"] 
    else:
        value = kwargs["text"]

    #set universal var for all radioboxes
    radioBox.set(memory["default"])    

    radiob = tk.Radiobutton(memory[window], 
        text = kwargs["text"], 
        variable = radioBox, 
        value = value)
    radiob.grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))    

def dropdownlist(window,variable,choices,default,row,column,**kwargs):
    new_window(window)
    memory[variable] = tk.StringVar(memory[window])
    popupmenu = tk.OptionMenu(memory[window], memory[variable], *choices)
    memory[variable].set(default) # default value
    popupmenu.grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))    

#text in text area looks ugly with scroll in macos
#you can use textarea without scroll
def textarea(identifier,**kwargs):
    new_window(window)
    memory[identifier] = tk.Text(memory[window],
        wrap = tk.WORD,
        height = 10, 
        width = 30,
        background = "grey95")
    memory[identifier].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

#Works slowly at big text (in macos)
def textareascroll(identifier,**kwargs):
    new_window(window)
    memory[identifier] = scrolledtext.ScrolledText(memory[window],
        wrap = tk.WORD,
        height = 10, 
        width = 30,
        background = "grey95")
    memory[identifier].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

#for change text in text area
def instertextarea(identifier,text,color):    
    memory[identifier].insert(1.0,text)
    memory[identifier].config(fg=color)

def msgbox(title,message): 
    msgbox = tk.messagebox.showinfo(title=title, message=message)

#alarm icon in message box
def msgboxwarning(title,message): 
    msgbox = tk.messagebox.showwarning(title=title, message=message)

def msgboxask(identifier,title,message): 
    memory[identifier] = tk.messagebox.askyesnocancel(title=title, message=message)
