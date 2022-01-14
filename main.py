import sys
from graficos.connection_screen import App
from tkinter import *
from PIL import Image

#problema com path do python
sys.path.insert(0,sys.path[0] + "/graficos")
import client

root = Tk()




def startGui():
    app = App(root)
    root.mainloop()




if __name__=="__main__":
    startGui() 