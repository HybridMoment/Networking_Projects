#! /usr/bin/env python3
# DNS PROJECT
# Eric Rogers - er272 - 001
import sys
import socket
import struct 
import time

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
look_up = sys.argv[3]

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set timeout to 1 second
clientsocket.settimeout(1)
print("Pinging " + host + ", " + str(port) + ":")
look_up_bytes = look_up.encode('utf-8')
fmt = "{}s".format(len(look_up_bytes))

try:

	#sending msg to server
	
	clientsocket.sendto(struct.pack(fmt, look_up_bytes),(host, port))
	# Receive the server response
	serverMsg , address= clientsocket.recvfrom(1024)
	response = struct.unpack("{}s".format(len(serverMsg)), serverMsg)

	response_str = str(response)
	value = response_str[3:-3]

	question_len = len(look_up)

	print("Received Response from {} ,{}".format(host, port))
	print("Return code : {}".format(2))
	print("Msg ID: {}".format(5))
	print("Question Length : {}".format(question_len))
	print("Question: {}".format(look_up))
	print("Answer: {} {}".format(look_up, value))

except Exception as e:
	
	print("Error connecting to server")
	print(e)

	for i in range(2):
		# try two more times
		try:
			clientsocket.sendto(struct.pack(fmt, look_up_bytes),(host, port))
			# Receive the server response
			serverMsg, address = clientsocket.recvfrom(1024)
			response = struct.unpack('{}s'.format(len(serverMsg)), serverMsg)
		
			print("Received Response from {}, {}".format(host,port))
			print("Return code : {}".format(2))
			print("Msg ID: {}".format(5))
			print("Question Length : {}".format(len(look_up)))
			print("Question: {}".format(look_up))
			print("Answer: {} {}".format(look_up, response))

		except Exception as e:
			print("Error connecting to server")
			print(e)

#Close the client socket
clientsocket.close()


'''
TODO: Test case 1: Client sends echo request to IP address and port specified on command-line 
	 
	  Test case 2: Client sends 3 echo requests with timeout

	  Both Test cases: Client prints message as specified when sends message
	  	- Client prints message as specified when reveives message or timeout

'''