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

# loop forever listening for incoming UDP messages
while True:
	
	# Receive and print the client data from "data" socket
	data, address = serverSocket.recvfrom(1024)
	msgType , sequenceNumber = struct.unpack('!ii' , data)
	#print("type: " + str(msgType) + " sequence: " + str(sequenceNumber))
	randy = random.randint(1,10)
	
	if randy < 4:
		#No response, wait to timeout
		print("Message with sequence number " + str(sequenceNumber) + " timed out")
		time.sleep(1)
	else:
		#respond
		print("Responding to ping request with sequence number " + str(sequenceNumber))
		serverSocket.sendto(struct.pack('!ii',2, sequenceNumber), (address))
	
  
	    
	
