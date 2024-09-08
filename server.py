import socket
import threading
import json

# Server settings
HOST = '127.0.0.1'  # Localhost
PORT = 3500
# Read port from config.json
try:
    with open("config.json", "r") as file:
        config = json.load(file)
        PORT = config.get("port", 3500)  # Default port if not found
except Exception as e:
    print(e)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Broadcast messages to all clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            # Handle broken connections
            client.close()
            clients.remove(client)

# Handle client connection
def handle_client(client):
    while True:
        try:
            # Receive and broadcast messages
            message = client.recv(1024)
            if not message:
                # Connection was closed
                break
            broadcast(message)
        except (ConnectionResetError, socket.error):
            # Handle disconnection or socket error
            break

    # Remove and close client
    index = clients.index(client)
    clients.remove(client)
    client.close()
    nickname = nicknames[index]
    broadcast(f'{nickname} has left the chat!'.encode('utf-8'))
    nicknames.remove(nickname)

# Receive clients
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("Server: Enter your nickname: ".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'Server: {nickname} joined the chat!'.encode('utf-8'))
        client.send('Client: Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is Run")
receive()