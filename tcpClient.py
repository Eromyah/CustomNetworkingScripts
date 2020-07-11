#!/usr/bin/python3


import socket

target_host = "192.168.168.106"
target_port = 9999 

# create a socket object the AF_INET indicates its going to use IPv4 and SOCK_STREAM indicates that it will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
message = input("What do you want to send?")
client.send(message.encode())

# receive some data
response = client.recv(4096)

decoded = response.decode()
print(decoded)

