#! /usr/bin/env python3
# Echo Client
# Eric Rogers - er272 - 001
import sys
import socket
import struct 
import time
# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
#count = int(sys.argv[3])
# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set timeout to 1 second
clientsocket.settimeout(1)
print("Pinging " + host + ", " + str(port) + ":")

for x in range(1,11):
	
	try:

		#sending msg to server
		timeSent = time.time()
		clientsocket.sendto(struct.pack('!ii',1, x),(host, port))
		# Receive the server response
		serverMsg, address = clientsocket.recvfrom(1024)
		timeRec = time.time()
		msgType, sequenceNumber = struct.unpack('!ii', serverMsg)

		print("Ping message number " + str(sequenceNumber) + "RTT: " + str(timeRec-timeSent))

	except Exception as e:
		print(e)
		print("Ping message number " + str(x) + " timed out")

#Close the client socket
clientsocket.close()


'''
TODO: Test case 1: Client sends echo request to IP address and port specified on command-line 
	 
	  Test case 2: Client sends 3 echo requests with timeout

	  Both Test cases: Client prints message as specified when sends message
	  	- Client prints message as specified when reveives message or timeout

'''