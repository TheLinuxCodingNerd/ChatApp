import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

# Create socket and connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Function to continuously receive messages from server
def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                print("Disconnected from server.")
                break
            print(data)
        except:
            print("An error occurred while receiving messages.")
            break

# Start a thread to handle incoming messages
threading.Thread(target=receive_messages, daemon=True).start()

# Main loop for sending messages
try:
    while True:
        msg = input()
        if msg.strip() == "":
            continue
        client_socket.sendall(msg.encode())
except KeyboardInterrupt:
    print("\nDisconnected by user.")
finally:
    client_socket.close()