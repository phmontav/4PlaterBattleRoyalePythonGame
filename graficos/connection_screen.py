
import imp
from tkinter import *
from PIL import Image

class App():

    def __init__(self,master):

        HEIGHT = 600
        my_blue = "#48b8fa"
        master.title("Battle Royale")
        fundo = PhotoImage(file="graficos/imagens/floresta.png")
        self.big_fundo = fundo.zoom(2,2)
        WIDHT = self.big_fundo.width()
        print(WIDHT)
        master.geometry(str(WIDHT + 30) + "x" + str(HEIGHT) + "+80+50")

        bg = Label(master,image=self.big_fundo)
        bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame_usuario = Frame(master,bg=my_blue,width=100,height=200)
        frame_usuario.place(x = 500, y = 100)

        welcome_text = Label(frame_usuario,text="Welcome!",font=("helvetica",30),fg="white",bg="#48b8fa",anchor="center")
        welcome_text.grid(row=0,column=0,sticky="")

        text_usuario = Label(frame_usuario,text="Insert Your name",bg=my_blue)
        text_usuario.grid(row=1,column=0)

        entry_usuario = Entry(frame_usuario,bg="white",relief=SUNKEN)
        entry_usuario.grid(row=2,column=0)

        buttton_confim = Button(frame_usuario,text="I'm Ready!")#,command=get_user)
        buttton_confim.grid(row=3,column=0,pady=10)

    

    

