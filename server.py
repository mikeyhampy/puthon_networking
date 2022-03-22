import socket
import server_info

# initialize server
port = 4375
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind(('0.0.0.0', server_info.SERVER_PORT))


# listen for people to connect
while True:
    clients_to_connect = []

    while True:
        data, address = serversocket.recvfrom(128)

        print('connection from: first client')
        clients_to_connect.append(address)

        serversocket.sendto(b'ready', address)

        # once there are two people are connected to server, it continues actions
        if len(clients_to_connect) == 2:
            print('got 2 clients, sending detaails to each')
            break

    # removed clients from list
    c1 = clients_to_connect.pop()
    c1_addr, c1_port = c1
    c2 = clients_to_connect.pop()
    c2_addr, c2_port = c2

    # send client info to each other
    serversocket.sendto('{} {} {}'.format(c1_addr, c1_port, port).encode(), c2)
    serversocket.sendto('{} {} {}'.format(c2_addr, c2_port, port).encode(), c1)