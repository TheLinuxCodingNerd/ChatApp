# 💬 ChatApp – Terminal-Based Python Chatroom

A minimal yet functional chatroom built with Python's `socket` and `threading` libraries. Run it in your terminal to simulate a multi-user chat experience. Designed for local or LAN testing, education, and fun experimentation with networking basics.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/github/license/TheLinuxCodingNerd/ChatApp)

---

## ✨ Features

- ✅ Real-time terminal-based messaging  
- 👥 Multi-client support using threading  
- 🧑 Username prompt for identification  
- 📡 Message broadcasting  
- 📟 Lightweight and dependency-free  

---

## 📂 Project Structure

```plaintext
📦 ChatApp
 ┣ 📜 server.py   # Starts the server and handles all clients
 ┗ 📜 Client.py   # Connects to the server and handles user input/output
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/TheLinuxCodingNerd/ChatApp.git
cd ChatApp
```

### 2. Start the Server

```bash
python server.py
```

The server will wait for incoming connections on the configured host and port.

### 3. Launch Clients

In separate terminal windows or machines:

```bash
python Client.py
```

Each client will be prompted to enter a username before joining the chat.

---

## ⚙️ Requirements

- Python 3.x  
- No external dependencies (uses built-in libraries only)

---

## 🛠️ How It Works

- The server listens for client connections and starts a new thread for each.
- Clients send messages to the server, which are then broadcasted to all other clients.
- Each client shows messages in real-time using input/output threads.

---

## 📸 Screenshots (Coming Soon)

_Contributions welcome! Submit a PR with demo screenshots!_

---

## 🧠 Educational Value

This is a great starter project to learn about:

- Socket programming  
- Multi-threaded applications  
- Server-client architecture  
- Command-line interfaces

---

## 📄 License

MIT License © 2025 [TheLinuxCodingNerd](https://github.com/TheLinuxCodingNerd)