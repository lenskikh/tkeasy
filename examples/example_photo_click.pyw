from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Photo click")

gui.photo(file="1.png",row=0,column=0)
gui.photo_click().bind("<Button-1>",lambda url:gui.msg_box(title="Clicked",message="Picture 1"))

gui.photo(file="2.png",row=0,column=1)
gui.photo_click().bind("<Button-1>",lambda url:gui.msg_box(title="Clicked",message="Picture 2"))

gui.photo(file="3.png",row=1,column=0)
gui.photo_click().bind("<Button-1>",lambda url:gui.msg_box(title="Clicked",message="Picture 3"))

gui.photo(file="4.png",row=1,column=1)
gui.photo_click().bind("<Button-1>",lambda url:gui.msg_box(title="Clicked",message="Picture 4"))

gui.loop()
