from logging import root
from tkinter import *
from PIL import Image
import threading

import sys

sys.path.insert(0,"..")
import client

received_message = "as"

root

class App():

    def __init__(self,master):

        HEIGHT = 600
        my_blue = "#48b8fa"
        self.master = master ## adicionei por ultimo!!!!
        global root 
        root = self.master
        master.title("Battle Royale")
        fundo = PhotoImage(file="graficos/imagens/floresta.png")
        self.big_fundo = fundo.zoom(2,2)
        WIDHT = self.big_fundo.width()
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

        buttton_confim = Button(frame_usuario,text="I'm Ready!",command= lambda: self.get_user(entry_usuario.get(),frame_usuario))
        buttton_confim.grid(row=3,column=0,pady=10)

    def wait_screen(self):
        global received_message
        my_blue = "#48b8fa"
        frame_wait = Frame(self.master,bg=my_blue,width=100,height=200)
        frame_wait.place(x = 400, y = 100)

        waiting_text = Label(frame_wait,text="Waiting players...",font=("helvetica",30),fg="white",bg="#48b8fa",anchor="center")
        waiting_text.grid(row=0,column=0,sticky="")

        number_players = Label(frame_wait,text=received_message,bg=my_blue,fg="white",font=("helvetica,25"))
        number_players.grid(row=1,column=0,sticky="")

        start_button = Button(frame_wait,text="Start!",width=15)#,command=start_click)
        start_button.grid(row=2,column=0,sticky="",pady=10)
        while True:
            self.master.update()
            self.master.update_idletasks()

    def get_user(self,usuario, frame_usuario):
        try:
            obj_socket = client.connect(usuario)
            self.master.after(1000,frame_usuario.destroy())
            #global message
            #message = ""
            communication_thread = threading.Thread(target=client.communication,args=(obj_socket,""))
            communication_thread.daemon = True
            communication_thread.start()
            self.wait_screen()
            
        except Exception as e:
            print(erro)
    
    

            


    

    

