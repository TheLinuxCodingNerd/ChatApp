# 💬 Python Chat Application

A simple, terminal-based multi-client chatroom built with Python's `socket` and `threading` libraries. Perfect for learning about networking, sockets, and multithreading in Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## ✨ Features

- ✅ Real-time messaging
- 👥 Multi-user support via threading
- 🧑 Username prompt for easy identification
- 🔁 Message broadcasting to all connected users
- 🖥️ Clean and simple CLI interface

---

## 📁 Project Structure

```plaintext
📦 ChatApp
 ┣ 📜 server.py   # Server to manage client connections and message broadcast
 ┗ 📜 Client.py   # Client that connects to the server and sends/receives messages
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chat-app.git
cd chat-app
```

### 2. Run the Server

```bash
python server.py
```

The server will start listening for client connections on a specified IP and port.

### 3. Run a Client

In another terminal window:

```bash
python Client.py
```

Enter a username when prompted. You can run this command on multiple terminals/machines to simulate different clients.

---

## ⚙️ Requirements

- Python 3.x
- No external libraries required (uses built-in `socket` and `threading`)

---

## 📌 Notes

- All clients must connect to the same host and port defined in `server.py`
- Designed for local or LAN use
- Does **not** support encryption or authentication – not for production

---

## 📷 Screenshots

> Coming soon — terminal screenshots of the chat in action!

---

## 🧠 Learning Goals

This project is a great starting point to understand:

- Network programming with sockets
- Multithreading in Python
- Basic server/client architecture
- CLI app interaction

---

## 📄 License

MIT License © 2025 Your Name