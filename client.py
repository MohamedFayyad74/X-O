# client/client.py
import os
import socket
from client.exceptions import *
from dotenv import load_dotenv

class client :
    load_dotenv()
    SERVER_HOST = os.getenv("HOST", "127.0.0.1")
    SERVER_PORT = int(os.getenv("PORT", "5000"))

    def __init__(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except (socket.timeout, socket.error) as e:
            raise NetworkError(f"Unexpected network error: {e}")

    def connect(self, SERVER_HOST =SERVER_HOST, SERVER_PORT = SERVER_PORT):
        try:
            self.sock.connect((SERVER_HOST, SERVER_PORT))
        except ConnectionRefusedError:
             raise ConnectionFailedError("Server refused the connection or not found.")
        except TimeoutError:
            raise TimeoutNetworkError("Connection attempt timed out.")
        except OSError as e:
            raise NetworkError(f"Unexpected network error: {e}") 
    
    def close(self):
        try:
            self.sock.close()
        except OSError as e:
            raise NetworkError(f"Unexpected network error or alerady closed: {e}")
        
    def send(self, message):
        try:
             # ensure newline (server is tolerant)
             if not message.endswith("\n"):
                 message = message + "\n"
             self.sock.sendall(message.encode())
        except BrokenPipeError:
            raise ConnectionLostError("Connection lost.")
        except ValueError:
            raise SendDataError("data format error.")
        except OSError as e:
            raise NetworkError(f"Unexpected network error: {e}")
    
    def receive(self):
        try:
            data = self.sock.recv(1024)
            if not data:
                return ""
            return data.decode()
        except (ConnectionResetError, ConnectionAbortedError):
            print("Connection closed by server.")
            return ""
        except OSError as e:
            raise NetworkError(f"Unexpected network error: {e}")


def main():
    c = client()
    c.connect()
    try:
        while True:
            response = c.receive()
            if not response:
                break
            print(response.strip())
            if "Your move" in response or "Your turn" in response:
                move = input("Enter your move (0-8) or QUIT: ")
                c.send(move)
    except KeyboardInterrupt:
        print("\nDisconnected by user.")
        try:
            c.send("QUIT")
        except Exception:
            pass
    finally:
        c.close()

if __name__ == "__main__":
    main()
