import socket
import threading
# Define host and port for the server
HOST = '127.0.0.1'
PORT = 2221
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the specified host and port
server_socket.bind((HOST, PORT))
# Listen for incoming connections
server_socket.listen()
# List to store all connected clients
clients = []
# Function to handle incoming messages from clients
def handle_messages(client_socket, client_address):
    while True:
        try:
            # Receive a message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                # Broadcast the message to all connected clients
                broadcast_message(message, client_address)
            else:
                # If the message is empty, remove the client from the list of connected clients
                remove_client(client_socket)
        except:
            # If there is an error while receiving the message, remove the client from the list of connected clients
            remove_client(client_socket)
            break
# Function to broadcast a message to all connected clients
def broadcast_message(message, sender_address):
    for client in clients:
        # Send the message to all connected clients except the sender
        if client != sender_address:
            client.sendall(message.encode('utf-8'))
# Function to remove a client from the list of connected clients
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()
# Function to accept incoming connections and start a thread to handle each connection
def accept_connections():
    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        # Add the client to the list of connected clients
        clients.append(client_socket)
        # Start a new thread to handle incoming messages from the client
        thread = threading.Thread(target=handle_messages, args=(client_socket, client_address))
        thread.start()
# Start accepting incoming connections
accept_connections()