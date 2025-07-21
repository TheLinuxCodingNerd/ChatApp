import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

# Create and bind the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []
usernames = {}
lock = threading.Lock()

print(f"Server started on {HOST}:{PORT}. Waiting for connections...")

# Broadcast message to all connected clients except the sender
def broadcast(message, sender_conn=None):
    with lock:
        for client in clients:
            if client != sender_conn:
                try:
                    client.sendall(message.encode())
                except:
                    client.close()
                    clients.remove(client)

# Handle incoming client connection
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    conn.sendall("Enter your username: ".encode())
    username = conn.recv(1024).decode().strip()

    with lock:
        clients.append(conn)
        usernames[conn] = username
    broadcast(f"{username} has joined the chat.", conn)

    try:
        while True:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"{username}: {message}")
            broadcast(f"{username}: {message}", conn)
    except:
        pass
    finally:
        with lock:
            clients.remove(conn)
            broadcast(f"{username} has left the chat.")
            del usernames[conn]
        conn.close()

# Accept new connections
while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()