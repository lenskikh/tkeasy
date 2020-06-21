import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext 

root = tk.Tk()
memory = {"filename":"", "checkbox 1":0, "convert to lower case":0,"multi":""}
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

def dialog():
    memory["filename"] = filedialog.askopenfilename(initialdir = os.getcwd()+"./",
                                            title = "Select file") 
    file = memory["filename"].split("/")[-1]

def buttons(text,command,row,column):
    tk.Button(root, text=text,command=command).grid(
        row=row,column=column,sticky=tk.W,padx=10,pady=10)

def labels(text,colortext,font,background,row,column):
    if font == "":
        font = "14"
    if colortext == "":
        colortext = "black"
    if background == "":
        background = "white"
    tk.Label(root, text=text,fg=colortext,font=font,bg=background).grid(
        row=row,column=column,sticky=tk.E,padx=10,pady=10)

def entryfield(num,row,column):
    memory[num] = tk.Entry(root)
    memory[num].grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)

def entryinsert(num,text,color):
    #memory["variable_entry"] = text
    #memory[num].insert(0,memory["variable_entry"])
    memory[num].insert(0,text)
    memory[num].config(fg=color)        

def checkbox(num,text,row,column):
    memory[num] = tk.IntVar()
    memory[text] = tk.Checkbutton(root,text=text,variable=memory[num])
    memory[text].grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)

def radiobox(text,value,row,column):
    radiob = tk.Radiobutton(root, text=text, variable=radioBox,command=selection, value=value)
    radiob.grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)

def popup(choices,variable,default,row,column):
    memory[variable] = tk.StringVar(root)
    popupmenu = tk.OptionMenu(root, memory[variable], command=selection, *choices)
    memory[variable].set(default) # default value
    popupmenu.grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)
'''
def textarea(num,row,column):
    memory[num] = tk.Text(root,height=10, width=30,background="grey95")
    memory[num].grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)
'''
def textarea(num,row,column):
    memory[num] = scrolledtext.ScrolledText(root,wrap = tk.WORD,height=10, width=30,background="grey95")
    memory[num].grid(row=row,column=column,sticky=tk.W,padx=10,pady=10)

def instertextarea(num,text,color):    
    memory[num].insert(1.0,text)
    memory[num].config(fg=color)
