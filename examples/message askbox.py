from tkeasy import *

title_size("Ask message box","")

def showinfo():
    print(memory["ask"])
    
msgboxask("ask","Message box","A system can't find file. Would you like created it?")
buttons("get info",showinfo,0,0,"center")
