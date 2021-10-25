import os
from tkinter import *
from tkinter import filedialog, scrolledtext, messagebox, colorchooser

memory = {}

#version, author
def version():
    return "Version 0.8"

#new window
def new_window(**kwargs):
    try:
        window = kwargs["window"]
    except:
    #root - defualt name for the first window
        window = "root"
        
    #see example for reopen windows
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
        if name == "file" or name == "folder" or name == "save":
            return memory[name]
        else:
            #entry,checkbox,radiobox
            return memory[name].get()

def move_window(event,**kwargs):
    window = new_window(**kwargs) 
    memory[window].geometry(f'+{event.x_root}+{event.y_root}')

def advanced(**kwargs):
    window = new_window(**kwargs)
    return memory[window]

def alignment(**kwargs):
    try:
        sticky = kwargs["sticky"]
        if sticky == "right":
            sticky = "E"
        elif sticky == "left":
            sticky = "W"
        elif sticky == "center":
            sticky = "EW"        
    except KeyError:
        sticky = "EW"       

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
    
def clipboard_in(selected,**kwargs):
    window = new_window(**kwargs) 
    memory[window].clipboard_clear()
    memory[window].clipboard_append(selected)

def delete_selected(name,**kwargs):
    window = new_window(**kwargs) 
    memory[name].delete("sel.first", "sel.last")

def paste_text(name,**kwargs):
    window = new_window(**kwargs) 
    selected = memory[window].clipboard_get()
    position = memory[name].index(INSERT)
    memory[name].insert(position, selected)

def colorpicker(**kwargs):
    return colorchooser.askcolor()[1]
     
def select_file():
    return filedialog.askopenfilename(initialdir = os.getcwd()+"./",title = "Select file")

def select_folder():
    return filedialog.askdirectory(initialdir = os.getcwd()+"./",title = "Select folder")   

def save_file():
	return filedialog.asksaveasfilename(initialdir = os.getcwd()+"./",title = "Save file") 

def makegrid(fn,row,column,**kwargs):
    return fn.grid(
        row = row,
        column = column,
        sticky = alignment(**kwargs),
        padx = padx(**kwargs),
        pady = pady(**kwargs)
    )

def separator(column_length,**kwargs):
    window = new_window(**kwargs) 
    separator = Frame(memory[window],height=2, bd=1, relief="sunken")
    separator.grid(columnspan=column_length, sticky="EW",
        padx=padx(**kwargs), pady=pady(**kwargs))

def button(text,command,row,column,**kwargs):  
    window = new_window(**kwargs) 
    fn = Button(memory[window], 
        text = text,
        command = command,
        justify = justification(**kwargs))
    makegrid(fn,row,column,**kwargs)

def label(text,row,column,**kwargs):   
    window = new_window(**kwargs)
    memory["label"] = Label(memory[window], 
        text = text,
        fg = colortext(**kwargs),
        bg = background(**kwargs),
        justify = justification(**kwargs),
        font = label_font(**kwargs),
        wrap = label_length(**kwargs))
    makegrid(memory["label"],row,column,**kwargs)

def label_click():
    return memory["label"]

def photo(file,row,column,**kwargs):
    window = new_window(**kwargs) 
    photo = PhotoImage(file=file)
    memory["picture"] = Label(memory[window],image=photo)
    memory["picture"].photo = photo
    makegrid(memory["picture"],row,column,**kwargs)
 
def photo_click():
    return memory["picture"]

def entry(name,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = Entry(memory[window],
        width = width_entry(**kwargs))
    makegrid(memory[name],row,column,**kwargs)

def checkbox(name,text,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = IntVar()
    memory[text] = Checkbutton(memory[window],
        text = text,
        variable = memory[name],
        bg = background(**kwargs),
        activebackground = activebg(**kwargs))
    makegrid(memory[text],row,column,**kwargs)

def slider(name,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = Scale(memory[window],
        from_= 0, 
        to = 100, 
        orient=scale_oriental(**kwargs),
        bg = background(**kwargs))
    makegrid(memory[name],row,column,**kwargs)   

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
    makegrid(radiob,row,column,**kwargs)

def dropdown_list(variable,choices,default,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[variable] = StringVar(memory[window])
    popupmenu = OptionMenu(memory[window], memory[variable], *choices)
    memory[variable].set(default) # default value
    makegrid(popupmenu,row,column,**kwargs)

#text in text area looks ugly with scroll in macos
#you can use textarea without scroll
def text_area(name,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = Text(memory[window],
        wrap = WORD,
        height = 10, 
        width = 30,
        background = "grey95")
    makegrid(memory[name],row,column,**kwargs)

#Works slowly at big text (in macos)
def text_area_scroll(name,row,column,**kwargs):
    window = new_window(**kwargs)
    memory[name] = scrolledtext.ScrolledText(memory[window],
        wrap = WORD,
        height = 10, 
        width = 30,
        background = "grey95")
    makegrid(memory[name],row,column,**kwargs)

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

def spinbox(name,from_to,row,column,**kwargs):
    window = new_window(**kwargs)  
    data1 = int(from_to.split("-")[0])
    data2 = int(from_to.split("-")[1])
    memory[name] = Spinbox(memory[window],from_=data1, to=data2)
    makegrid(memory[name],row,column,**kwargs)

def listbox_insert(name,text):
    for x in text:
        memory[name].insert("end", x)    

def listbox_item_selected(name):
    return memory[name].get("active")


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

def top_menu(tabs,**kwargs):

    window = new_window(**kwargs)
    
    menubar = Menu(memory[window])
    
    for name_of_tab in tabs:

        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label=name_of_tab, menu=filemenu)

        for name_in_menu in tabs[name_of_tab]:
           
            if name_in_menu == "---":
                filemenu.add_separator()
            else:
                filemenu.add_command(label=name_in_menu, 
                command=tabs[name_of_tab][name_in_menu])

    memory[window].config(menu=menubar)

def quit(**kwargs):
    window = new_window(**kwargs)
    memory[window].destroy()

def app_loop(**kwargs):
    window = new_window(**kwargs)
    memory[window].mainloop()
