import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext 

root = tk.Tk()
memory = {"filename":"", "event":0,"checkbox 1":0,"multi":"","focus":""}
radioBox = tk.StringVar()
radioBox.set(1)

def title(title):
    root.title(title)
    
#clear entry if text inside field used as prompting
def clear(event):    
    try: #if user click outside field we'll get error message
        memoryForClear = str(root.focus_get())
        if memoryForClear in memory["focus"]:
            pass #entry field was cleared
        elif "TAB" in memory["focus"]:
            pass
        else:
            root.focus_get().delete(0, tk.END)
            memory["focus"]+=memoryForClear
    except:
        pass
    
def key(event):
    char = str(event.char)
    if char == '\t':
        memory["focus"]+="TAB"
    
def alignment(sticky):
    if sticky == "right":
        sticky = tk.E
    elif sticky == "left":
        sticky = tk.W
    elif sticky == "center":
        sticky = tk.EW
    return sticky
    
def dialog():
    memory["filename"] = filedialog.askopenfilename(initialdir = os.getcwd()+"./",
                                            title = "Select file") 
    file = memory["filename"].split("/")[-1]

def buttons(text,command,row,column,sticky):
    sticky = alignment(sticky) 
    tk.Button(root, text=text,command=command).grid(
        row=row,column=column,sticky=sticky,padx=2,pady=2)

def labels(text,colortext,font,background,row,column,sticky):
    if font == "":
        font = "14"
    if colortext == "":
        colortext = "black"
    if background == "":
        background = "white"
    sticky = alignment(sticky)      
    tk.Label(root, text=text,fg=colortext,font=font,bg=background).grid(
        row=row,column=column,sticky=sticky,padx=2,pady=2)

def entryfield(identifier,row,column):
    memory[identifier] = tk.Entry(root)
    memory[identifier].grid(row=row,column=column,sticky=tk.W,padx=2,pady=2)
    
def entryinsert(identifier,text,color):
    memory[identifier].insert(0,text)
    memory[identifier].config(fg=color)

def checkbox(identifier,text,row,column):
    memory[identifier] = tk.IntVar()
    memory[text] = tk.Checkbutton(root,text=text,variable=memory[identifier])
    memory[text].grid(row=row,column=column,sticky=tk.W,padx=2,pady=2)

def radiobox(text,value,row,column):
    radiob = tk.Radiobutton(root, text=text, variable=radioBox, value=value)
    radiob.grid(row=row,column=column,sticky=tk.W,padx=2,pady=2)

def dropdownlist(choices,variable,default,row,column):
    memory[variable] = tk.StringVar(root)
    popupmenu = tk.OptionMenu(root, memory[variable], *choices)
    memory[variable].set(default) # default value
    popupmenu.grid(row=row,column=column,sticky=tk.W,padx=2,pady=2)

def textarea(identifier,row,column):
    memory[identifier] = tk.Text(root,height=10, width=30,background="grey95")
    memory[identifier].grid(row=row,column=column,sticky=tk.W,padx=2,pady=2)

def textareascroll(identifier,row,column):
    memory[identifier] = scrolledtext.ScrolledText(root,wrap = tk.WORD,height=10, width=30,background="grey95")
    memory[identifier].grid(row=row,column=column,sticky=tk.W,padx=2,pady=2)

def instertextarea(identifier,text,color):    
    memory[identifier].insert(1.0,text)
    memory[identifier].config(fg=color)
