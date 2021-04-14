#! /usr/bin/env python3
# Echo Server
# Eric Rogers - er272 - 001
import sys
import socket
import struct
import time
import random
# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print("The server is ready to receive on port:  " + str(serverPort) + "\n")
dns_Directory = {}
# loop forever listening for incoming UDP messages

with open("dns-master.txt") as f:
	for line in f:
		line_split = line.split()
		#Get Key and format 
		key = line_split[0]
		key.strip()
		#Get Value and format
		print(key)
		value = line_split[-1]
		value.rstrip()
		value = str(value)
		print(value)
		dns_Directory[key] = value


while True:
	
	# Receive and print the client data from "data" socket
	data, address = serverSocket.recvfrom(1024)
	look_up = struct.unpack('{}s'.format(len(data)) , data)
	
	look_up_str = str(look_up)
	key = look_up_str[3:-3]
	print(key)

	value = dns_Directory.get(key)
	if value == None:
		print("WTF")

	else:
		print(value)
		value_str = str(value)
		response_bytes = value_str.encode("utf-8")
		fmt = '{}s'.format(len(response_bytes))
		serverSocket.sendto(struct.pack(fmt, response_bytes) , (address))  


	

	
 