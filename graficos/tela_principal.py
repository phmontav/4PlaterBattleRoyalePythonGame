from tkinter import *
from PIL import Image
root = Tk()
WIDHT = 900
HEIGHT = 500
#root.geometry("800x600+300+50")
my_blue = "#48b8fa"
root.title("Battle Royale")
fundo = PhotoImage(file="jogo/graficos/floresta.png")
big_fundo = fundo.zoom(2,1)
WIDHT = big_fundo.width()

root.geometry(str(WIDHT) + "x" + str(HEIGHT) + "+80+50")

frame_up = Frame(root)
frame_up.place(relheight=0.8,relwidth=1)
bg = Label(frame_up,image=big_fundo)
bg.place(x=0,y=0)
frame_down = Frame(root,bg="gray",padx=10,relief=SUNKEN,border=10)
frame_down.place(relheight=0.3,relwidth=1,rely=0.75)















root.mainloop()