#! /usr/bin/env python3
# TCP Echo Client

import sys
import socket
import datetime, time
import os.path
from os import path

# get URL containing hostname and port EXAMPLE: localhost:12000/filename.html
url = sys.argv[1]

port = int(url[ url.find(":")+1 : url.find("/")])
filename = url[ url.find("/")+1 : ]
host =  url[:url.find(":")]

#print(port)
#print(host)
# Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create TCP connection to server
print("Connecting to " + host + ", " + str(port))
clientSocket.connect((host, port))


#If the is not yet cached, use a  HTTP GET operation to fetch the file name in URL
#Print out the ccontents of the file then cache the file
"""
Request linecontaining method (GET), object (from URL) and version (HTTP1.1)
Host: Same as in GET request
f-Modified-Since:Echo back value of “Last-Modified” time in HTTP GET Response
Blank line:signifies ends of header 
"""
if(path.exists("cache.txt")):
	#file is already cached, check if modified - conditional GET
	secs = os.path.getmtime("cache.txt")
	t = time.gmtime(secs)
	last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)
	last_mod_response = "If-Modified-Since: " + last_mod_time
	httpConditionGet = "GET /" + filename + "HTTP/1.1\r\n" + "Host: " + str(host) + ":"+str(port) + "\r\n" + last_mod_response +"\r\n\r\n"
	
	#print("Sending data to server: " + httpConditionGet)
	clientSocket.send(str.encode(httpConditionGet))
	dataEcho = clientSocket.recv(1024)
	decoded =  dataEcho.decode()
	
	if("304" in decoded):
		#Not modified just print out cached file
		f = open("cache.txt","r")
		print("Not modified from cache: " + f.read())
	elif("404" in decoded):
		print(decoded)
	else:
		cache = open("cache.txt","w")
		cache.write(decoded)
		print("Receive data from server: " + decoded)
	
else:
	#cache DNE - HTTP GET
	httpGET = "GET /" + filename +" HTTP/1.1\r\n" + "Host: "+ str(host) +":"+str(port)+"\r\n\r\n"
	print("Sending data to server:   " + httpGET)
	#send get request
	clientSocket.send(str.encode(httpGET))
	#reveive the server response
	dataEcho = clientSocket.recv(1024)
	# Display the decoded server response as an output
	cache = open("cache.txt", "w")
	cache_store = dataEcho.decode();
	cache.write(cache_store)
	cache.close()

	print("Receive data from server: " + cache_store) 

	#store the file in the cache 

#if the file is chached, use a conditional Get operation for the file name in URL
#If server indicate the file has not been modified since last downloaded, print out saying so (no need to print file contents)
#other wise, indicate that the file has been modified and print file, and cache the new contents
      
# Close the client socket
clientSocket.close()





