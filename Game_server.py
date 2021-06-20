import tkinter as tk
from tkinter import *
import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",55555))
server.listen()

clients = []
nicknames = []

room = {}

def broadcast(message):
    for client in clients:
        if(type(message) is bytes):
            client.send(message)

def send_number(room_code,number):
    for client in room.get(room_code):
        print(client)
        client.send(number)

def handel(client):
    while True:
        try:
            message = client.recv(1024)
            message1 = message.decode("ascii")
            if (str(message1).startswith("room")):
                message1 = str(message1).split()
                print(type(message1[-1]))
                if(room.get(message1[-1])):
                    room.get(message1[-1]).append(client)
                else:
                    room[message1[-1]] = [client]
                print(room)

            if (str(message1).startswith("number")):
                message1 = str(message1).split()
                room_code = message1[-2]
                number = message1[-1].encode("ascii")
                send_number(room_code,number)
            else:
                broadcast(message)
                
        except Exception as e:
            print(e)
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"{nickname} left the game")
                nicknames.remove(nickname)
                break

def receive():
    while True:
        client,address = server.accept()
        print(f"client added to {address}")
        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)
        print(nickname)
        print(f"nickname of the client is {nickname}")
        t1 = threading.Thread(target=handel, args=(client,))
        t1.start()


print("server start")
receive()    