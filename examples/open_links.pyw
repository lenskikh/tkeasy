from tkeasy import TKeasy
import webbrowser

gui = TKeasy()

def open_url(link):
    webbrowser.open_new_tab(link)

gui.Title("Open links")
    
gui.label(text="Python official website", fg="blue",row=0)
gui.label_click().bind("<Button-1>",lambda url:open_url("https://www.python.org/"))

gui.label(text="Google official website", fg="blue",row=1)
gui.label_click().bind("<Button-1>",lambda url:open_url("https://www.google.com"))

gui.label(text="Gmail website", fg="blue",row=2)
gui.label_click().bind("<Button-1>",lambda url:open_url("https://www.gmail.com"))

gui.loop()
