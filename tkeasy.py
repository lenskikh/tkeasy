import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, colorchooser

#"Version 1.0"

 
def make_grid(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result.grid(row = kwargs.get('row', 0),
                    column = kwargs.get('column', 0),
                    padx = kwargs.get('padx', 0),
                    pady = kwargs.get('pady', 0))    

        #execution of widget parameters
        for param in kwargs:
            if 'param' in kwargs:
                try:
                    result.config(param = kwargs[param])  
                except:
                    print(kwargs)
                    result.config(kwargs)
        return result
    return wrapper


class TKeasy():
    

    def __init__(self):
        self.window = tk.Tk()

        #for take information from widgets
        self.memory = {}

        #default frame
        self.frame = tk.Frame(self.window,
                              highlightbackground = None,
                              highlightthickness = None,
                              background = None,
                              padx = None,
                              pady = None)
        
        self.frame.place(x=0,y=0)


    #add new frame
    def frames(self,frame,x,y,
               highlightbackground = None,
               highlightthickness  = None,
               background = None,
               padx = None,
               pady = None):

        self.frame = frame
        self.frame = tk.Frame(self.window,
                              highlightbackground = highlightbackground,
                              highlightthickness = highlightthickness,
                              background = background,
                              padx = padx,
                              pady = pady)
        
        self.frame.place(x = x, y = y)
    
    def Title(self,title):
        self.window.title(title)

    def bind_listen(self,event,command):
        return self.window.bind(event, command)

    #size of window, color of background window, border and icon
    def config(self,size:str = None,
               bg:str = None,
               border:int = None,
               icon:str = None):
        
        self.window.geometry(size) #correct syntax "300x300+300+300"
        self.window.configure(background=bg)
        self.window.iconbitmap(icon)

        if border == "False":
            self.window.overrideredirect(1)       
    
    def show_coords(self,event):
        print(f'x = {event.x_root}, y = {event.y_root}')

    def move_window(self,event):
        self.window.geometry(f'+{event.x_root}+{event.y_root}')        

    def hotkey(self,key,command):
        return self.window.bind(key,command)

    @make_grid #LABEL WIDGET   
    def label(self, name="label", row:int = 0, column:int = 0, padx = 0, pady = 0, **kwargs):
        self.memory[name] = tk.Label(self.frame, **kwargs)
        return self.memory[name]  
    
    def label_click(self):
        return self.memory["label"]

    def file(self,file):
        return tk.PhotoImage(file=file)
    
    @make_grid 
    def photo(self, file = None, row = 0, column = 0, padx = 0, pady = 0, **kwargs):
        photo = tk.PhotoImage(file=file)
        self.memory["picture"] = tk.Label(self.frame,image=photo, **kwargs)
        self.memory["picture"].photo = photo
        return self.memory["picture"]

    def photo_click(self,name = "picture"):
        return self.memory[name]

    @make_grid #BUTTON WIDGET
    def button(self,command:str = None, text = None, row:int = 0, column:int = 0, padx = 0, pady = 0, **kwargs):
        
        return tk.Button(self.frame,text = text,
                command = command, **kwargs)      
               
    @make_grid #ENTRY WIDGET
    def entry(self, name:str = "from_entry",row = 0,column = 0, padx = 0, pady = 0, **kwargs):
        
        self.memory[name] = tk.Entry(self.frame, **kwargs)

        return self.memory[name]
    
    @make_grid
    def text_area(self, name = "text_area", #Name by default
                  row = 0, column = 0, padx = 0, pady = 0, **kwargs):

        self.memory[name] = tk.Text(self.frame, **kwargs)

        return self.memory[name]       

    @make_grid
    def text_area_scroll(self,name = "text_area_scroll", row = 0, column = 0, padx = 0, pady = 0, **kwargs):
        self.memory[name] = scrolledtext.ScrolledText(self.frame, **kwargs)     
        return self.memory[name]  
        
    @make_grid #CHECKBUTTON WIDGET
    def checkbox(self,
                 name:str = "checkbox", #Name by default
                 text:str = "", row:int = 0, column:int = 0, padx = 0, pady = 0, **kwargs):

        self.memory[name] = tk.IntVar()
        self.memory[text] = tk.Checkbutton(self.frame,
                                           text = text,
                                           variable = self.memory[name], **kwargs)
        return self.memory[text]
    

    @make_grid #RADIOBUTTON WIDGET
    def radiobox(self,text,row:int = 0,column:int = 0, padx = 0, pady = 0, **kwargs):
        if "radiobox" not in self.memory:
            self.memory["radiobox"] = tk.StringVar()
        
        self.memory["radiobox"].set(None)
        self.memory[text] = tk.Radiobutton(self.frame, text = text, value = text, variable = self.memory["radiobox"], **kwargs)

        return self.memory[text]
    
    def dropdown_list(self,variable,choices,row = 0, column = 0, padx = 0, pady = 0, **kwargs):
        self.memory[variable] = tk.StringVar(self.frame)
        self.memory[variable].set(choices[0]) # default value
        self.memory["dropdown"] =  tk.OptionMenu(self.frame, self.memory[variable],*choices)
        for conf in kwargs:
            self.memory["dropdown"].config(kwargs)
        self.memory["dropdown"].grid(column=column, row=row)
    
    @make_grid #LISTBOX WIDGET
    def listbox(self,name = "Listbox", row = 0, column = 0, padx = 0, pady = 0, **kwargs):
        self.memory[name] = tk.Listbox(self.frame, **kwargs)
        return self.memory[name] 

    def listbox_insert(self,name,text):
        for x in text:
            self.memory[name].insert("end", x)    

    @make_grid #SPINBOX WIDGET
    def spinbox(self,name = "spinbox", from_to:str = "0-10", row = 0,column = 0, padx = 0, pady = 0, **kwargs):
 
        data1 = int(from_to.split("-")[0])
        data2 = int(from_to.split("-")[1])
        self.memory[name] = tk.Spinbox(self.frame,from_=data1, to=data2, **kwargs)

        return self.memory[name] 
    
    @make_grid #SCALE WIDGET
    def slider(self,name="slider", from_:int = 0, to:int = 100, row = 0, column = 0, padx = 0, pady = 0, **kwargs):
        self.memory[name] = tk.Scale(self.frame, from_= from_, to = to, **kwargs)
        return self.memory[name] 

    def colorpicker(self):
        return tk.colorchooser.askcolor()[1]
    
    def msg_box(self,title,message): 
        return tk.messagebox.showinfo(title=title, message=message)

    #alarm icon in message box
    def msg_box_warning(self,title,message): 
        return tk.messagebox.showwarning(title=title, message=message)    
    
    def msg_box_ask(self,name,title,message): 
        self.memory[name] = tk.messagebox.askyesnocancel(title=title, message=message)    
        return self.memory[name]
    
    #FILE NAME WITH PATH
    def select_file(self):
        return tk.filedialog.askopenfilename(initialdir = os.getcwd()+"./",title = "Select file")

    #ONLY FILE
    def only_file_name(self):
        return tk.filedialog.askopenfilename(initialdir = os.getcwd()+"./",title = "Select file").split("/")[-1]

    #ASK FOLDER
    def select_folder(self):
        return tk.filedialog.askdirectory(initialdir = os.getcwd()+"./",title = "Select folder")   

    def save_file(self):
        return tk.filedialog.asksaveasfilename(initialdir = os.getcwd()+"./",title = "Save file") 

    def clear_area(self,name):
        try:
            self.memory[name].delete(0, 'end')
        except:
            pass

        try:
            self.memory[name].delete('1.0', tk.END)
        except:
            pass 

    def text_area_select(self,name):
        return self.memory[name].selection_get()

    def get_info(self,name:str):
        try:
            return self.memory[name].get()
        except:
            return self.memory[name].get("1.0", 'end')  

    def destroy_frame(self,**kwargs):
        self.frame.destroy()     

    def save_file(self):
        return filedialog.asksaveasfilename(initialdir = os.getcwd()+"./",title = "Save file") 
    

    def insert_text_area(self,name,text,**kwargs): 
        self.memory[name].insert(1.0,text)    

    def insert_text(self,name,text,**kwargs):  
        self.memory[name].insert(0,text)     

    def listbox_item_selected(self,name):
        return self.memory[name].get("active")         

    def clipboard_in(self,selected,**kwargs):
        self.window.clipboard_clear()
        self.window.clipboard_append(selected)

    def delete_selected(self,name,**kwargs):
        self.memory[name].delete("sel.first", "sel.last")

    def paste_text(self,name,**kwargs):
        selected = self.window.clipboard_get()
        position = self.memory[name].index(tk.INSERT)
        self.memory[name].insert(position, selected)        

    def top_menu(self, tabs,**kwargs):
       
        menu_bar = tk.Menu(self.window)
        
        for name_of_tab in tabs:

            file_menu = tk.Menu(menu_bar, tearoff=0)
            menu_bar.add_cascade(label=name_of_tab, menu=file_menu)

            for name_in_menu in tabs[name_of_tab]:
            
                if name_in_menu == "---":
                    file_menu.add_separator()
                else:
                    file_menu.add_command(label=name_in_menu, 
                    command=tabs[name_of_tab][name_in_menu])

        self.window.config(menu=menu_bar)

    def focus(self, focus_name):
        self.memory[focus_name].focus()

    def clear_area(self,name_for_clear):    
        try:
            self.memory[name_for_clear].delete(0, 'end')
        except:
            pass

        try:
            self.memory[name_for_clear].delete('1.0', tk.END)
        except:
            pass    

    def quit(self,**kwargs):
        self.window.destroy()           
    
    def loop(self):
        self.window.mainloop()
        
