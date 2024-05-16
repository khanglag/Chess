# import socket
# import pickle
# import engine  # Ensure this is the correct module

# HOST = "192.168.116.1"  # Update to your server's IP address
# PORT = 5050  # Ensure this port is correct and available
# BUFFER_SIZE = 4096

# def main():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket
#     server.bind((HOST, PORT))  # Bind socket to address and port
#     server.listen()  # Listen for connections
#     print("Waiting for connection...")

#     conn, addr = server.accept()  # Accept connection from client
#     print(f"Connection established with {addr}")

#     gs = engine.GameState()  # Create game state
#     validMoves = gs.getValidMoves()  # Get initial valid moves

#     while True:
#         try:
#             data = pickle.dumps(validMoves)  # Convert valid moves to binary data
#             conn.send(data)  # Send data to client

#             # Receive move from client
#             data = conn.recv(BUFFER_SIZE)
#             if data:
#                 received_move = pickle.loads(data)  # Convert binary data to move
#                 gs.makeMove(received_move)  # Make move on the board
#                 validMoves = gs.getValidMoves()  # Update valid moves
#         except KeyboardInterrupt:
#             print("\nServer terminated by user.")
#             break

#     conn.close()  # Close connection
#     server.close()  # Close socket

# if __name__ == "__main__":
#     main()

import socket
import pickle
import engine  # Đảm bảo bạn có module 'engine'

HOST = "192.168.116.1" # Lắng nghe trên tất cả các giao diện khả dụng
PORT = 5050  # Cổng để lắng nghe
BUFFER_SIZE = 4096

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Máy chủ đang chờ kết nối...")

    conn, addr = server.accept()
    print(f"Kết nối được thiết lập với {addr}")

    gs = engine.GameState()  # Khởi tạo trạng thái trò chơi
    validMoves = gs.getValidMoves()  # Lấy các nước đi hợp lệ ban đầu

    while True:
        try:
            # Gửi các nước đi hợp lệ cho máy khách
            data = pickle.dumps(validMoves)
            conn.send(data)

            # Nếu là lượt của người chơi Trắng (máy chủ)
            if gs.whiteToMove:
                print("Lượt của người chơi Trắng")
                data = conn.recv(BUFFER_SIZE)
                if data:
                    received_move = pickle.loads(data)
                    gs.makeMove(received_move)
                    validMoves = gs.getValidMoves()
            else:
                print("Lượt của người chơi Đen")
                received_move = None
                while not received_move:
                    data = conn.recv(BUFFER_SIZE)
                    if data:
                        received_move = pickle.loads(data)
                        gs.makeMove(received_move)
                        validMoves = gs.getValidMoves()
        except KeyboardInterrupt:
            print("\nMáy chủ đã bị dừng bởi người dùng.")
            break
        except Exception as e:
            print(f"Một lỗi đã xảy ra: {e}")
            break

    conn.close()
    server.close()

if __name__ == "__main__":
    main()
