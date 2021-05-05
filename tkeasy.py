import os
from tkinter import *
from tkinter import filedialog, scrolledtext, messagebox

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
            memory[window].focus_get().delete(0, END)
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
        memory[window] = Tk()
    return window        

def title(text,**kwargs):
    window = new_window(**kwargs)
    memory[window].title(text)

def config(**kwargs):
    window = new_window(**kwargs)
    try:
        size = kwargs["size"]
        memory[window].geometry(size)  
    except:
        pass

    try:
        bgcolor = kwargs["background"]
        memory[window].configure(background=bgcolor)  
    except:
        pass

    try:
        border = kwargs["border"]
        memory[window].overrideredirect(1)
    except:
        pass

    try:
        icon = kwargs["icon"]
        memory[window].iconbitmap(icon)
    except:
        pass
    
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
            sticky = E
        elif sticky == "left":
            sticky = W
        elif sticky == "center":
            sticky = EW        
    except KeyError:
        sticky = EW       

    return sticky

#for label                                            
def colortext(**kwargs):
    try:
        colortext = kwargs["colortext"]
        return colortext
    except:
        pass
    
#for label
def background(**kwargs):
    try:
        background = kwargs["background"]
        return background
    except:
        pass
    
#wrap for label
def label_length(**kwargs):
    try:
        wrap = kwargs["wrap"]
    except KeyError:
        wrap = 600
    return wrap    

def justification(**kwargs):
    try:
        justify = kwargs["justify"]
    except KeyError:
        justify = "center"
    return justify 

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

def activebg(**kwargs):
    try: 
        activebg = kwargs["activebg"]
        return activebg
    except:
        pass
    


def select_file():
    memory["file"] = filedialog.askopenfilename(initialdir = os.getcwd()+"./",
                                            title = "Select file")

def select_folder():
    memory["folder"] = filedialog.askdirectory(initialdir = os.getcwd()+"./",
                                            title = "Select folder")   

def separator(column_length,**kwargs):
    window = new_window(**kwargs) 
    separator = Frame(memory[window],height=2, bd=1, relief="sunken")
    separator.grid(columnspan=column_length, sticky="EW",
        padx=padx(**kwargs), pady=pady(**kwargs))

def button(text,command,row,column,**kwargs):  
    window = new_window(**kwargs) 
    Button(memory[window], 
        text = text,
        command = command).grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def label(text,row,column,**kwargs):   
    window = new_window(**kwargs)
    memory["label"] = Label(memory[window], 
        text = text,
        fg = colortext(**kwargs),
        bg = background(**kwargs),
        justify = justification(**kwargs),
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
    photo = PhotoImage(file=file)
    memory["picture"] = Label(memory[window],image=photo)
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
    memory[name] = Entry(memory[window],
        width = width_entry(**kwargs))
    memory[name].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def checkbox(name,text,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = IntVar()
    memory[text] = Checkbutton(memory[window],
        text = text,
        variable = memory[name],
        bg = background(**kwargs),
        activebackground = activebg(**kwargs))
    memory[text].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def slider(name,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = Scale(memory[window],
        from_= 0, 
        to = 100, 
        orient=scale_oriental(**kwargs),
        bg = background(**kwargs))
    memory[name].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))        

def radiobox(text,row,column,**kwargs):
    window = new_window(**kwargs)
    if "radiobox" not in memory:
        memory["radiobox"] = StringVar()

    #No radio boxes are selected
    memory["radiobox"].set(None)

    if kwargs.get("value"):
        value = kwargs["value"] 
    else:
        #if value not provided, use text as value
        value = text

    radiob = Radiobutton(memory[window], 
        text = text, 
        variable = memory["radiobox"], 
        value = value,
        bg = background(**kwargs),
        activebackground = activebg(**kwargs))
    radiob.grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))    

def dropdown_list(variable,choices,default,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[variable] = StringVar(memory[window])
    popupmenu = OptionMenu(memory[window], memory[variable], *choices)
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
    memory[name] = Text(memory[window],
        wrap = WORD,
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
        wrap = WORD,
        height = 10, 
        width = 30,
        background = "grey95")
    memory[name].grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs))

def text_area_select(name):
    return memory[name].selection_get()

def text_area_clear(name):
    memory[name].delete('1.0', END)

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
def insert_text(name,text,color,**kwargs):  
    window = new_window(**kwargs)  
    memory[name].insert(0,text)
    memory[name].config(fg=color)

def insert_text_area(name,text,color,**kwargs):
    window = new_window(**kwargs) 
    memory[name].insert(1.0,text)
    memory[name].config(fg=color)

def msg_box(title,message): 
    msgbox = messagebox.showinfo(title=title, message=message)

#alarm icon in message box
def msg_box_warning(title,message): 
    msgbox = messagebox.showwarning(title=title, message=message)

def msg_box_ask(name,title,message): 
    memory[name] = messagebox.askyesnocancel(title=title, message=message)

def top_menu(**kwargs):

    window = new_window(**kwargs)
    
    menubar = Menu(memory[window])
    filemenu = Menu(menubar, tearoff=0)

    try:
        new = kwargs["new"]
        filemenu.add_command(label="New", command=new)
    except:
        pass

    try:
        openfile = kwargs["openfile"]
        filemenu.add_command(label="Open", command=openfile) 
    except:
        pass
    
    filemenu.add_command(label="Save", command="False")
    filemenu.add_command(label="Save as...", command="False")
    filemenu.add_command(label="Close", command="False")

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=memory[window].quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command="False")

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command="False")
    editmenu.add_command(label="Copy", command="False")
    editmenu.add_command(label="Paste", command="False")
    editmenu.add_command(label="Delete", command="False")
    editmenu.add_command(label="Select All", command="False")

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command="False")
    helpmenu.add_command(label="About...", command="False")
    menubar.add_cascade(label="Help", menu=helpmenu)

    memory[window].config(menu=menubar)

def app_loop(**kwargs):
    window = new_window(**kwargs)
    memory[window].mainloop()

