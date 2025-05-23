import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"received by client: {message}")
            
            if message!="DESCONEXION":
                res = message.upper()
                print('sending data back to the client')
                connection.sendall(res.encode())
            else:
                connection.sendall(message.encode())
                break

    finally:
        # Clean up the connection
        connection.close()