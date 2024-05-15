import socket
import threading
import pickle

# Cấu hình server
HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def handle_client(conn, addr):
    print(f"Đã kết nối với {addr}")
    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break
            broadcast(data, conn)
        except:
            clients.remove(conn)
            conn.close()
            break

def broadcast(data, conn):
    for client in clients:
        if client != conn:
            try:
                client.send(data)
            except:
                clients.remove(client)
                client.close()

def main():
    print("Server đang chạy..."+ HOST)
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
