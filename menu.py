import pygame
import sys
from constants import WIDTH, HEIGHT, SQ_SIZE
from graphics import drawText

def menu(screen):
    while True:
        background_image = pygame.transform.scale(pygame.image.load("images/background.png"), (WIDTH, HEIGHT))
        screen.blit(background_image, (0, 0))
        drawText(screen, "Chess Game", pygame.Color("#FFFFCC"), (WIDTH // 2, HEIGHT // 4), 60, center=True)
        
        pygame.draw.rect(screen, pygame.Color("#FFFFCC"), (125, 200, 250, 50))
        drawText(screen, "Play with Bot", pygame.Color("#666666"), (250, 225), 36, center=True)
        
        pygame.draw.rect(screen, pygame.Color("#FFFFCC"), (125, 300, 250, 50))
        drawText(screen, "Play with Human", pygame.Color("#666666"), (250, 325), 36, center=True)

        pygame.draw.rect(screen, pygame.Color("#FFFFCC"), (125, 400, 250, 50))
        drawText(screen, "Play Online", pygame.Color("#666666"), (250, 425), 36, center=True)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    x, y = event.pos
                    if 125 <= x <= 375 and 200 <= y <= 250:  
                        return "bot"
                    elif 125 <= x <= 375 and 300 <= y <= 350:  
                        return "human"
                    elif 125 <= x <= 375 and 400 <= y <= 450:
                        return "socket"
def menuSocket(screen):
    while True:
        background_image = pygame.transform.scale(pygame.image.load("images/background.png"), (WIDTH, HEIGHT))
        screen.blit(background_image, (0, 0))
        drawText(screen, "Chess Game", pygame.Color("#FFFFCC"), (WIDTH // 2, HEIGHT // 4), 60, center= True)

        pygame.draw.rect(screen, pygame.Color("#FFFFCC"), (125, 200, 250, 50))
        drawText(screen, "White", pygame.Color("#666666"), (250, 225), 36, center=True)

        pygame.draw.rect(screen, pygame.Color("#FFFFCC"), (125, 300, 250, 50))
        drawText(screen, "Black", pygame.Color("#666666"), (250, 325), 36, center=True)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if 125 <= x <= 375 and 200 <= y <= 250:
                        return "white"
                    elif 125 <= x <= 375 and 300 <= y <= 350:
                        return "black"
