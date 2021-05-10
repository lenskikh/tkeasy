from tkeasy import *

title(text="The first window")

label(text="William Shakespeare was the son of",row=0,column=0)
separator(column_length=1)
label(text="John Shakespeare a successful glove-maker",row=2,column=0)

title(window="second",text="The second window")
label(window="second",text="Throughout his career, Shakespeare divided his",row=0,column=0)
separator(window="second",column_length=1)
label(window="second",text="time between London and Stratford",row=2,column=0)

app_loop()

