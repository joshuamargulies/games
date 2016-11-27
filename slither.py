import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 225, 225)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

img = pygame.image.load('snake.png')
apple = pygame.image.load('apple.png')
body = pygame.image.load('snakebody.png')

clock = pygame.time.Clock()

block_size = 20
FPS_init = 10


directionhead = "right"


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def d_direction(x, y):
    if x == -1 * block_size:
        direction = "left"
    elif x == 1 * block_size:
        direction = "right"
    elif y == -1 * block_size:
        direction = "up"
    else:
        direction = "down"
    return direction

rotate = {"up":0, "left":90, "down":180, "right":270}

def snake(snakelist):
# head - direction comes from player
    head = pygame.transform.rotate(img, rotate[directionhead])
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

# body - direction comes from segment ahead of it
    if len(snakelist) > 1:
        for idx in range(0, len(snakelist) -1):
            x = snakelist[idx + 1][0] - snakelist[idx][0]
            y = snakelist[idx + 1][1] - snakelist[idx][1]
            d = d_direction(x,y)
            segment = pygame.transform.rotate(body, rotate[d])
            gameDisplay.blit(segment, (snakelist[idx][0], snakelist[idx][1]))
      #      pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def score(score, speed):
    text = smallfont.render("Score: " + str(score) + " Speed: " + str(speed), True, black)
    gameDisplay.blit(text, [0,0])

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global directionhead
    gameExit = False
    gameOver = False
    FPS = FPS_init

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0




    while not gameExit:

        while gameOver == True:
            #gameDisplay.fill(white)
            message_to_screen(" ya boi wins!",
                              red,
                              y_displace=-50,
                              size="large")

            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        FPS = FPS_init
                        direction = "right"
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    directionhead = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    directionhead = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    directionhead = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    directionhead = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        AppleThickness = 30
 #       pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(apple, [randAppleX, randAppleY])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)


        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(snakeList)

        score(snakeLength - 1, FPS)



        pygame.display.update()

        ##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
        ##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
        ##                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
        ##                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
        ##                snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                snakeLength += 1
                FPS += 0

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                snakeLength += 1
                FPS += 0

        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
