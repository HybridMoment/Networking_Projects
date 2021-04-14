#! /usr/bin/env python3
# TCP Echo Server

import sys
import socket
import datetime, time
import os.path
from os import path

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a TCP "welcoming" socket. Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
# Listen for incoming connection requests
serverSocket.listen(1)

print('The server is ready to receive on port:  ' + str(serverPort) + '\n')
# loop forever listening for incoming connection requests on "welcoming" socket

while True:
    # Accept incoming connection requests; allocate a new socket for data communication
    connectionSocket, address = serverSocket.accept()
    print("Socket created for client " + address[0] + ", " + str(address[1]))
    
    #http request to parse to get filename and etc
    httpRequest = connectionSocket.recv(1024)
    #print(httpRequest.decode())
    request = httpRequest.decode()
    #get filename
    filename = request[request.find("/")+1 :request.find(".")] + ".html"

    req_split = request.split("\r\n")
    #print(filename)
    #response to send back
    """
    blankline = "\r\n"
    response = "HTTP/1.1 200 OK" + blankline
    t = datetime.datetime.now(datetime.timezone.utc)
    date = t.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n")
    date_response = "Date: " + date
    
    secs = os.path.getmtime(filename)
    t = time.gmtime(secs)
    last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)
    last_mod_response = "Last-Modified: " + last_mod_time
    file_size = path.getsize(filename)
    content_type = "text/html; charset=UTF-8\r\n"
	"""
    #get file contents for body
    """
    with open(filename , "r") as file_content:
    	content = file_content.read()

    print("Print request : " + request)
    """
    if(path.exists(filename) == False):
    	response = "HTTP/1.1 404 Not Found\r\n"
    	t = datetime.datetime.now(datetime.timezone.utc)
    	date = t.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n")
    	date_response = "Date: " + date
    	httpResponse = str.encode(response + date_response + "\r\n")
    else:
    	if_modified = req_split[2]
    	token = if_modified[:if_modified.find(":")]
    	#print("printing token : " + token)
    	with open(filename, "r") as file_content:
    		content = file_content.read()
    	print("Printing Request: " + request)

    	if("If-Modified-Since" == token):
            #check if file modified - Client has cache
            if( path.exists(filename) == False):
                #filname DNE - 404 response
                response = "HTTP/1.1 404 Not Found\r\n"
                t = datetime.datetime.now(datetime.timezone.utc)
                date = t.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n")
                date_response = "Date: " + date
                httpResponse = str.encode(response + date_response + "\r\n")
            else:
                #check if modified compare the cached time with file time
                #cache file time 
                cache_secs = os.path.getmtime("cache.txt")
                cache_time = time.gmtime(cache_secs)
                #stored file time
                secs = os.path.getmtime(filename)
                file_time = time.gmtime(secs)

                #compare time
                if(file_time > cache_time):
                    #file was modified
                    response = "HTTP/1.1 200 OK\r\n"
                    t = datetime.datetime.now(datetime.timezone.utc)
                    date = t.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n")
                    date_response = "Date: " + date
                    secs = os.path.getmtime(filename)
                    t = time.gmtime(secs)
                    last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)
                    last_mod_response = "Last-Modified: "+ last_mod_time
                    file_size = path.getsize(filename)
                    content_type = "text/html; charset=UTF-8\r\n"
                    httpResponse = str.encode(response + date_response + last_mod_response+ "Content-Length: "+ str(file_size) + "\r\n" +content_type + content)
                else:
                    #304
                    response = "HTTP/1.1 304 Not Modified\r\n"
                    secs = os.path.getmtime(filename)
                    t = time.gmtime(secs)
                    last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)
                    date_response = "Date: "+ last_mod_time + "\r\n"
                    httpResponse = str.encode(response + date_response + "\r\n")
    	else:
            #not cached send back file
            blankline = "\r\n"
            response = "HTTP/1.1 200 OK" + blankline
            t = datetime.datetime.now(datetime.timezone.utc)
            date = t.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n")
            date_response = "Date: " + date

            secs = os.path.getmtime(filename)
            t = time.gmtime(secs)
            last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)
            last_mod_response = "Last-Modified: " + last_mod_time
            file_size = path.getsize(filename)
            content_type = "text/html; charset=UTF-8\r\n"

            httpResponse = str.encode(response + date_response + last_mod_response + "Content-Length: " +str(file_size) + blankline +content_type + content)

    """
    #response to send back
    blankline = "\r\n"
    response = "HTTP/1.1 200 OK" + blankline
    t = datetime.datetime.now(datetime.timezone.utc)
    date = t.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n")
    date_response = "Date: " + date
    
    secs = os.path.getmtime(filename.txt)
    t = time.getmtime(secs)
    last_mod_time = t.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n")
    last_mod_response = "Last-Modified: " + last_mod_time
    file_size = path.getize(filename)
    content_type = "text/html; charset=UTF-8\r\n"

    #get file contents for body
    with open(filename , "r") as file_content:
    	content = file_content.read()
	"""
    #httpResponse = str.encode(response + date_response + last_mod_response + "Content-Length: " +file_size + blankline +content_type + content)

    #serverSocket.sendto( httpRespone , address)



    #Listen for incoming HTTP get and Condition GET requests from on or more http clients
    #- in the case of a GET request:
    #- read the named file and return a HTTP GET response, including the last modified header field

    #-inthe case of a Condition Get:
    #- if the file has not been modified since that indicated by if-modified-since, return 304
    #- if the file has been modifiedm return the file contents as in step 2

    #in the case of the named file DNE, return 404

    # Receive and print the client data in bytes from "data" socket
    #data = connectionSocket.recv(dataLen).decode()
    #print("Data from client: " + data)

    # Echo back to client
    connectionSocket.send(httpResponse)
	
        
