#!/usr/bin/python3

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket


# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)


while True:
    print ('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print ('HTTP request received:')
    print (recvSocket.recv(1024))

    """ PONER UN TEXTO """
    recvSocket.send(
            bytes(
               "HTTP/1.1 200 OK\r\n\r\n" +
               "<html><body><h1>Hello World!</h1></body></html>" +
               "\r\n",
               "utf-8"
            )
    )

    """ PONER EN EL NAVEGADOR UNA IMAGEN DAD UNA URL"""
#    recvSocket.send(
#            bytes(
#               "HTTP/1.1 200 OK\r\n\r\n" +
#               "<html><body><img src='http://images.khinsider.com/KINGDOM%20HEARTS%202.8/Screenshots/4Gamer%20-%20November%2003%202015/13.jpg'/></body></html>" +
#               "\r\n",
#               "utf-8"
#            )
#    )

    """ PONER EN EL NAVEGADOR UN ENLACE HACIA OTRA PAGINA"""
#    recvSocket.send(
#                    bytes(
#                        "HTTP/1.1 200 OK\r\n\r\n" +
#                        "<html><body><a href='http://www.urjc.es'>" +
#                        "www.urjc.es</a></body></html>",
#                        "utf-8"
#                    )
#    )
    recvSocket.close()
