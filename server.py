import socket
import threading	#execute multiple tasks at the same time

#declare ip, port
host= '192.168.253.3' #server vm ip address
PORT= 8888

#create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully.\n")

server.bind(('', PORT))
print("Socket is binded successfully to the port.\n")

#listen to client that wants to connect to server
server.listen()
print("Waiting for client(s)!\n")

clients = []    #keep list of clients
nicknames = []  #keep list of clients' nicknames

#function to inform clients their current positions in the game
def broadcast(msg):
    for client in clients:
        print(msg)

#function to handle client
def handle(client):
    while True:
        try:    
            position = client.recv(1024) 			                     #broadcast msg 
        except:        			 			                                 #handle exception
            index = clients.index(client)
            clients.remove(client) 				                         #remove clients
            client.close() 						                             #close clients
            nn = nicknames[index]
            broadcast('{} left!'.format(nn).encode('ascii'))       #broadcast clients who left game
            nicknames.remove(nn) 				                           #remove nicknames
            break

#receive and listen
def receive():
    while True:
        # accept connection
        client, addr = server.accept()
        print("Connected to {}".format(str(addr))+"!\n")

        #ask client to input nickname
        client.send('NICK'.encode('ascii'))
        nn = client.recv(1024).decode('ascii')
        nicknames.append(nn)					    #add nn to nicknames[]
        clients.append(client) 					  #add client to clients[]

        #print nickname
        print("Client nickname: {}".format(nn)) 

        #broadcast the nickname entered by client and successful connection
        broadcast("{} joined the game.Hi there!".format(nn).encode('ascii'))
        client.send('Client is connected to the server.\n'.encode('ascii'))

        #handle thread for clients
        thread = threading.Thread(target=handle, args=(client,))
        thread.start() 						#start thread


print("Listening to incoming clients...")

#while-loop that loops forever and  accepts new connections from clients whenever there is any
receive()
