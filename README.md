# 🖥️ Network-Controlled Custom CMD Panel (TCP Sockets)

A sophisticated **client-server command execution system** built with **Python TCP sockets**, providing **remote command execution with a professional GUI, real-time monitoring, and multi-client support**.  
Demonstrates practical networking concepts, reliable message protocols, and scalable architecture design.

**Status:** ✅ Fully Functional | **Version:** 1.0 | **Python:** 3.6+

---

## 📌 Quick Overview

This project implements a complete network-based command execution framework where:
- **Clients** connect via TCP and send commands through a modern GUI interface
- **Server** validates, processes, and returns command results
- **Communication** uses a robust length-prefixed JSON protocol for reliability
- **Architecture** supports concurrent multi-client connections

Perfect for understanding real-world networking applications, socket programming, and client-server design patterns.

---

## 🚀 Quick Start

### Prerequisites
```bash
python --version  # Python 3.6 or higher
pip install --upgrade pip
```

### Installation
```bash
# Clone the repository
git clone https://github.com/hamzaali-712/Network-Controlled-Custom-CMD-Panel-Using-TCP-Sockets.git
cd Network-Controlled-Custom-CMD-Panel-Using-TCP-Sockets

# No external dependencies required! (uses only Python standard library)
```

### Run the Client
```bash
python cmd_client_gui.py
```

**Expected Output:**
- GUI window opens with black terminal interface
- Connects to server automatically
- Shows "Connected to server." in the output panel

---

## ⚙️ Features

| Feature | Description |
|---------|-------------|
| 🔗 **TCP Socket Communication** | Reliable, ordered message delivery with connection verification |
| 🖥️ **GUI Terminal Interface** | Modern Tkinter-based terminal emulation (Consolas font, black/white theme) |
| 📤 **Remote Command Execution** | Execute system commands on server from client GUI |
| 👥 **Multi-Client Support** | Server handles multiple simultaneous client connections |
| 📡 **Real-Time Response** | Instant feedback with scrollable output history |
| 🔄 **Threaded I/O** | Non-blocking network operations with responsive GUI |
| 📋 **Structured Protocol** | Length-prefixed JSON for guaranteed message integrity |
| 🎯 **Command Parsing** | Automatic separation of command name and arguments |
| 📊 **Connection Status** | Live indicator showing server connection state |  

---

## 🏗️ Project Structure

```
Network-Controlled-Custom-CMD-Panel-Using-TCP-Sockets/
├── cmd_client_gui.py          # ⭐ Main client application
├── python                      # Server executable/script
├── README.md                   # This file
├── sample.txt                  # Test data file
├── .gitignore                  # Git configuration
└── .git/                       # Repository history
```

---

## 🔧 Configuration

### Modify Server Connection (in `cmd_client_gui.py`)

```python
# Line 5-6: Update these constants for your environment
SERVER_HOST = "10.120.12.12"   # Change to your server IP
SERVER_PORT = 50001             # Change if server uses different port
PROMPT = "mycmd> "              # Customize prompt text
```

### Example Configurations
```python
# Local machine testing
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 50001

# Local network
SERVER_HOST = "192.168.1.100"
SERVER_PORT = 50001

# Remote server
SERVER_HOST = "your.server.com"
SERVER_PORT = 50001
```

---

## 💻 Usage Guide

### Starting the Client

1. **Launch GUI:**
   ```bash
   python cmd_client_gui.py
   ```

2. **Wait for Connection:**
   - Status bar shows "Connected" when server is ready
   - Connection message appears in output area

3. **Send Commands:**
   - Type command in the input field at bottom
   - Press `Enter` to execute
   - Results appear in output area above

### Example Commands
```
mycmd> GET_STATUS
mycmd> LIST_FILES
mycmd> EXECUTE_COMMAND dir
mycmd> SEND_TEXT_FILE sample.txt
mycmd> PING
```

---

## 🌐 Network Protocol

### Communication Flow

```
CLIENT                              SERVER
  │                                   │
  ├─ TCP Connect (10.120.12.12:50001)─>
  │                                   │
  │<─ Connection Accepted ────────────┤
  │                                   │
  ├─ {"cmd":"LIST","args":[]} ─────>
  │  (4-byte length + JSON)           │
  │                                   ├─ Process Command
  │                                   │
  │<─ {"output":"[...]"} ────────────┤
  │  (4-byte length + JSON)           │
  │                                   │
```

### Message Format

**Sending (Client → Server):**
```json
{
  "cmd": "COMMAND_NAME",
  "args": ["arg1", "arg2", "arg3"]
}
```

**Receiving (Server → Client):**
```json
{
  "output": "command result or error message"
}
```

**Protocol Details:**
- **Length Header:** 4-byte unsigned integer (network byte order: `!I`)
- **Data:** UTF-8 encoded JSON string
- **Format:** `[4-byte length][JSON data]`

---

## 🛠️ Technologies & Stack

| Layer | Technology |
|-------|-------------|
| **Language** | Python 3.6+ |
| **GUI Framework** | Tkinter (built-in, no installation needed) |
| **Networking** | Socket module (TCP/IP) |
| **Data Format** | JSON (built-in `json` module) |
| **Concurrency** | Threading module (daemon threads) |
| **Protocols** | Custom length-prefixed JSON over TCP |

### Why This Stack?

| Choice | Reason |
|--------|--------|
| **Python** | Easy to learn, excellent for networking demos, large standard library |
| **Tkinter** | Built-in, cross-platform, sufficient for this application |
| **TCP Sockets** | Reliable delivery, ordered messages, perfect for commands |
| **JSON** | Human-readable, language-agnostic, easy to parse |
| **Threading** | Non-blocking I/O keeps GUI responsive |  

---

## � Learning Outcomes

- ✅ **Socket Programming** — Understanding TCP/IP fundamentals and socket operations
- ✅ **Client-Server Architecture** — Designing distributed systems
- ✅ **Network Protocols** — Creating reliable message formats with length-prefixing
- ✅ **GUI Development** — Building user interfaces with Tkinter
- ✅ **Concurrent Programming** — Managing multiple threads safely
- ✅ **JSON Serialization** — Encoding/decoding structured data
- ✅ **Error Handling** — Connection errors, timeouts, malformed messages
- ✅ **Real-World Design** — Practical considerations in networked applications  

---

## � Security Considerations

> ⚠️ **This is an educational project. For production use, add:**

- [ ] **Authentication** — Username/password or token-based auth
- [ ] **Authorization** — User permission levels for commands
- [ ] **Encryption** — SSL/TLS for transport layer security
- [ ] **Logging** — Audit trail of executed commands
- [ ] **Input Validation** — Sanitize and validate all commands
- [ ] **Rate Limiting** — Prevent brute force and DoS attacks
- [ ] **Command Whitelist** — Only allow specific approved commands

---

## ⚙️ System Requirements

| Requirement | Specification |
|-------------|----------------|
| **OS** | Windows, macOS, Linux |
| **Python** | 3.6 or higher |
| **RAM** | Minimum 50MB (typically < 20MB) |
| **Network** | TCP/IP connectivity to server |
| **GUI** | Display with 800x450+ resolution |
| **Permissions** | Execute Python scripts |

---

## 🐛 Troubleshooting

### Issue: Connection Refused
**Problem:** "Connection failed: [Errno 111] Connection refused"  
**Solution:**
- Verify server is running: `ping 10.120.12.12`
- Check SERVER_HOST and SERVER_PORT are correct
- Ensure firewall allows TCP port 50001

### Issue: GUI Not Responding
**Problem:** Window freezes when sending command  
**Solution:**
- This is normal while waiting for server response
- Try clicking in the window — it's still responsive
- Check server logs for errors

### Issue: "ModuleNotFoundError: No module named 'tkinter'"
**Problem:** Tkinter not installed (Linux)  
**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS (usually pre-installed)
brew install python-tk
```

### Issue: Port Already in Use
**Problem:** "Address already in use" error  
**Solution:**
- Change SERVER_PORT to different number (e.g., 50002)
- Or kill existing Python process: `killall python`

---

## 📈 Future Enhancements

- [x] ✅ **GUI Interface** — Implemented with Tkinter
- [ ] 🔐 **Authentication Layer** — Username/password or token-based
- [ ] 📊 **Logging & Reporting** — Command execution history
- [ ] 🔒 **SSL/TLS Encryption** — Secure communication channel
- [ ] 🌐 **Web Dashboard** — Flask/FastAPI based monitoring panel
- [ ] 📱 **Mobile Client** — Android/iOS app
- [ ] 💾 **Database Integration** — Store command logs in MongoDB/MySQL
- [ ] 🧪 **Unit Tests** — Comprehensive test suite
- [ ] 📈 **Performance Metrics** — Response time, throughput monitoring
- [ ] 🐳 **Docker Support** — Containerized deployment

---

## 📚 References & Resources

### TCP/IP & Socket Programming
- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- [TCP vs UDP comparison](https://www.geeksforgeeks.org/differences-between-tcp-and-udp/)
- [Socket programming tutorial](https://realpython.com/python-sockets/)

### Tkinter GUI
- [Tkinter documentation](https://docs.python.org/3/library/tkinter.html)
- [Tkinter tutorial](https://www.tutorialspoint.com/python/python_gui_programming.htm)

### Best Practices
- [Network protocol design](https://www.ietf.org/rfc/)
- [Python code style - PEP 8](https://pep8.org/)

---

## 📄 License

This project is provided as-is for educational purposes.  
Feel free to fork, modify, and distribute.  

---

## 💡 About the Author

**Hamza Ali & Akif Naveed**  
🎓 Bachelor of Science in Computer Science (Software Engineering)  
&nbsp;&nbsp;&nbsp;&nbsp;COMSATS University Islamabad, Wah Campus  

💻 **Interests:**
- Network Programming & Cybersecurity
- Artificial Intelligence & Machine Learning
- Data Science & Cloud Computing
- Software Architecture & Design Patterns

🌐 **Connect with me:**
- [LinkedIn](https://www.linkedin.com/in/hamza-ali-893a4a353)
- [GitHub](https://github.com/hamzaali-712)
- Email: hamzaali712@gmail.com

---

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome!  
Please feel free to:
- Open an issue for bugs or feature requests
- Submit pull requests with improvements
- Share this project if you found it helpful

---

⭐ **If you found this project helpful, please give it a star!**  
Your support motivates continuous improvement and helps others discover the project.

---

**Last Updated:** May 2026  
**Status:** Production Ready | **Version:** 1.0
