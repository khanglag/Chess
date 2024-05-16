import socket
import pickle
import  engine
HOST = "192.168.116.1"  # Update to match the server's IP address
PORT = 5050  # Ensure this port matches the server's port
BUFFER_SIZE = 4096

def connectToServer():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket
    client.connect((HOST, PORT))  # Connect to server
    print("Connected to server...")
    return client

def main():
    client = connectToServer()
    gs = engine.GameState()
    validMoves = gs.getValidMoves()

    while True:
        try:
            data = client.recv(BUFFER_SIZE)
            if data:
                validMoves = pickle.loads(data)  # Receive and decode valid moves
                print("Received valid moves from server:", validMoves)
        except KeyboardInterrupt:
            print("\nClient terminated by user.")
            break

    client.close()  # Close connection

if __name__ == "__main__":
    main()
