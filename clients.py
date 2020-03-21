#! usr/bin/env python3.8

import socket

# TCP: Transmission Control Protocol (connection oriented)
# UDP: User Datagram Protocol (connectionless)

target_host = 'www.google.com'
target_port = 80

""" TCP Client Example """
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((target_host, target_port))
# send some data
client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
# receive some data
response = client.recv(4096)
print(response)


""" UDP Client Example """
target_host = '127.0.0.1'
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send some data
client.sendto(b'AAABBBCCC', (target_host, target_port))
# receive some data
data, addr = client.recvfrom(4096)
print(data)
