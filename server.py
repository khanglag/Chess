import socket
import threading
import pickle

clients = []

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(4096)
            if data:
                broadcast(data, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(data, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(data)
            except:
                clients.remove(client)
                client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.116.1', 5050))
    server.listen(2)
    print("Server started, waiting for connections...")

    while True:
        client_socket, addr = server.accept()
        print(f"Client {addr} connected")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
