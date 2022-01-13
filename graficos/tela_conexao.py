from tkinter import *
from PIL import Image
import sys
sys.path.insert(0,"jogo")

import os
def get_user():
    
    usuario = entry_usuario.get()
   # root.after(1000,root.quit())
    connection_screen()
    return usuario

def connection_screen():
    frame_usuario.destroy()
    root.update()

root = Tk()
WIDHT = 900
HEIGHT = 600
#root.geometry("800x600+300+50")
my_blue = "#48b8fa"
root.title("Battle Royale")

fundo = PhotoImage(file="graficos/imagens/floresta.png")
big_fundo = fundo.zoom(2,2)
WIDHT = big_fundo.width()

root.geometry(str(WIDHT + 30) + "x" + str(HEIGHT) + "+80+50")

bg = Label(root,image=big_fundo)
bg.place(x=0,y=0,relwidth=1,relheight=1)

frame_usuario = Frame(root,bg=my_blue,width=100,height=200)
frame_usuario.place(x = 500, y = 100)

welcome_text = Label(frame_usuario,text="Welcome!",font=("helvetica",30),fg="white",bg="#48b8fa",anchor="center")
welcome_text.grid(row=0,column=0,sticky="")

text_usuario = Label(frame_usuario,text="Insert Your name",bg=my_blue)
text_usuario.grid(row=1,column=0)

entry_usuario = Entry(frame_usuario,bg="white",relief=SUNKEN)
entry_usuario.grid(row=2,column=0)

buttton_confim = Button(frame_usuario,text="I'm Ready!",command=get_user)
buttton_confim.grid(row=3,column=0,pady=10)


root.mainloop()









