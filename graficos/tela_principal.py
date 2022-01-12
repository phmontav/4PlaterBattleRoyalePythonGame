from tkinter import *
from PIL import Image
root = Tk()
WIDHT = 900
HEIGHT = 600
#root.geometry("800x600+300+50")
my_blue = "#48b8fa"
root.title("Battle Royale")
fundo = PhotoImage(file="jogo/graficos/floresta.png")
big_fundo = fundo.zoom(2,1)
WIDHT = big_fundo.width()

root.geometry(str(WIDHT) + "x" + str(HEIGHT) + "+80+50")

frame_up = Frame(root)
frame_up.pack(fill="both",expand=True,side="top")

bg = Label(frame_up,image=big_fundo)
bg.place(x=0,y=0)

frame_down = Frame(root,padx=105,pady=10,bg="white")
frame_down.pack(fill="both",expand=True,side="bottom")














root.mainloop()