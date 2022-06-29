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

# just of effects. add a delay of 1 second before performing any action
WAIT  = 1
MAX_VAL = 50

# snake takes you down
snakes = {
    39: 3,
    46: 14,
    49: 13,
}

# ladder takes you up
ladders = {
    5: 43,
    9: 30,
    20: 41,
}
