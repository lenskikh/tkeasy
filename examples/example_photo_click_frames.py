from tkeasy import *

title("Photo click")

photo(frame="1",x=5,y=5,file="1.png",row=0,column=0)
photo_click().bind("<Button-1>",lambda url:
                   msg_box(title="Clicked",message="Picture 1"))

photo(frame="1",x=5,y=5,file="2.png",row=0,column=1)
photo_click().bind("<Button-1>",lambda url:
                   msg_box(title="Clicked",message="Picture 2"))

photo(frame="2",x=63,y=60,file="3.png",row=1,column=0)
photo_click().bind("<Button-1>",lambda url:
                   msg_box(title="Clicked",message="Picture 3"))

photo(frame="2",x=63,y=60,file="4.png",row=1,column=1)
photo_click().bind("<Button-1>",lambda url:
                   msg_box(title="Clicked",message="Picture 4"))

app_loop()
