from tkeasy import *

label(frame="1",x=10,y=10,text="" ,background="#7cc5ba",font=14,row=0,column=0,padx=0,pady=0)

frame3 = Frame(advanced(),highlightbackground="#7cc5ba",highlightthickness=1,width=110, height=101)
frame3.place(x=10,y=50)

button(frame="2",x=15,y=55,text="  7  ",command=False,row=0,column=0)
button(frame="2",x=15,y=55,text="  8  ",command=False,row=0,column=1)
button(frame="2",x=15,y=55,text="  9  ",command=False,row=0,column=2)

button(frame="2",x=15,y=55,text="  4  ",command=False,row=1,column=0)
button(frame="2",x=15,y=55,text="  5  ",command=False,row=1,column=1)
button(frame="2",x=15,y=55,text="  6  ",command=False,row=1,column=2)

button(frame="2",x=15,y=55,text="  1  ",command=False,row=2,column=0)
button(frame="2",x=15,y=55,text="  2  ",command=False,row=2,column=1)
button(frame="2",x=15,y=55,text="  3  ",command=False,row=2,column=2)
