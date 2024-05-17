import pygame
import engine
import smartmoveFinder
from network import receive_data, send_data
from graphics import loadImages, drawGameState, drawText, animateMove
from menu import menu, menuSocket
from constants import WIDTH, HEIGHT, SQ_SIZE, MAX_FPS

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
    
    playerOne = True
    playerTwo = False
    
    mode = menu(screen)
    
    if mode == "bot":
        playerOne =True
    elif mode == "human":
        playerTwo = True
        
    if mode == "bot" or mode == "human":
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
                            print(move.getChessNotation())
                            for i in range(len(validMoves)):
                                if move == validMoves[i]:
                                    gs.makeMove(validMoves[i])
                                    moveMade = True
                                    animate = True
                                    sqSelected = ()
                                    playerClicks = []
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

            # BOT
            if not gameOver and not humanTurn:
                botMove = smartmoveFinder.findBestMove(gs, validMoves)
                if botMove is None:
                    botMove = smartmoveFinder.findRandomMove(validMoves)
                gs.makeMove(botMove)
                moveMade = True
                animate = True

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
    elif mode == "socket":
        choose = menuSocket(screen)
        if choose == "white":
            from network import white
            white()
        elif choose == "black":
            from network import black
            black()
    pygame.quit()

if __name__ == "__main__":
    main()
