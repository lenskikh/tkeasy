from tkeasy import TKeasy

gui = TKeasy()

gui.Title("Photos")

gui.photo("1.png",padx = 0, pady =0, borderwidth = 0)
gui.photo("2.png",row = 1, padx = 0, pady =0, borderwidth = 0)
gui.photo("3.png",column = 1, padx = 0, pady =0, borderwidth = 0)
gui.photo("4.png",row = 1,column = 1, padx = 0, pady =0, borderwidth = 0)

gui.loop()
