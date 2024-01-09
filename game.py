import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 700))

button = 0

# purchase status
t2s = t3s = t4s = t5s = t6s = t7s = t8s = 0

# button coordinates
boxW = 385
boxH = 100
boxRX = 100
boxRX2 = 525
boxY1 = 160
boxY2 = 295
boxY3 = 430
boxY4 = 565

# colors
LIGHT1 = (22, 219, 101)
DARK1 = (5, 140, 66)
DARK2 = (4, 71, 28)
DARK3 = (13, 40, 24)
DARK4 = (2, 2, 2)

# fonts
regular = pygame.font.Font("./assets/fonts/ChakraPetch-Regular.ttf", 60)
light = pygame.font.Font("./assets/fonts/ChakraPetch-Light.ttf", 30)

baseMoney = 60

money = 0

def calcReqCost(n):
    final = baseMoney*(12**(n-2))
    return final


def task(statVar, moneyReq, x, y, n):

    buyTxt = light.render("BUY TASK" + " - " + str(round(calcReqCost(n))), 1, LIGHT1)
    buyTxtCan = light.render("BUY TASK" + " - " + str(round(calcReqCost(n))), 1, DARK4)
    textWidth, textHeight = light.size("BUY TASK" + " - " + str(round(calcReqCost(n))))

    button = pygame.Rect(x, y, boxW, boxH)

    if money >= moneyReq and statVar == 0:
        pygame.draw.rect(screen, LIGHT1, button)
        textX = x + (boxW - textWidth) // 2
        textY = y + (boxH - textHeight) // 2
        textRect = pygame.Rect(textX, textY, textWidth, textHeight)
        screen.blit(buyTxtCan, textRect)
    elif statVar == 0:
        pygame.draw.rect(screen, LIGHT1, button, 2)
        textX = x + (boxW - textWidth) // 2
        textY = y + (boxH - textHeight) // 2
        textRect = pygame.Rect(textX, textY, textWidth, textHeight)
        screen.blit(buyTxt, textRect)
    elif statVar == 1:
        pygame.draw.rect(screen, LIGHT1, (x, y, boxW, boxH), 6)


playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            button = event.button

    if button == 1:
        if mx > boxRX and mx < boxRX + boxW and my > boxY1 and my < boxY1 + boxH:
            money += 1
        elif mx > boxRX and mx < boxRX + boxW and my > boxY2 and my < boxY2 + boxH:
            if t2s == 0 and money >= calcReqCost(2):
                t2s = 1
                money -= calcReqCost(2)
            elif t2s == 1:
                money += calcReqCost(2)
        elif mx > boxRX and mx < boxRX + boxW and my > boxY3 and my < boxY3 + boxH:
            if t3s == 0 and money >= calcReqCost(3):
                t3s = 1
                money -= calcReqCost(3)
            elif t3s == 1:
                money += calcReqCost(3)*0.75
        elif mx > boxRX and mx < boxRX + boxW and my > boxY4 and my < boxY4 + boxH:
            if t4s == 0 and money >= calcReqCost(4):
                t4s = 1
                money -= calcReqCost(4)
            elif t4s == 1:
                money += calcReqCost(4)*0.5

        button = 0

    # background
    screen.fill(DARK4)
    pygame.draw.rect(screen, LIGHT1, (1, 2, 999, 698), 2)

    # header
    pygame.draw.rect(screen, LIGHT1, (1, 1, 999, 125), 2)
    moneyText = regular.render("$" + str(money), 1, LIGHT1)
    screen.blit(moneyText, (100, 27.5))

    ## TASKS ##

    task(1, 0, boxRX, boxY1, 1)
    task(t2s, calcReqCost(2), boxRX, boxY2, 2)
    task(t3s, calcReqCost(3), boxRX, boxY3, 3)
    task(t4s, calcReqCost(4), boxRX, boxY4, 4)
    task(t5s, calcReqCost(5), boxRX2, boxY1, 5)
    task(t6s, calcReqCost(6), boxRX2, boxY2, 6)
    task(t7s, calcReqCost(7), boxRX2, boxY3, 7)
    task(t8s, calcReqCost(8), boxRX2, boxY4, 8)

    pygame.display.update()

pygame.quit()
