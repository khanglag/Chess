# import socket
# import threading
# import pickle
#
# # Cấu hình server
# HOST = socket.gethostbyname(socket.gethostname())
#
# PORT = 5050
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
# server.listen()
#
# clients = []
#
# def handle_client(conn, addr):
#     print(f"Đã kết nối với {addr}")
#     while True:
#         try:
#             data = conn.recv(4096)
#             if not data:
#                 break
#             broadcast(data, conn)
#             move = pickle.loads(data)
#             print(f"Nước đi từ {addr}: {move}")
#         except:
#             print(f"Client mất kết nối: {addr[0]}")
#             clients.remove(conn)
#             conn.close()
#             break
#
# def broadcast(data, conn):
#     for client in clients:
#         if client != conn:
#             try:
#                 client.send(data)
#             except:
#                 clients.remove(client)
#                 client.close()
#
# def main():
#     print("Server đang chạy... " + HOST)
#     while True:
#         conn, addr = server.accept()
#         clients.append(conn)
#         thread = threading.Thread(target=handle_client, args=(conn, addr))
#         thread.start()
#
# if __name__ == "__main__":
#     main()
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
    server.bind(('0.0.0.0', 5050))
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
