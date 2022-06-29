import socket
import threading #for performing various tasks at the same time

# Connection Data
host = '192.168.1.15'
port = 5555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
#waits for clients to connect
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []
