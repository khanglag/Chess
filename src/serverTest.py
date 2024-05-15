import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
def handle_client(client_socket):
    while True:
        # Nhận dữ liệu từ client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print("Received message from client:", data)
        
        # Gửi dữ liệu đã nhận cho tất cả các client khác
        for c in clients:
            if c != client_socket:
                c.send(data.encode('utf-8'))

    # Khi client ngắt kết nối, loại bỏ nó khỏi danh sách và đóng kết nối
    clients.remove(client_socket)
    client_socket.close()

def main():
    # Khởi tạo socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Server listening on port 5050..."+HOST)
    
    while True:
        # Chấp nhận kết nối từ client
        client_socket, addr = server_socket.accept()
        print("Accepted connection from", addr)
        
        # Thêm client vào danh sách
        clients.append(client_socket)
        
        # Bắt đầu một thread mới để xử lý client này
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

clients = []

if __name__ == "__main__":
    main()
