#ask folder - gui widget
from tkeasy import *

title(text="Ask Folder")

def askfolder():
    print(select_folder())

label(text="ASK FOLDER",colortext="white",
      background="green",row=0,column=0)

button(text='CHOOSE FOLDER',command=askfolder,
       row=1,column=0)

app_loop()
