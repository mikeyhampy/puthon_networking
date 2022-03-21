import socket
import sys
import threading
import server_info

# server IP and port
server_ip = (server_info.SERVER_IP, server_info.SERVER_PORT)
print('connecting to server')

# conncecting to the server
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.bind(('0.0.0.0', 4374))
clientsocket.sendto(b'0', server_ip)
while True:
    data = clientsocket.recv(1024).decode()

    if data.strip() == 'ready':
        print('checking in with server, waiting')
        break

# waiting for server to send other client info
data = clientsocket.recv(1024).decode()

# other client's info
ip, sport, dport = data.split(' ')
sport = int(sport)
dport = int(dport)

print('\ngot peer')
print('punching hole')

# start peer to peer networking
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.bind(('0.0.0.0', sport))
clientsocket.sendto(b'0', (ip, dport))

print('ready to exchange messages\n')

# listen for messages to send
def listen():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientsocket.bind(('0.0.0.0', sport +2))

    while True:
        data = clientsocket.recv(1024)
        print('\rpeer: {}\n>'.format(data.decode()), end='')

# send messages to peer
listener = threading.Thread(target=listen, daemon=True)
listener.start()
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.bind(('0.0.0.0', dport))

# recieve messages from peer
while True:
    msg = input('> ')
    clientsocket.sendto(msg.encode(), (ip, sport + 2))
