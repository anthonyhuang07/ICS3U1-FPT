import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 700))

button = 0

# colors
LIGHT1 = (22, 219, 101)
DARK1 = (5, 140, 66)
DARK2 = (4, 71, 28)
DARK3 = (13, 40, 24)
DARK4 = (2, 2, 2)

# fonts
regular = pygame.font.Font("./assets/fonts/ChakraPetch-Regular.ttf",60)
medium = pygame.font.Font("./assets/fonts/ChakraPetch-Medium.ttf",50)

money = 0

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            button = event.button

    if button == 1:
        if(mx > 100 and mx < 475 and my > 175 and my < 275):
            money += 1
        button = 0

    # background
    screen.fill(DARK4)
    pygame.draw.rect(screen, LIGHT1, (1,2,999,698), 2)

    # header
    pygame.draw.rect(screen, LIGHT1, (1,1,999,125), 2)
    moneyText = regular.render("$" + str(money) , 1, LIGHT1)
    screen.blit(moneyText, (100,27.5))

    pygame.draw.rect(screen, LIGHT1, (100,160,385,100))
    pygame.draw.rect(screen, LIGHT1, (525,160,385,100), 2)
    pygame.draw.rect(screen, LIGHT1, (100,295,385,100), 2)
    pygame.draw.rect(screen, LIGHT1, (100,430,385,100), 2)
    pygame.draw.rect(screen, LIGHT1, (100,565,385,100), 2)

    pygame.display.update()

pygame.quit()