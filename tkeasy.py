import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext 

root = tk.Tk()
memory = {"filename":"", "event":0,"checkbox 1":0,"multi":"","focus":""}
radioBox = tk.IntVar()
radioBox.set(1)

def title(title):
    root.title(title)
    
def show_entry_fields():
    print("Find entry = " + memory["find entry"].get())
    print("Replace entry = " + memory["replace entry"].get())
    print("Checkbox = %s" % memory["checkbox"].get())
    print("Radiobox = %s" % radioBox.get())
    memory["find entry"].delete(0, tk.END)
    memory["replace entry"].delete(0, tk.END)

def selection(*args):
    print("Radiobox = %s" % radioBox.get())
    print("Dropdown menu = %s" % memory["variable"].get())
    print("Dropdown menu = %s" % memory["variable2"].get())

#clear entry if text inside field used as prompting
def clear(event):
    memoryForClear = str(root.focus_get())
    if memoryForClear in memory["focus"]:
        pass #entry field was cleared
    else:
        root.focus_get().delete(0, tk.END)
        memory["focus"]+=memoryForClear   

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
        row=row,column=column,sticky=sticky,padx=10,pady=10)

def labels(text,colortext,font,background,row,column,sticky):
    if font == "":
        font = "14"
    if colortext == "":
        colortext = "black"
    if background == "":
        background = "white"
    sticky = alignment(sticky)      
    tk.Label(root, text=text,fg=colortext,font=font,bg=background).grid(
        row=row,column=column,sticky=sticky,padx=10,pady=10)

def entryfield(identifier,row,column):
    memory[identifier] = tk.Entry(root)
    memory[identifier].grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)
    
def entryinsert(identifier,text,color):
    #memory["variable_entry"] = text
    #memory[identifier].insert(0,memory["variable_entry"])
    memory[identifier].insert(0,text)
    memory[identifier].config(fg=color)        

def checkbox(identifier,text,row,column):
    memory[identifier] = tk.IntVar()
    memory[text] = tk.Checkbutton(root,text=text,variable=memory[identifier])
    memory[text].grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)

def radiobox(text,value,row,column):
    radiob = tk.Radiobutton(root, text=text, variable=radioBox,command=selection, value=value)
    radiob.grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)

def popup(choices,variable,default,row,column):
    memory[variable] = tk.StringVar(root)
    popupmenu = tk.OptionMenu(root, memory[variable], command=selection, *choices)
    memory[variable].set(default) # default value
    popupmenu.grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)

def textarea(identifier,row,column):
    memory[identifier] = tk.Text(root,height=10, width=30,background="grey95")
    memory[identifier].grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)

def textareascroll(identifier,row,column):
    memory[identifier] = scrolledtext.ScrolledText(root,wrap = tk.WORD,height=10, width=30,background="grey95")
    memory[identifier].grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)

def instertextarea(identifier,text,color):    
    memory[identifier].insert(1.0,text)
    memory[identifier].config(fg=color)
