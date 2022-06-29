import socket
import errno
import time
import random
from os import system


_ = system('clear')

# Choosing Nickname
print("-------------------------------------------------------------------")
print("|            Welcome to the Snake and Ladder Game                  |")
print("-------------------------------------------------------------------")

print ("Name will display on server")
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.253.3', 55555))
