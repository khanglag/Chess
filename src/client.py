import socket
import threading
import pygame
import sys
import engine
import pickle

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def receive_data(client, gs, validMoves):
    global moveMade, animate , playerOne, playerTwo
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

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     clock = pygame.time.Clock()
#     screen.fill(pygame.Color("white"))
#
#     gs = engine.GameState()
#     validMoves = gs.getValidMoves()
#     moveMade = False
#     animate = False
#     loadImages()
#     run = True
#     sqSelected = ()
#     playerClicks = []
#     gameOver = False
#     playerOne = True
#     playerTwo = False
#
#
#     # Kết nối tới server
#     HOST = '192.168.1.20'  # Địa chỉ IP của server
#     PORT = 5050
#
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect((HOST, PORT))
#
#     # Bắt đầu luồng để nhận dữ liệu từ server
#     receive_thread = threading.Thread(target=receive_data, args=(client, gs, validMoves))
#     receive_thread.start()
#
#     while run:
#         humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 client.close()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if not gameOver and humanTurn:
#                     location = pygame.mouse.get_pos()
#                     col = location[0] // SQ_SIZE
#                     row = location[1] // SQ_SIZE
#                     if sqSelected == (row, col):
#                         sqSelected = ()
#                         playerClicks = []
#                     else:
#                         sqSelected = (row, col)
#                         playerClicks.append(sqSelected)
#                     if len(playerClicks) == 2:
#                         move = engine.Move(playerClicks[0], playerClicks[1], gs.board)
#                         for i in range(len(validMoves)):
#                             if move == validMoves[i]:
#                                 gs.makeMove(validMoves[i])
#                                 send_data(client, validMoves[i])
#                                 moveMade = True
#                                 animate = True
#                                 sqSelected = ()
#                                 playerClicks = []
#                                 playerOne = not playerOne
#                                 playerTwo = not playerTwo
#                         if not moveMade:
#                             playerClicks = [sqSelected]
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_z:
#                     gs.undoMove()
#                     moveMade = True
#                     animate = False
#                 if event.key == pygame.K_r:
#                     gs = engine.GameState()
#                     validMoves = gs.getValidMoves()
#                     sqSelected = ()
#                     playerClicks = []
#                     moveMade = False
#                     animate = False
#
#         if moveMade:
#             if animate:
#                 animateMove(gs.moveLog[-1], screen, gs.board, clock)
#             validMoves = gs.getValidMoves()
#             moveMade = False
#             animate = False
#
#         drawGameState(screen, gs, validMoves, sqSelected)
#
#         if gs.checkmate:
#             gameOver = True
#             if gs.whiteToMove:
#                 drawText(screen, "Black wins by checkmate", pygame.Color("black"), (WIDTH // 2, HEIGHT // 2))
#             else:
#                 drawText(screen, "White wins by checkmate", pygame.Color("black"), (WIDTH // 2, HEIGHT // 2))
#         elif gs.stalemate:
#             gameOver = True
#             drawText(screen, "Stalemate", pygame.Color("black"), (WIDTH // 2, HEIGHT // 2))
#
#         clock.tick(MAX_FPS)
#         pygame.display.flip()
#
#     pygame.quit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))

    gs = engine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    animate = False
    loadImages()
    run = True
    sqSelected = ()
    playerClicks = []
    gameOver = False
    # playerOne = True
    # playerTwo = False


    # Kết nối tới server
    HOST = '192.168.1.20'  # Địa chỉ IP của server
    PORT = 5050

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Bắt đầu luồng để nhận dữ liệu từ server
    receive_thread = threading.Thread(target=receive_data, args=(client, gs, validMoves))
    receive_thread.start()

    while run:
        # humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                client.close()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not gameOver : #and humanTurn:
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
                                send_data(client, validMoves[i])
                                moveMade = True
                                animate = True
                                sqSelected = ()
                                playerClicks = []
                                # playerOne = not playerOne
                                # playerTwo = not playerTwo
                        if not moveMade:
                            playerClicks = [sqSelected]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    gs.undoMove()
                    moveMade = True
                    animate = False
                if event.key == pygame.K_r:
                    gs = engine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = False
                    animate = False

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

def highlightSquares(screen, gs, validMoves, sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            s = pygame.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(pygame.Color('blue'))
            screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))
            s.fill(pygame.Color('yellow'))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (move.endCol * SQ_SIZE, move.endRow * SQ_SIZE))

def drawGameState(screen, gs, validMoves, sqSelected):
    drawBoard(screen)
    highlightSquares(screen, gs, validMoves, sqSelected)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    global colors
    colors = [pygame.Color("white"), pygame.Color("#CCCCCC")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def animateMove(move, screen, board, clock):
    global colors
    coords = []
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framePerSquare = 10
    frameCount = (abs(dR) + abs(dC)) * framePerSquare
    for frame in range(frameCount + 1):
        r, c = (move.startRow + dR * frame / frameCount, move.startCol + dC * frame / frameCount)
        drawBoard(screen)
        drawPieces(screen, board)
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = pygame.Rect(move.endCol * SQ_SIZE, move.endRow * SQ_SIZE, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(screen, color, endSquare)
        if move.pieceCaptured != "--":
            screen.blit(IMAGES[move.pieceCaptured], endSquare)
        screen.blit(IMAGES[move.pieceMoved], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        pygame.display.flip()
        clock.tick(60)

def drawText(screen, text, color, center, font_size = None):
    font = pygame.font.SysFont("Helvetica", 32, True, False)
    textObject = font.render(text, 0, color)
    textLocation = textObject.get_rect(center=center)
    screen.blit(textObject, textLocation)

if __name__ == "__main__":
    main()
