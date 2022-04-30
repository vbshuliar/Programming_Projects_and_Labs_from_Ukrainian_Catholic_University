"""Client module."""
import socket
import threading
import rsa


class Client:
    """Client class."""

    def __init__(self, server_ip: str, port: int, username: str) -> None:
        """Receives information."""

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
        server_keys_public = list(map(int, data[1:-1].split(", ")))

        self.s.send(str(self.keys_public).encode())

        message_handler = threading.Thread(target=self.read_handler, args=())
        message_handler.start()
        input_handler = threading.Thread(target=self.write_handler, args=())
        input_handler.start()

    def read_handler(self):
        """Read handler."""
        while True:
            message = self.s.recv(1024).decode()

            print(message)

    def write_handler(self):
        """Write handler."""
        while True:
            message = input()

            self.s.send(message.encode())


if __name__ == "__main__":
    cl = Client("127.0.0.1", 9001, "User")
    cl.init_connection()
