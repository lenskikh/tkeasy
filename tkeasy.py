import os
from tkinter import *
from tkinter import filedialog, scrolledtext, messagebox, colorchooser

memory = {}

#version
def version():
    return "Version 0.99"

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

#A frame by default if didn't set by user 
def frames(**kwargs):   
    window = new_window(**kwargs) 
    
    try:
        frame = kwargs["frame"]["name_of_frame"]       
    except:
        frame = "root_frame"

    try:
        x = kwargs["frame"]["x"]
        y = kwargs["frame"]["y"]
    except:
        x = 0
        y = 0

    try:
        highlightthickness = kwargs["frame"]["border_thickness"]
    except:
        highlightthickness = None

    try:
        highlightbackground = kwargs["frame"]["border_color"]
    except:
        highlightbackground = None

    try:
        background = kwargs["frame"]["background"]
    except:
        background = None

    try:
        padx = kwargs["frame"]["padx"] 
    except:
        padx = 1

    try:
        pady = kwargs["frame"]["pady"]
    except:
        pady = 1

    try:
        width = kwargs["frame"]["width"]
    except:
        width = None

    try:
        height = kwargs["frame"]["height"]
    except:
        height = None

    if frame not in memory:
        memory[frame] = Frame(memory[window],highlightbackground=highlightbackground,highlightthickness=highlightthickness,background=background,padx=padx,pady=pady)
        memory[frame].place(x=x,y=y)

    return frame        
    
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
        return memory[name].get()
    except:
        return memory[name].get("1.0", 'end')

def move_window(event,**kwargs):
    window = new_window(**kwargs) 
    memory[window].geometry(f'+{event.x_root}+{event.y_root}')

def advanced(**kwargs):
    window = new_window(**kwargs)
    return memory[window]

def hotkey(key,command,**kwargs):
    window = new_window(**kwargs)
    return memory[window].bind(key,command)

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

#for label, button                                            
def colortext(**kwargs):
    try:
        colortext = kwargs["colortext"]
        return colortext
    except:
        colortext = None
    
#for label, button
def background(**kwargs):
    try:
        background = kwargs["background"]
        return background
    except:
        background = None
    
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
        return justify 
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

def width_settings(**kwargs):
    try:
        width = kwargs["width"]
    except:
        width = None
    return width

def height_settings(**kwargs):
    try:
        height = kwargs["height"]
    except:
        height = None
    return height

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

def inner_border(**kwargs):
    try: 
        inner_border = kwargs["inner_border"]
        return inner_border
    except:
        pass

def asterisks(**kwargs):
    try: 
        asterisks = kwargs["asterisks"]
        return asterisks
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

def select_file_name():
    return filedialog.askopenfilename(initialdir = os.getcwd()+"./",title = "Select file").split("/")[-1]

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

def button(text,command,row,column,**kwargs):  
    window = new_window(**kwargs) 
    frame = frames(**kwargs)
    fn = Button(memory[frame], 
        text = text,
        command = command,
        bg = background(**kwargs),
        fg = colortext(**kwargs),
        justify = justification(**kwargs),)
    makegrid(fn,row,column,**kwargs)

def label(text,row,column,**kwargs):   
    window = new_window(**kwargs)
    frame = frames(**kwargs)
    memory["label"] = Label(memory[frame], 
        text = text,
        fg = colortext(**kwargs),
        bg = background(**kwargs),
        justify = justification(**kwargs),
        font = label_font(**kwargs),
        wrap = label_length(**kwargs),
        width=width_settings(**kwargs),
        height=height_settings(**kwargs))
    makegrid(memory["label"],row,column,**kwargs)

def label_click():
    return memory["label"]

def photo(file,row,column,**kwargs):
    window = new_window(**kwargs) 
    frame = frames(**kwargs)
    photo = PhotoImage(file=file)
    memory["picture"] = Label(memory[frame],image=photo)
    memory["picture"].photo = photo
    makegrid(memory["picture"],row,column,**kwargs)
 
def photo_click():
    return memory["picture"]

def entry(name,row,column,**kwargs):
    window = new_window(**kwargs)
    frame = frames(**kwargs)
    memory[name] = Entry(memory[frame],
        width = width_settings(**kwargs),
        bd = inner_border(**kwargs),
        bg = background(**kwargs),
        show=asterisks(**kwargs),
        justify = justification(**kwargs))
    makegrid(memory[name],row,column,**kwargs)

def checkbox(name,text,row,column,**kwargs):
    window = new_window(**kwargs)
    frame = frames(**kwargs)
    memory[name] = IntVar()
    memory[text] = Checkbutton(memory[frame],
        text = text,
        variable = memory[name],
        bg = background(**kwargs),
        activebackground = activebg(**kwargs))
    makegrid(memory[text],row,column,**kwargs)

def slider(name,row,column,**kwargs):
    window = new_window(**kwargs)
    frame = frames(**kwargs)
    memory[name] = Scale(memory[frame],
        from_= 0, 
        to = 100, 
        orient=scale_oriental(**kwargs),
        bg = background(**kwargs))
    makegrid(memory[name],row,column,**kwargs)   

def radiobox(text,row,column,**kwargs):
    window = new_window(**kwargs)
    frame = frames(**kwargs)
    if "radiobox" not in memory:
        memory["radiobox"] = StringVar()

    #No radio boxes are selected
    memory["radiobox"].set(None)

    if kwargs.get("value"):
        value = kwargs["value"] 
    else:
        #if value not provided, use text as value
        value = text

    radiob = Radiobutton(memory[frame], 
        text = text, 
        variable = memory["radiobox"], 
        value = value,
        bg = background(**kwargs),
        activebackground = activebg(**kwargs))
    makegrid(radiob,row,column,**kwargs)

def dropdown_list(variable,choices,default,row,column,**kwargs):
    window = new_window(**kwargs)
    frame = frames(**kwargs)
    memory[variable] = StringVar(memory[window])
    popupmenu = OptionMenu(memory[frame], memory[variable], *choices)
    memory[variable].set(default) # default value
    makegrid(popupmenu,row,column,**kwargs)

#text in text area looks ugly with scroll in macos
#you can use textarea without scroll
def text_area(name,row,column,**kwargs):
    window = new_window(**kwargs)
    frame = frames(**kwargs)
    memory[name] = Text(memory[frame],
        wrap = WORD,
        bd = inner_border(**kwargs),
        bg = background(**kwargs),        
        height = height_settings(**kwargs), 
        width = width_settings(**kwargs))
    makegrid(memory[name],row,column,**kwargs)

#Works slowly at big text (in macos)
def text_area_scroll(name,row,column,**kwargs):
    window = new_window(**kwargs)
    frame = frames(**kwargs)
    memory[name] = scrolledtext.ScrolledText(memory[frame],
        wrap = WORD,
        bd = inner_border(**kwargs),
        bg = background(**kwargs),        
        height = height_settings(**kwargs), 
        width = width_settings(**kwargs),
        background = "grey95")
    makegrid(memory[name],row,column,**kwargs)

def text_area_select(name):
    return memory[name].selection_get()

def clear_area(name):
    try:
        memory[name].delete(0, 'end')
    except:
        pass

    try:
        memory[name].delete('1.0', END)
    except:
        pass

def listbox(name,row,column,**kwargs):
    window = new_window(**kwargs)
    frame = frames(**kwargs)
    try:
        height = kwargs["height"]
    except:
        height = None

    try:
        width = kwargs["width"]
    except:
        width = None

    memory[name] = Listbox(memory[frame],height = height,width=width)
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
    frame = frames(**kwargs) 
    data1 = int(from_to.split("-")[0])
    data2 = int(from_to.split("-")[1])
    memory[name] = Spinbox(memory[frame],from_=data1, to=data2)
    makegrid(memory[name],row,column,**kwargs)

def listbox_insert(name,text):
    for x in text:
        memory[name].insert("end", x)    

def listbox_item_selected(name):
    return memory[name].get("active")

#for change text in text area
def insert_text(name,text,**kwargs):  
    window = new_window(**kwargs)  
    memory[name].insert(0,text)
    try:
        memory[name].config(fg=kwargs["color"])
    except:
        memory[name].config(fg="black")

def insert_text_area(name,text,color,**kwargs):
    window = new_window(**kwargs) 
    memory[name].insert(1.0,text)
    memory[name].config(fg=color)

def focus(name):
    #set focus on specific widget
    memory[name].focus()

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