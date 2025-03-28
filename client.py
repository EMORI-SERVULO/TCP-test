import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
while True:
    try:

        # Send data
        cliente_message =input("Input message!:")
        sock.sendall(cliente_message.encode())

        # Look for the response
        res = sock.recv(1024)
        print(f" answer by server: {res.decode()}")
        if(res.decode() == "DESCONEXION"):
            break

    finally:
        print('closing socket')
        sock.close()