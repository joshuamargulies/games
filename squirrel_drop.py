import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# Initialise screen
pygame.init()
display_width = 600
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Squirrel drop')
screen.fill(white)

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

sqrl_size = 30

#gameDisplay = pygame.display.set_mode((display_width, display_height))
#pygame.display.set_caption('Squirrel Drop')


clock = pygame.time.Clock()
FPS = 30


sqrl = pygame.image.load('sqrl.png')

def gameLoop():

    randsqrlX = round(random.randrange(0, display_width - sqrl_size))  # /10.0)*10.0
    sqrlY = 0
    screen.blit(sqrl, [randsqrlX, sqrlY])
    pygame.display.update()

    while sqrlY < display_height - sqrl_size:
        screen.fill(white,[randsqrlX, sqrlY, sqrl_size, sqrl_size])
        sqrlY += 5
        screen.blit(sqrl, [randsqrlX, sqrlY])
        pygame.display.update()

        clock.tick(FPS)
    gameLoop()
gameLoop()