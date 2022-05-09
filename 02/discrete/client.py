"""Client module."""
import socket
import threading
import rsa_algorithm as rsa
import hashlib


class Client:
    """Chat user."""

    def __init__(self, server_ip: str, port: int, username: str) -> None:
        """Basic information."""
        self.server_ip = server_ip
        self.port = port
        self.username = username

    def init_connection(self):
        """Initializes connection."""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.server_ip, self.port))
        except Exception as e:
            return print("Server is offline!")
        keys = rsa.keys()
        self.keys_public = (keys[1], keys[0])
        self.keys_private = (keys[2], keys[0])
        self.s.send(self.username.encode())
        data = self.s.recv(1024).decode()
        self.server_keys_public = list(map(int, data[1:-1].split(", ")))
        self.s.send(str(self.keys_public).encode())
        message_handler = threading.Thread(target=self.read_handler, args=())
        message_handler.start()
        input_handler = threading.Thread(target=self.write_handler, args=())
        input_handler.start()

    def read_handler(self):
        """Decodes message from another user in the chat."""
        while True:
            data = self.s.recv(1024).decode()
            text_hash, text = data[1:-1].split(", ")
            text = rsa.decoding(text, self.keys_private)
            test = hashlib.sha256()
            test.update(text.encode())
            test = str(test.digest())
            assert test == text_hash
            print(text)

    def write_handler(self):
        """Encodes user's input and sends it to the server."""
        while True:
            message = input()[:180]
            text = rsa.encoding(message, self.server_keys_public)
            text_hash = hashlib.sha256()
            text_hash.update(message.encode())
            text_hash = str(text_hash.digest())
            self.s.send(f"({text_hash}, {text})".encode())


if __name__ == "__main__":
    cl = Client("127.0.0.1", 9002, "User")
    cl.init_connection()
