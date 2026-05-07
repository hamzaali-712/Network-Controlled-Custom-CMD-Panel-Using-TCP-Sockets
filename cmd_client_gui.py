import socket, json, struct, threading, tkinter as tk
from tkinter.scrolledtext import ScrolledText

SERVER_HOST = "10.120.12.12"   # change if needed
SERVER_PORT = 50001
PROMPT = "mycmd> "

# ---------------- Network Helpers ----------------
def send_msg(sock, obj):
    data = json.dumps(obj).encode("utf-8")
    sock.sendall(struct.pack("!I", len(data)) + data)

def recv_msg(sock):
    raw = sock.recv(4)
    if not raw:
        return None
    length = struct.unpack("!I", raw)[0]
    data = b""
    while len(data) < length:
        data += sock.recv(length - len(data))
    return json.loads(data.decode("utf-8"))

# ---------------- GUI ----------------
class CmdWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Abhav - Client CMD Panel")
        self.geometry("800x450")
        self.configure(bg="black")

        # OUTPUT
        self.output = ScrolledText(
            self,
            bg="black",
            fg="white",
            font=("Consolas", 11),
            state="disabled"
        )
        self.output.pack(fill=tk.BOTH, expand=True)

        # BOTTOM BAR
        bottom = tk.Frame(self, bg="black")
        bottom.pack(fill=tk.X)

        tk.Label(
            bottom,
            text=PROMPT,
            bg="black",
            fg="white",
            font=("Consolas", 11)
        ).pack(side=tk.LEFT)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            bottom,
            textvariable=self.entry_var,
            bg="black",
            fg="white",
            insertbackground="white",
            font=("Consolas", 11)
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self.on_enter)

        # STATUS
        self.status = tk.Label(
            self,
            text="Disconnected",
            bg="black",
            fg="gray",
            anchor="w",
            font=("Consolas", 9)
        )
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

        # SOCKET
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.after(100, lambda: self.entry.focus_force())
        threading.Thread(target=self.connect, daemon=True).start()

    # ---------------- CONNECTION ----------------
    def connect(self):
        try:
            self.sock.connect((SERVER_HOST, SERVER_PORT))
            self.status.config(text="Connected")
            self.write("Connected to server.")
            threading.Thread(target=self.receive_loop, daemon=True).start()
        except Exception as e:
            self.write(f"Connection failed: {e}")

    # ---------------- OUTPUT ----------------
    def write(self, text):
        self.output.configure(state="normal")
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)
        self.output.configure(state="disabled")

    # ---------------- SEND COMMAND ----------------
    def on_enter(self, event=None):
        text = self.entry_var.get().strip()
        if not text:
            return

        parts = text.split()
        cmd = parts[0].upper()
        args = parts[1:]

        self.write(PROMPT + text)

        send_msg(self.sock, {
            "cmd": cmd,
            "args": args
        })

        self.entry_var.set("")
        self.entry.focus_force()

    # ---------------- RECEIVE ----------------
    def receive_loop(self):
        while True:
            resp = recv_msg(self.sock)
            if not resp:
                break

            output = resp.get("output", "")
            # Handle dict, list, or string output
            if isinstance(output, dict):
                for k, v in output.items():
                    self.write(f"{k}: {v}")
            elif isinstance(output, list):
                for line in output:
                    self.write(line)
            else:
                self.write(output)

# ---------------- RUN ----------------
if __name__ == "__main__":
    CmdWindow().mainloop()
