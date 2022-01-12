from socket import *

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

def message(obj_socket, id):
    while True:
        resposta = obj_socket.recv(1024).decode()
        aux_list = resposta.split(":")
        #if(aux_list[0] != ""):
            #print(aux_list)
        if(aux_list[0] == "ID"):
            id = aux_list[1] #string
            #print("ID " + id)
            confirm(obj_socket)
        elif(aux_list[0] == "MSG"):
            print(aux_list[1] + "\n")
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

        



servidor = gethostbyname(gethostname())
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor,porta))
msg = input("insert Name: ")
obj_socket.send(msg.encode())

try:
    while True:
        
        message(obj_socket,"")
        #print(resposta.split(":"))
except:
    obj_socket.close()



""" 
while True: 
    play()  
 """