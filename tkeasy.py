import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import Listbox
import tkinter.messagebox

memory = {"filename":"", "key TAB":""}

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
def new_window(**kwargs):
    try:
        window = kwargs["window"]
    except:
        window = "root"        
    if window not in memory:
        memory[window] = tk.Tk()
    return window        

def title(text,**kwargs):
    window = new_window(**kwargs)
    memory[window].title(text)

def geometry(size,**kwargs):
    window = new_window(**kwargs)
    memory[window].geometry(size)    

def get_info(name):
    try:
        #text area 
        return memory[name].get("1.0", 'end')
    except:
        #ask file or folder
        if name == "file" or name == "folder":
            return memory[name]
        else:
            #entry,checkbox,radiobox
            return memory[name].get()

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

#wrap for label
def label_length(**kwargs):
    try:
        wrap = kwargs["wrap"]
    except KeyError:
        wrap = 600
    return wrap    

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

def width_entry(**kwargs):
    try:
        width = kwargs["width"]
    except:
        width = 20
    return width

def label_font(**kwargs):
    try:
        font = kwargs["font"]
    except:
        font = "Helvetica", 13
    return font

def scale_oriental(**kwargs):
    try:
        kwargs["pos"]
        orient = "vertical"
    except:
        orient = "horizontal"
    return orient


def select_file():
    memory["file"] = filedialog.askopenfilename(initialdir = os.getcwd()+"./",
                                            title = "Select file")

def select_folder():
    memory["folder"] = filedialog.askdirectory(initialdir = os.getcwd()+"./",
                                            title = "Select folder")   

def separator(column_length,**kwargs):
    window = new_window(**kwargs) 
    separator = tk.Frame(memory[window],height=2, bd=1, relief="sunken")
    separator.grid(columnspan=column_length, sticky="EW",
        padx=padx(**kwargs), pady=pady(**kwargs))

def button(text,command,row,column,**kwargs):  
    window = new_window(**kwargs) 
    tk.Button(memory[window], 
        text = text,
        command = command).grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def label(text,row,column,**kwargs):   
    window = new_window(**kwargs)
    memory["label"] = tk.Label(memory[window], 
        text = text,
        fg = colortext(**kwargs),
        bg = background(**kwargs),
        font = label_font(**kwargs),
        wrap = label_length(**kwargs))
    memory["label"].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))  

def label_click():
    return memory["label"]

def photo(file,row,column,**kwargs):
    window = new_window(**kwargs) 
    photo = tk.PhotoImage(file=file)
    memory["picture"] = tk.Label(memory[window],image=photo)
    memory["picture"].photo = photo
    memory["picture"].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def photo_click():
    return memory["picture"]

def entry(name,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = tk.Entry(memory[window],
        width = width_entry(**kwargs))
    memory[name].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def checkbox(name,text,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = tk.IntVar()
    memory[text] = tk.Checkbutton(memory[window],
        text = text,
        variable = memory[name])
    memory[text].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def slider(name,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = tk.Scale(memory[window],
        from_= 0, to = 100, orient=scale_oriental(**kwargs))
    memory[name].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))        

def radiobox(text,row,column,**kwargs):
    window = new_window(**kwargs)
    if "radiobox" not in memory:
        memory["radiobox"] = tk.StringVar()

    #No radio boxes are selected
    memory["radiobox"].set(None)

    if kwargs.get("value"):
        value = kwargs["value"] 
    else:
        #if value not provided, use text as value
        value = text

    radiob = tk.Radiobutton(memory[window], 
        text = text, 
        variable = memory["radiobox"], 
        value = value)
    radiob.grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))    

def dropdown_list(variable,choices,default,row,column,**kwargs):
    window = new_window(**kwargs)
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
def text_area(name,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = tk.Text(memory[window],
        wrap = tk.WORD,
        height = 10, 
        width = 30,
        background = "grey95")
    memory[name].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

#Works slowly at big text (in macos)
def text_area_scroll(name,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = scrolledtext.ScrolledText(memory[window],
        wrap = tk.WORD,
        height = 10, 
        width = 30,
        background = "grey95")
    memory[name].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def listbox(name,row,column,**kwargs):
    window = new_window(**kwargs)
    try:
        height = kwargs["height"]
    except:
        height = 10

    memory[name] = Listbox(memory[window],height = height)
    memory[name].grid(
        row = row,
        column = column)   
    try: 
        text = kwargs["text"]
        listbox_insert(name,text)
    except:
        pass

def listbox_insert(name,text):
    for x in text:
        memory[name].insert("end", x)    

def listbox_item_selected(name):
    print(memory[name].get("active"))


#for change text in text area
def insert_text(name,text,color):    
    memory[name].insert(0,text)
    memory[name].config(fg=color)

def insert_text_area(name,text,color):
    memory[name].insert(1.0,text)
    memory[name].config(fg=color)

def msg_box(title,message): 
    msgbox = tk.messagebox.showinfo(title=title, message=message)

#alarm icon in message box
def msg_box_warning(title,message): 
    msgbox = tk.messagebox.showwarning(title=title, message=message)

def msg_box_ask(name,title,message): 
    memory[name] = tk.messagebox.askyesnocancel(title=title, message=message)

def app_loop(**kwargs):
    window = new_window(**kwargs)
    memory[window].mainloop()

