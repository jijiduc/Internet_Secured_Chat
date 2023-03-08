"""""
C'est le fichier de connexion TCP au server
"""""
import socket
import functions

host_ip, server_port = "vlbelintrocrypto.hevs.ch", 6000
data = functions.encode()

# Initialize a TCP client socket using SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#try:
# Establish connection to TCP server and exchange data
tcp_client.connect((host_ip, server_port))
tcp_client.sendall(data)
print("Bytes Sent:     {}".format(data))

# Read data from the TCP server and close the connection
while True :
    received = tcp_client.recv(1024)

    print("Bytes Received: {}".format(received.decode()))

#finally:
#    tcp_client.close()

