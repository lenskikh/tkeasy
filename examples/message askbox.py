from tkeasy import *

#root is default var
root.title("Ask message box")

def showinfo():
    print(memory["ask"])

buttons(text="get info",command=showinfo,row=0,column=0,sticky="center")    
msgboxask("ask","Message box","A system can't find file. Would you like created it?")

