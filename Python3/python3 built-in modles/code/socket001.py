import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serversocket.bind((host, port))

serversocket.listen(5)

while True:
    clinetsocket, addr = serversocket.accept()
    
    print("link address %s" % str(addr))
    msg = "first socket \n"
    clinetsocket.send(msg.encode('utf-8'))
    clinetsocket.close()