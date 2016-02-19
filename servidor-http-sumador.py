#!/usr/bin/python

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

pnum= None
try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        peticion= recvSocket.recv(1024)
        num=peticion.split()[1][1:]
        if pnum == None:
            pnum= num
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
               "<html><body><h1>Primer Sumando: " + pnum+"</h1></body></html>"
                  +"\r\n")
        else:
              try:
                  suma = int(pnum)+ int(num)

                  recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1> Suma: "+str(pnum)+" + " + str(num)+"= "+str(suma)+"</h1></body></html>"
                        +"\r\n")
                  pnum = None
              except ValueError:
                  recvSocket.send("HTTP/1.1 400 Error..\r\n\r\n" +
                    "<html><body><h1> Not a number ...</h1></body></html>"
                        +"\r\n")
                  pnum = None
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
