from tkeasy import *

title("wordpad")

def new_file():
    text_area_clear("area 2")
    
def open_in_menu():
    select_file()
    print(get_info("file"))

def save():
    save_file()
    name_for_save = get_info("save")
    text_file = open(name_for_save, 'w')
    text_file.write(get_info("area 2"))
	# Close the file
    text_file.close()

top_menu(new=new_file,openfile=open_in_menu,save=save)

text_area(name="area 2", row=0,column=0)

app_loop()
