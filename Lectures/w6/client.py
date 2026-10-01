import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# target machine
client_socket.connect(("localhost", 5002))

message = "Hello!"
client_socket.sendall(message.encode())

response = client_socket.recv(2048).decode()
print(response)

client_socket.close()
