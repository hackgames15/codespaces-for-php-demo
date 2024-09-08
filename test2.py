import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

# Client settings
HOST = '127.0.0.1'
PORT = 5000

# Initialize socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        self.root.configure(bg="#1E1E1E")

        self.server_ip = tk.Label(root,text=f"server_ip: {HOST}")
        self.server_ip.pack()
        self.server_port = tk.Label(root,text=f"server_port: {PORT}")
        self.server_port.pack()
        
        self.chat_label = tk.Label(root, text="Chat:")
        self.chat_label.pack(padx=20, pady=5)
        
        self.text_area = scrolledtext.ScrolledText(root)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')
        
        self.msg_label = tk.Label(root, text="Message:")
        self.msg_label.pack(padx=20, pady=5)
        
        self.msg_entry = tk.Entry(root, width=50)
        self.msg_entry.pack(padx=20, pady=5)
        
        self.send_button = tk.Button(root, text="Send", command=self.write)
        self.send_button.pack(padx=20, pady=5)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(padx=20, pady=5)
        
        self.root.protocol("WM_DELETE_WINDOW", self.stop)

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent=root)
        client.send(self.nickname.encode('utf-8'))
        
        self.running = True
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()

    def write(self):
        message = f"{self.nickname}: {self.msg_entry.get()}"
        client.send(message.encode('utf-8'))
        self.msg_entry.delete(0, tk.END)

    def receive(self):
        while self.running:
            try:
                message = client.recv(1024).decode('utf-8')
                self.text_area.config(state='normal')
                self.text_area.insert(tk.END, message + '\n')
                self.text_area.config(state='disabled')
                self.text_area.yview(tk.END)
            except:
                print("An error occurred!")
                client.close()
                break

    def stop(self):
        self.running = False
        client.close()
        self.root.destroy()

root = tk.Tk()
app = ChatClient(root)
root.mainloop()
