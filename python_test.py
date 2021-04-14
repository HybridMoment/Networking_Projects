#python test
import struct 
import sys
import socket
import time 

host = sys.argv[1]
port = int(sys.argv[2])
look_up = sys.argv[3]


# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set timeout to 1 second
clientsocket.settimeout(1)
print("Pinging " + host + ", " + str(port) + ":")

lol = str(sys.argv[3])

lol_to_bytes = lol.encode("utf-8")

fmt = '{}s'.format(len(lol))
print(lol)

clientsocket.sendto(struct.pack(fmt, lol_to_bytes),(host, port))

#response
serverMsg , address = clientsocket.recvfrom(1024)
fmt =  '{}s'.format(len(serverMsg))
response = struct.unpack(fmt, serverMsg) 

response_str = str(response)
value = response_str[3:-3]
print(value)

print(response)

