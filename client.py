import socket
import sys
import threading

server_ip = ('', 22)
print('connecting to server')

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.bind(('0.0.0.0', 4374))
clientsocket.sendto(b'0', server_ip)

while True:
    data = clientsocket.recv(1024).decode()

    if data.strip() == 'ready':
        print('checking in with server, waiting')
        break

data = clientsocket.recv(1024).decode()
ip, sport, dport = data.split(' ')
sport = int(sport)
dport = int(dport)

print('\ngot peer')
print('  ip:           {}'.format(ip))
print('  source port:  {}'.format(sport))
print('  dest port     {}'.format(dport))

print('punching hole')

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.bind(('0.0.0.0', sport))
clientsocket.sendto(b'0', (ip, dport))

print('ready to exchange messages\n')

def listen():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientsocket.bind(('0.0.0.0', sport +2))

    while True:
        data = clientsocket.recv(1024)
        print('\rpeer: {}\n>'.format(data.decode()), end='')
listener = threading.Thread(target=listen, daemon=True)
listener.start()

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.bind(('0.0.0.0', dport))

while True:
    msg = input('> ')
    clientsocket.sendto(msg.encode(), (ip, sport + 2))
