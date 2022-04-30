"""Server module."""

import socket
import threading
import rsa


class Server:
    """Server class."""

    def __init__(self, port: int) -> None:
        """Receives information."""
        self.host = "127.0.0.1"
        self.port = port
        self.clients = []
        self.username_lookup = {}
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """Start."""
        self.s.bind((self.host, self.port))
        self.s.listen(100)

        keys = rsa.keys()
        self.keys_public = [keys[1], keys[0]]
        self.keys_private = [keys[2], keys[0]]

        while True:
            client, address = self.s.accept()
            username = client.recv(1024).decode()
            client.send(f"{self.keys_public}".encode())
            data = client.recv(1024).decode()
            client_keys_public = list(map(int, data[1:-1].split(", ")))

            self.username_lookup[client] = [username, client_keys_public]
            self.clients.append(client)

            print(f"New client: {username}.")
            self.broadcast(f"{username} joined chat.")

            threading.Thread(
                target=self.handle_client,
                args=(
                    client,
                    address,
                ),
            ).start()

    def broadcast(self, text: str):
        """Broadcast."""
        for _ in self.clients:
            _.send(str(rsa.encoding(text, self.username_lookup[_][-1])).encode())

    def handle_client(self, client: socket, address):
        """Handles client."""
        while True:
            text = rsa.decoding(client.recv(1024).decode(), self.keys_private)
            for _ in self.clients:
                if _ != client:
                    _.send(rsa.encoding(text, self.username_lookup[_][-1]).encode())


if __name__ == "__main__":
    s = Server(9001)
    s.start()
