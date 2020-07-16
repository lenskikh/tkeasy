import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import tkinter.messagebox

root = tk.Tk()
memory = {"filename":"", "key TAB":""}
radioBox = tk.StringVar()

def title_size(**kwargs):
    title = kwargs["title"]
    root.title(title)

    size = ""
    try:
        size = kwargs["size"]
        root.geometry(size)
    except KeyError:
        pass        

#clear entry if text inside field used as prompting
#when you click in entry field, a text inside text will be cleared
def clearbyclick(event):    
    try: #if user click outside field we'll get error message
        memoryForClear = str(root.focus_get())
        if memoryForClear in memory["key TAB"]:
            pass #entry field was cleared
        elif "TAB" in memory["key TAB"]:
            pass
        else:
            root.focus_get().delete(0, tk.END)
            memory["key TAB"]+= memoryForClear
    except:
        pass

#if press TAB key a text inside entry will be cleared
def key(event):
    char = str(event.char)
    if char == '\t':
        memory["key TAB"]+="TAB"

#new window
def new_window(identifier):
    memory[identifier] = tk.Toplevel(root)
    
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
    
def selectfile():
    memory["filename"] = filedialog.askopenfilename(initialdir = os.getcwd()+"./",
                                            title = "Select file")

def selectfolder():
    memory["filename"] = filedialog.askdirectory(initialdir = os.getcwd()+"./",
                                            title = "Select folder")   

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

def buttons(**kwargs):   
    tk.Button(root, 
        text = kwargs["text"],
        command = kwargs["command"]).grid(
        row = kwargs["row"],
        column = kwargs["column"],
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))
   
def labels(**kwargs):   
    tk.Label(root, 
        text = kwargs["text"],
        fg = colortext(**kwargs),
        bg = background(**kwargs)).grid(
        row = kwargs["row"],
        column = kwargs["column"],
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))
  
def entryfield(identifier,**kwargs):
    memory[identifier] = tk.Entry(root)
    memory[identifier].grid(
        row = kwargs["row"],
        column = kwargs["column"],
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))
    
def entryinsert(identifier,text,colortext):
    memory[identifier].insert(0,text)
    memory[identifier].config(fg=colortext)

def checkbox(identifier,text,**kwargs):
    memory[identifier] = tk.IntVar()
    memory[text] = tk.Checkbutton(root,
        text = text,
        variable = memory[identifier])
    memory[text].grid(
        row = kwargs["row"],
        column = kwargs["column"],
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def radiobox(**kwargs):
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

    radioBox.set(memory["default"])    
    radiob = tk.Radiobutton(root, 
        text = kwargs["text"], 
        variable = radioBox, 
        value = value)
    radiob.grid(
        row = kwargs["row"],
        column = kwargs["column"],
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))    

def dropdownlist(variable,choices,default,**kwargs):
    memory[variable] = tk.StringVar(root)
    popupmenu = tk.OptionMenu(root, memory[variable], *choices)
    memory[variable].set(default) # default value
    popupmenu.grid(
        row = kwargs["row"],
        column = kwargs["column"],
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))    

def textarea(identifier,**kwargs):
    memory[identifier] = tk.Text(root,
        wrap = tk.WORD,
        height = 10, 
        width = 30,
        background = "grey95")
    memory[identifier].grid(
        row = kwargs["row"],
        column = kwargs["column"],
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def textareascroll(identifier,**kwargs):
    memory[identifier] = scrolledtext.ScrolledText(root,
        wrap = tk.WORD,
        height = 10, 
        width = 30,
        background = "grey95")
    memory[identifier].grid(
        row = kwargs["row"],
        column = kwargs["column"],
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def instertextarea(identifier,text,color):    
    memory[identifier].insert(1.0,text)
    memory[identifier].config(fg=color)

def msgbox(title,message): 
    msgbox = tk.messagebox.showinfo(title=title, message=message)

def msgboxwarning(title,message): 
    msgbox = tk.messagebox.showwarning(title=title, message=message)

def msgboxask(identifier,title,message): 
    memory[identifier] = tk.messagebox.askyesnocancel(title=title, message=message)
