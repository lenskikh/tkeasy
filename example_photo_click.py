from tkeasy import *

title("Photo click")

photo(file="1.png",row=0,column=0)
photo_click().bind("<Button-1>",lambda url:
                   msg_box(title="Clicked",message="Picture 1"))

photo(file="2.png",row=0,column=1)
photo_click().bind("<Button-1>",lambda url:
                   msg_box(title="Clicked",message="Picture 2"))

photo(file="3.png",row=1,column=0)
photo_click().bind("<Button-1>",lambda url:
                   msg_box(title="Clicked",message="Picture 3"))

photo(file="4.png",row=1,column=1)
photo_click().bind("<Button-1>",lambda url:
                   msg_box(title="Clicked",message="Picture 4"))

