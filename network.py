import socket
import threading
import pickle
import pygame
import sys
import engine
from graphics import drawGameState, drawText, animateMove, loadImages
from constants import WIDTH, HEIGHT, SQ_SIZE, MAX_FPS

def receive_data(client, gs, validMoves):
    global moveMade, animate
    while True:
        try:
            data = client.recv(4096)
            if data:
                move = pickle.loads(data)
                print(f"Nước đi từ đối thủ: {move.getChessNotation()}")
                gs.makeMove(move)
                moveMade = True
                animate = True
        except Exception as e:
            print("Mất kết nối với server")
            print(f"Error: {e}")
            client.close()
            break

def send_data(client, data):
    try:
        serialized_data = pickle.dumps(data)
        client.send(serialized_data)
    except Exception as e:
        print(f"Không thể gửi dữ liệu: {e}")

def white():
    global moveMade, animate
    moveMade = False
    animate = False

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))

    gs = engine.GameState()
    validMoves = gs.getValidMoves()
    loadImages()
    run = True
    sqSelected = ()
    playerClicks = []
    gameOver = False
    playerOne = True
    playerTwo = False

    # Kết nối tới server
    HOST = '192.168.116.1'  # Địa chỉ IP của server
    PORT = 5050

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Bắt đầu luồng để nhận dữ liệu từ server
    receive_thread = threading.Thread(target=receive_data, args=(client, gs, validMoves))
    receive_thread.start()

    while run:
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not gameOver and humanTurn:
                    location = pygame.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if sqSelected == (row, col):
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks) == 2:
                        move = engine.Move(playerClicks[0], playerClicks[1], gs.board)
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(validMoves[i])
                                send_data(client, move)
                                moveMade = True
                                animate = True
                                sqSelected = ()
                                playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected]

        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock)
            validMoves = gs.getValidMoves()
            moveMade = False
            animate = False

        drawGameState(screen, gs, validMoves, sqSelected)

        if gs.checkmate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen, "Black wins by checkmate", pygame.Color("black"), (WIDTH // 2, HEIGHT // 2))
            else:
                drawText(screen, "White wins by checkmate", pygame.Color("black"), (WIDTH // 2, HEIGHT // 2))
        elif gs.stalemate:
            gameOver = True
            drawText(screen, "Stalemate", pygame.Color("black"), (WIDTH // 2, HEIGHT // 2))

        clock.tick(MAX_FPS)
        pygame.display.flip()
    
    pygame.quit()

def black():
    global moveMade, animate
    moveMade = False
    animate = False

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))

    gs = engine.GameState()
    validMoves = gs.getValidMoves()
    loadImages()
    run = True
    sqSelected = ()
    playerClicks = []
    gameOver = False
    playerOne = False
    playerTwo = True

    # Kết nối tới server
    HOST = '192.168.116.1'  # Địa chỉ IP của server
    PORT = 5050

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Bắt đầu luồng để nhận dữ liệu từ server
    receive_thread = threading.Thread(target=receive_data, args=(client, gs, validMoves))
    receive_thread.start()

    while run:
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not gameOver and humanTurn:
                    location = pygame.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if sqSelected == (row, col):
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks) == 2:
                        move = engine.Move(playerClicks[0], playerClicks[1], gs.board)
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(validMoves[i])
                                send_data(client, move)
                                moveMade = True
                                animate = True
                                sqSelected = ()
                                playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected]

        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock)
            validMoves = gs.getValidMoves()
            moveMade = False
            animate = False

        drawGameState(screen, gs, validMoves, sqSelected)

        if gs.checkmate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen, "Black wins by checkmate", pygame.Color("black"), (WIDTH // 2, HEIGHT // 2))
            else:
                drawText(screen, "White wins by checkmate", pygame.Color("black"), (WIDTH // 2, HEIGHT // 2))
        elif gs.stalemate:
            gameOver = True
            drawText(screen, "Stalemate", pygame.Color("black"), (WIDTH // 2, HEIGHT // 2))

        clock.tick(MAX_FPS)
        pygame.display.flip()
    
    pygame.quit()
