import socket
from typing import SupportsIndex

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input("[+]Enter the host: ")
#port = int(input("[+]Enter the port : ")) 
for port in range(1,10):
    if sock.connect_ex((host,port)):
        print("port %d is closed "%port)
    else :
        print("port %d is open"% port)