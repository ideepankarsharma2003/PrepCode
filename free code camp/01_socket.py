# importing the module
import os
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# host ----> 'data.pr4e.org'
# port ---> 80

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)  # sends the command line across the internet

while True:
    data = mysock.recv(512)  # receive 512 characters in each iteration
    if(len(data) < 1):  # 0 characters means the end of the string
        break
    print(data.decode())
    mysock.close()
