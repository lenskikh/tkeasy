#ask folder - gui widget
from tkeasy import *

#root is default var of Tk
title(text="Ask Folder")
config(size="50x60")

def askfolder():
    print(select_folder())

label(text="ASK FOLDER",colortext="white",
      background="green",row=0,column=0)

button(text='CHOOSE FOLDER',command=askfolder,
       row=1,column=0)

app_loop()
