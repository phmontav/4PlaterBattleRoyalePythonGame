from socket import *
import os
from _thread import *
import player
from player import *
import random
import sys
import threading

def wait_response(con):
    while True:
        resp = con.recv(1024).decode()
        if(resp.split(":")[0] == "OK"):
            break

def broadcast_send(msg):
    for conn in connection_list:
        conn.send(msg)
    total_resp = 0
    while total_resp < len(connection_list):
        for conn in connection_list:
            resp = conn.recv(1024).decode()
            if(resp.split(":")[0] == "OK"):
                total_resp += 1

def get_multiplier():
    roll = random.randrange(-2,10)
    if(roll >= 8):
        return 1.4
    elif (roll < 0):
        return 0.8
    else: return 1.0 

def get_msg(value):
    if(value > 1.0):
        return " Great "
    elif(value < 1.0):
        return " Bad "
    else:
        return " Normal "
    

def end_battle():
    if len(player_list) == 1:
        connection_list[player_list[0][0].id].send(("WIN:Congratulation!! You won").encode())
        wait_response(connection_list[player_list[0][0].id])
        broadcast_send(("END:").encode())
        print("END OF BATTLE\n")
        
        sys.exit()
        


def battle():
    print("battle")
    battle_log = "MSG: ###### Battle log #######\n"
    for i in range(0,len(player_list)):
        val = get_multiplier()
        if player_list[i][1] == "D":
            battle_log += player_list[i][0].nome + " Had a" + get_msg(val) + "Defense\n"
            player_list[i][0].defense *= val
    for i in range(0,len(player_list)):
        val = get_multiplier()
        if player_list[i][1][0] == "A":
            battle_log += player_list[i][0].nome + " Attacks " + player_list[int(player_list[i][1][1])][0].nome + "\n"
            battle_log += player_list[i][0].nome + " Had a" + get_msg(val) + "Attack\n"
            player_list[i][0].attack *= val
            player_list[int(player_list[i][1][1])][0].life -= 10 * player_list[i][0].attack/player_list[int(player_list[i][1][1])][0].defense
    battle_log += "\n#### Player's Life####\n"
    for players in player_list:
        battle_log += players[0].nome + " " + str(players[0].life) + "\n"
        players[0].attack = 10.0 ## corrigir ataque
        players[0].defense = 1.0
        players[1] = ""
    battle_log += "\n### DEATHS ###\n"

    for i in range(0,len(player_list)):
        #print(i)
        if player_list[i][0].life <= 0:
            battle_log += player_list[i][0].nome + " Died\n"
            connection_list[player_list[i][0].id].send(("CL:").encode())
            wait_response(connection_list[i])
            player_list.pop(i)
            
            
    broadcast_send(battle_log.encode())
    print(battle_log + "\n")
    end_battle()
    
        

        

                   

def threaded_clients(con,total):
    con.send(("ID:" + str(total)).encode())
    wait_response(con)
    #print(total)
    broadcast_send(("MSG:Number of players " + str(total)).encode())
    if(total == 2):
        broadcast_send("MSG:The battle will start!".encode())
        print("The battle will start!")
        
        while True:
            broadcast_send(("PL: Choose your action").encode())
            print("Waiting actions")
            act_count = 0
            while act_count < total:
                for con in connection_list:
                    resposta = con.recv(1024).decode()
                    aux_list = resposta.split(":")
                    if(aux_list[0] == "ACT"):
                       # print(aux_list)
                        act_count += 1
                        which_player = aux_list[1]
                        action = aux_list[2]
                        player_list[int(which_player) - 1][1] = action
            count = 0
            for i in range( 0 , len(player_list)):
                #print("####")
                #print(i)
                #print(player_list[i])
                if(player_list[i][1] == "A"):
                    count += 1
                    msg = "CH:Choose player to attack\n"
                    for j in range(0,len(player_list)):
                        if(i != j):
                            msg += str(j) + " " + player_list[j][0].nome
                    msg += "\n"
                    connection_list[i].send(msg.encode())
                    #print(msg)
                    #wait_response(connection_list[i])
            responses = 0
            while responses < count:
                #print(count)
                for i in range(0,len(connection_list)):
                    if(player_list[i][1] == "A"):
                        #print(i)
                        resp = connection_list[i].recv(1024).decode()
                        if(resp.split(":")[0] == "CH"):
                           # print(resp.split(":"))
                            responses += 1
                            #print (str(count) + " &&&" + str(responses))
                           #print(player_list)
                            player_list[i][1] += resp.split(":")[1]
                           # print(player_list)
                           # print("qqqqq")
            #print(player_list)
            battle()
    


servidor = str(gethostbyname(gethostname()))
porta  = 43210
player_list = []
connection_list = []
obj_socket = socket(AF_INET,SOCK_STREAM)
try:
    obj_socket.bind((servidor,porta))
except :
    pass
    
obj_socket.listen(2)

try:
    print("waiting for players...")
    total = 0
   
    while True:
        con,cliente = obj_socket.accept()
        username = con.recv(1024).decode()
        print("MSG:" + str(username) + " connected")
        player_list.append([player(username,total),""])
        connection_list.append(con)
        print(player_list)
        total += 1
        #con.send("ID " + str(total).encode())
        
        th = threading.Thread(target=threaded_clients(con,total))
        th.daemon = True
        th.start()
        #start_new_thread(threaded_clients,(con,total,run).daemon)
          
        

    
except :   
    obj_socket.close()
    
obj_socket.close()
