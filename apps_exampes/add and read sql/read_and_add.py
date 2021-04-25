#Add to database
#Search in database

from tkeasy import *
import sqlite3

title("Add and read sql db")

conn = sqlite3.connect("add_and_read.db")
cursor = conn.cursor()

try:
    cursor.execute('''CREATE TABLE info
             (lines text)''')
except:
    pass

add = "INSERT INTO info(lines) values (?)"
discover = "SELECT * FROM info WHERE lines=?"

def add_to_db():
    info = get_info("entry 1")
    cursor.execute(add, [(info)])
    conn.commit()
    label(text="Info was added",colortext="black",
              background="lightgreen",row=2,column=0)
   
def search():
    info = get_info("entry 1")
    
    cursor.execute(discover, [(info)])
    #strict search
    check = cursor.fetchall()
    if check==None:
        #red text if can't find anything
        label(text="NO INFO",colortext="white",
              background="red",row=2,column=0)
    else:
        #output multiply lines from db 
        rownumber = 2
        for rowinfo in check:          
            label(text=rowinfo,colortext="black",
                  background="lightblue",row=rownumber,column=0)
            rownumber+=1

entry(name="entry 1",row=1,column=0)

button(text="Add to db",
       command=add_to_db,row=1,column=1)

button(text="Search",
       command=search,row=2,column=1)

app_loop()
conn.close()
