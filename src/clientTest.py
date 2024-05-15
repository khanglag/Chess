import socket
import threading

def receive_messages(client_socket):
    while True:
        # Nhận tin nhắn từ server và in ra màn hình
        message = client_socket.recv(1024).decode('utf-8')
        print(message)

def main():
    # Kết nối đến server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.20', 5050))

    # Bắt đầu một thread mới để nhận tin nhắn từ server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Gửi tin nhắn từ client
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
