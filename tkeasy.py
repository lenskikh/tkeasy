import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import tkinter.messagebox

root = tk.Tk()
memory = {"filename":"", "key TAB":""}
radioBox = tk.StringVar()

def title_size(title,size):
    root.title(title)
    if size == "":
        pass
    else:
        root.geometry(size)

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
            memory["key TAB"]+=memoryForClear
    except:
        pass

#if press TAB key a text inside entry will be cleared
def key(event):
    char = str(event.char)
    if char == '\t':
        memory["key TAB"]+="TAB"

def new_window(identifier):
    memory[identifier] = tk.Toplevel(root)
    
def alignment(**kwargs):
    sticky = ""
    try:
        sticky = kwargs["sticky"]
    except KeyError:
        sticky = tk.W
        
    if sticky == "right":
        sticky = tk.E
    elif sticky == "left":
        sticky = tk.W
    elif sticky == "center":
        sticky = tk.EW
    return sticky
    
def selectfile():
    memory["filename"] = filedialog.askopenfilename(initialdir = os.getcwd()+"./",
                                            title = "Select file")

def selectfolder():
    memory["filename"] = filedialog.askdirectory(initialdir = os.getcwd()+"./",
                                            title = "Select folder")   

def buttons(**kwargs):
    sticky = alignment(**kwargs)
    text = kwargs["text"]
    command = kwargs["command"]
    row = kwargs["row"]
    column = kwargs["column"]
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
    
def entryinsert(identifier,text,colortext):
    memory[identifier].insert(0,text)
    memory[identifier].config(fg=colortext)

def checkbox(identifier,text,row,column):
    memory[identifier] = tk.IntVar()
    memory[text] = tk.Checkbutton(root,text=text,variable=memory[identifier])
    memory[text].grid(row=row,column=column,sticky=tk.W,padx=2,pady=2)

def radiobox(default,text,value,row,column):
    radioBox.set(default)    
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

def msgbox(title,message): 
    msgbox = tk.messagebox.showinfo(title=title, message=message)

def msgboxwarning(title,message): 
    msgbox = tk.messagebox.showwarning(title=title, message=message)

def msgboxask(identifier,title,message): 
    memory[identifier] = tk.messagebox.askyesnocancel(title=title, message=message)
