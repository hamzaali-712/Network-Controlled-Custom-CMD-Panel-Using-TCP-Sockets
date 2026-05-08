# cmd_server.py
import socket, threading, json, struct, datetime, os
try:
    import psutil
except:
    psutil = None

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 50000

# Command execution logs
COMMAND_LOGS = []

# ---------------- Utility Functions ----------------
def send_msg(conn, obj):
    data = json.dumps(obj).encode('utf-8')
    conn.sendall(struct.pack('!I', len(data)) + data)

def recv_msg(conn):
    raw = conn.recv(4)
    if not raw: return None
    length = struct.unpack('!I', raw)[0]
    data = b''
    while len(data) < length:
        chunk = conn.recv(length - len(data))
        if not chunk: return None
        data += chunk
    return json.loads(data.decode('utf-8'))

# ---------------- Command Handlers ----------------
def handle_echo(args):
    return {"status":"OK", "output":" ".join(args)}

def handle_ping(args):
    target = args[0] if args else "localhost"
    return {"status":"OK", "output":f"Simulated ping to {target}: 12ms"}

def handle_time(args):
    return {"status":"OK", "output":datetime.datetime.now().isoformat()}

def handle_sysinfo(args):
    info = {"OS":"PyOS 1.0", "CPU":"N/A", "RAM":"N/A", "Uptime":"N/A"}
    if psutil:
        info["CPU"] = f"{psutil.cpu_percent()}%"
        info["RAM"] = f"{psutil.virtual_memory().percent}%"
    uptime_sec = (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(__file__))).seconds
    info["Uptime"] = f"{uptime_sec} sec"
    return {"status":"OK", "output":info}

def handle_send_text_file(args):
    filename = args[0] if args else "sample.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        return {"status":"OK", "output": text}
    except Exception as e:
        return {"status":"ERROR", "output":"", "error": str(e)}

def handle_help(args):
    commands = list(COMMANDS.keys())
    return {"status":"OK", "output":", ".join(commands)}

def handle_quit(args):
    return {"status":"OK", "output":"Goodbye!"}

def handle_joke(args):
    return {"status":"OK", "output":"Why don’t programmers like nature? Too many bugs."}

def handle_quote(args):
    return {"status":"OK", "output":"Success is not final. Failure is not fatal."}

def handle_calc(args):
    expr = " ".join(args)
    try:
        # safe eval for simple math
        allowed_chars = "0123456789+-*/(). "
        if not all(c in allowed_chars for c in expr):
            raise ValueError("Invalid characters")
        result = eval(expr)
        return {"status":"OK", "output":str(result)}
    except Exception as e:
        return {"status":"ERROR", "output":"", "error": str(e)}

def handle_random_fact(args):
    facts = ["Python was named after a comedy show.",
            "TCP ensures reliable communication.",
            "Networking is fun!"]
    import random
    return {"status":"OK", "output":random.choice(facts)}

def handle_sys_logs(args):
    return {"status":"OK", "output":COMMAND_LOGS[-5:]}

# ---------------- Command Registry ----------------
COMMANDS = {
    "ECHO": handle_echo,
    "PING": handle_ping,
    "TIME": handle_time,
    "SYSINFO": handle_sysinfo,
    "SEND_TEXT_FILE": handle_send_text_file,
    "HELP": handle_help,
    "QUIT": handle_quit,
    "JOKE": handle_joke,
    "QUOTE": handle_quote,
    "CALC": handle_calc,
    "RANDOM_FACT": handle_random_fact,
    "SYS_LOGS": handle_sys_logs
}

# ---------------- Client Handler ----------------
def handle_client(conn, addr):
    print(f"[+] Client connected: {addr}")
    try:
        while True:
            msg = recv_msg(conn)
            if not msg: break
            cmd = msg.get("cmd", "").upper()
            args = msg.get("args", [])
            req_id = msg.get("id", None)
            COMMAND_LOGS.append(cmd)
            handler = COMMANDS.get(cmd)
            if handler:
                resp = handler(args)
                resp["id"] = req_id
            else:
                resp = {"id": req_id, "status":"ERROR", "output":"", "error":f"Unknown command {cmd}"}
            send_msg(conn, resp)
            if cmd == "QUIT":
                break
    except Exception as e:
        print("Client error:", e)
    finally:
        conn.close()
        print(f"[-] Client disconnected: {addr}")

# ---------------- Server Start ----------------
def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"Server listening on {HOST}:{PORT}")
    try:
        while True:
            conn, addr = sock.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print("Server shutting down")
    finally:
        sock.close()

if __name__ == "__main__":
    start_server()
