#! /usr/bin/env python3
# DNS PROJECT
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

#DNS DIRECTORY FOR KEY VALUE STORES 
dns_Directory = {}
#Read in the DNS master text and store into a dictionary for look up
with open("dns-master.txt") as f:
	for line in f:
		line_split = line.split()
		#Get Key and format 
		key = line_split[0]
		key.strip()
		#Get Value and format
		value = line_split[-1]
		value.rstrip()
		value = str(value)
		#dns store
		dns_Directory[key] = value


# loop forever listening for incoming UDP messages
while True:
	
	# Receive and print the client data from "data" socket
	data, address = serverSocket.recvfrom(1024)
	look_up = struct.unpack('{}s'.format(len(data)) , data)
	look_up_str = str(look_up)
	key = look_up_str[3:-3]

	#print("Looking up key: {}".format(key))
	value = dns_Directory.get(key)
	print(key)
	print(value)

	if value == None:
		#ERROR NOT IN DNS DIRECTORY 
		#Send back Error
		error = "error"
		serverSocket.sendto(struct.pack('{}s'.format(len(error)), error.encode("utf-8") ), (address))
	

	else:
		#Send back RESPONSE
		value_str = str(value)
		response_bytes = value_str.encode('utf-8')
		serverSocket.sendto(struct.pack('{}s'.format(len(response_bytes)), response_bytes), (address))
	
	
  
	    
	
