
from socket import *
from graficos import connection_screen
#import main
def turno(obj_socket, id):
    choice = input("write A for Attack or D for Defense: ").upper()
    obj_socket.send(("ACT:" + id + ":" + str(choice)).encode())
    if(choice == "A"):
        while True:
            resposta = obj_socket.recv(1024).decode()
            aux_list = resposta.split(":")
            if(aux_list[0] == "CH"):
                print(aux_list[1] + "\n")
                which = "CH:"
                which += input("Which one? ")
                obj_socket.send(which.encode())
                #print("which" + which)
                break
    

def confirm(obj_socket):
    obj_socket.send(("OK:").encode())

def communication(obj_socket, id):
    while True:
        connection_screen.received_message
        resposta = obj_socket.recv(1024).decode()
        aux_list = resposta.split(":")
        if(aux_list[0] != ""):
            if(aux_list[0] == "ID"):
                id = aux_list[1] #string
                #print("ID " + id)
                confirm(obj_socket)
            elif(aux_list[0] == "MSG"):
                #print(aux_list[1] + "\n")
                connection_screen.received_message = aux_list[1]
                print(connection_screen.received_message + "----")
                confirm(obj_socket)
            elif(aux_list[0] == "PL"):
                print(aux_list[1] + "\n")
                confirm(obj_socket)
                turno(obj_socket,id)
            elif(aux_list[0] == "CH"):
                print(aux_list[1] + "\n")
                resp = input("Which one?")
                obj_socket.send(resp.encode())
            elif(aux_list[0] == "CL"):
                print("You Died\n")
                confirm(obj_socket)
            elif(aux_list[0] == "WIN"):
                print(aux_list[1] + "\n")
                confirm(obj_socket)
            elif(aux_list[0] == "END"):
                print("END OF BATTLE\n")
                confirm(obj_socket)
                obj_socket.close()
            connection_screen.received_message = aux_list[1]
            #connection_screen.root.update()
            #connection_screen.root.update_idletasks()

        

def connect(name):

    try:
        servidor = gethostbyname(gethostname())
        porta = 43210

        obj_socket = socket(AF_INET, SOCK_STREAM)
        obj_socket.connect((servidor,porta))
        msg = name
        obj_socket.send(msg.encode())
        return obj_socket
    except:
        raise




def play(obj_socket):
    try:
        while True:
            
            communication(obj_socket,"")
            #print(resposta.split(":"))
    except:
        #obj_socket.close()
        pass

if __name__ == "__main__":
    communication(connect("miando"),"")