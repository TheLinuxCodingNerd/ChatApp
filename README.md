# Python Chat Application

This is a simple terminal-based chat application using Python's `socket` and `threading` libraries. It supports real-time communication between multiple clients over a TCP connection. The server broadcasts all messages to all connected clients and supports user identification via usernames.

## Features

- Multi-client support via threading  
- Message broadcasting  
- Username prompt for client identification  
- Real-time message relay  
- Simple and clean terminal interface

## Files

- `server.py`: Runs the server that accepts client connections and broadcasts messages.
- `Client.py`: Runs the client that connects to the server and allows message input/output.

## Setup Instructions

### 1. Start the Server

Run the following command in your terminal:

```bash
python server.py
```

The server will listen for incoming client connections on the specified host and port.

### 2. Start a Client

In a separate terminal window or machine, run:

```bash
python Client.py
```

Enter a username when prompted. You can run multiple clients simultaneously.

## Requirements

- Python 3.x
- No external dependencies; uses built-in libraries only.

## Notes

- Ensure all clients connect to the same IP address and port as the server.
- This application is for educational or small LAN usage. It does not include encryption or advanced error handling.