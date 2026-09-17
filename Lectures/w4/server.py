import socket, time, threading

class Worker(threading.Thread):

    def run(self):
        time.sleep(10)
        print("Thread is finished")

# configure the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# be listening for connection request
server_socket.bind(("localhost", 5002))
server_socket.listen(1)

# loop that listens for three messages
while True:
    print("Waiting for client...")
    client, address = server_socket.accept()
    message = client.recv(2048).decode()

    print(message)

    w = Worker()

    w.start()
    
    client.sendall("Hello back from the server!".encode())
    client.close()

server_socket.close()
