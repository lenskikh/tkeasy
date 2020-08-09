from tkinter import *

master = Tk()

photo = PhotoImage(file="3.png")
w = Label(master, image=photo)
w.photo = photo
w.pack()

mainloop()