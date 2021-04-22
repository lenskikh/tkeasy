#An example app. The application tests the knowledge
#of the multiplication table with increasing difficulty.
#tkeasy.py should be in root folder
from tkeasy import *
import random

varib = {"level":9}

def info():
   
    answer = get_info("entry 1")
    result = eval(varib['question'])
    
    if int(answer)==result:
        label(text="The answer is correct",
              colortext="white",background="green",
              row=2,column=0) 
    else:
        label(text=answer+" is "+"wrong answer!",
              colortext="white",background="red",
              row=2,column=0) 
    
title("Check your math")

def render():
    varib['a'] = random.randrange(2,9)
    varib['b'] = random.randrange(2,varib["level"])
    varib['question'] = str(varib['a'])+"*"+str(varib['b'])

def newlevel():
    varib["level"]+=90

def new():
    render()

    entry(name="entry 1",
               row=1,column=0)

    button(text="Check answer",
           command=info,row=0,column=1)

    label(text=varib['question'],
          colortext="white",background="green",
          row=0,column=0)

    label(text="",background="lightgrey",
          row=2,column=0)     

button(text="New task",
       command=new,row=1,column=1)

button(text="Next level",
       command=newlevel,row=2,column=1)

app_loop()
