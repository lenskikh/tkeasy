from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Cards")

gui.config(size="230x100+500+300")

filename = "words.txt"
i = 0

with open(filename) as f:
    content = f.readlines()

def next_word():
    global i
    try:
        gui.label(text=content[i].strip(),background="white",width=12, padx = 5, pady = 5, row=0, column=0)
    except:
        gui.label(text="End of file",background="white",width=12, padx = 5, pady = 5, row=0, column=0)
    i+=1

gui.button(text="Next word",command=next_word, padx = 5, pady = 5, row=1,column=0)

gui.loop()
