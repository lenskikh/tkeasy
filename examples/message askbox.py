from tkeasy import *

title("Ask message box","")

def showinfo():
    print(memory["ask"])
    
msgboxask("ask","Message box","A system can't find file. Would you like created it?")
buttons("get info",showinfo,0,0,"center")

root.mainloop()
