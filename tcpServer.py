#!/usr/python3

import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("[*] Listening on " + str(bind_ip) +":" + str(bind_port))

#this is my client-handling thread

def handle_client(socket):

    #prints out what the client sends
    data = socket.recv(4096).decode()

    print(f"[*] Received data: {data}")

    #send back a packet
    message = "Hello and Welcome to my simple TCP Server"
    client_socket.send(message.encode())

    client_socket.close()

#Accept Connections
while True:
    client_socket, addr = server.accept()
    print(f"[*] Accepted Connection from: {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()


