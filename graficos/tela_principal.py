from cProfile import label
from cgitb import text
from email.mime import image
from tkinter import *
from PIL import Image
root = Tk()
WIDHT = 900
HEIGHT = 500
#root.geometry("800x600+300+50")
my_blue = "#48b8fa"
root.title("Battle Royale")
fundo = PhotoImage(file="graficos/imagens/floresta.png")
big_fundo = fundo.zoom(2,1)
WIDHT = big_fundo.width()


#my_help = str(help(Text))
#print(my_help)

warrior = PhotoImage(file="graficos/imagens/warrior2.gif")
warrior = warrior.subsample(3,3)
print(warrior.width())
print(warrior.height())

root.geometry(str(WIDHT) + "x" + str(HEIGHT) + "+80+50")
root.resizable(False,False)

#create upper division
frame_up = Frame(root)
frame_up.place(relheight=0.8,relwidth=1)
my_canvas = Canvas(frame_up)
my_canvas.pack(fill="both",expand=True)
my_canvas.create_image(0,0,image=big_fundo,anchor="nw")
my_canvas.create_image(100,280,image= warrior)


label = Label(frame_up,text="aaaaaa")
but_window = my_canvas.create_window(10,10,anchor="nw",window=label)
#bg = Label(frame_up,image=big_fundo)
#bg.place(x=0,y=0)




#create lower division
frame_down = Frame(root,bg="gray",padx=10,relief=SUNKEN,border=8)
frame_down.place(relheight=0.3,relwidth=1,rely=0.75)
txt = Label(frame_down,text="aasdadaadaada")
txt.pack()













root.mainloop()


print("aaaa")
