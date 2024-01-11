# GAME INSPIRED BY ADVENTURE CAPITALIST #
# MATHEMATICAL SOURCES USED BELOW #
# https://www.youtube.com/watch?v=Ogdo271YWsw #
# https://adventure-capitalist.fandom.com/wiki/Businesses #
# SAME MATHEMATICAL FORMULAS AS ADVENTURE CAPITALIST ARE USED! #

import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 700))

button = 0

# task coordinates
boxW = 385
boxH = 100
boxRX = 100
boxRX2 = 525
boxY1 = 160
boxY2 = 295
boxY3 = 430
boxY4 = 565

# buy button coordinates
buyW = boxW / (4 / 3) / 1.4 + 6
buyH = boxH / 2
buyRX = boxRX + boxW / 4 - 5
buyRX2 = boxRX2 + boxW / 4 - 5
buyY1 = boxY1 + boxH / 2
buyY2 = boxY2 + boxH / 2
buyY3 = boxY3 + boxH / 2
buyY4 = boxY4 + boxH / 2


# colors
LIGHT1 = (22, 219, 101)
DARK1 = (5, 140, 66)
DARK2 = (4, 71, 28)
DARK3 = (13, 40, 24)
DARK4 = (2, 2, 2)

# fonts
regular = pygame.font.Font("./assets/fonts/ChakraPetch-Regular.ttf", 60)
regularS = pygame.font.Font("./assets/fonts/ChakraPetch-Regular.ttf", 25)
light = pygame.font.Font("./assets/fonts/ChakraPetch-Light.ttf", 30)
lightS = pygame.font.Font("./assets/fonts/ChakraPetch-Light.ttf", 23)


# calculates task cost requirements (e.g. task 2 is $60)
def calcReqCost(n):
    if n == 1:
        final = 3.738317757
    else:
        final = baseMoney * (12 ** (n - 2))
    return final


def calcTaskCost(n):
    final = calcReqCost(n) * (coefficients[n - 1] ** amounts[n - 1])
    return final


# base moneys
money = 0.00
baseMoney = 60.00

# purchase status
t1s = 1
t2s = t3s = t4s = t5s = t6s = t7s = t8s = 0
statuses = [t1s, t2s, t3s, t4s, t5s, t6s, t7s, t8s]

# base income
BI1 = 1.00
BI2 = calcReqCost(2)
BI3 = calcReqCost(3) * 0.75
BI4 = calcReqCost(4) * 0.5
BI5 = calcReqCost(5) * 0.5
BI6 = calcReqCost(6) * 0.5
BI7 = calcReqCost(7) * 0.5
BI8 = calcReqCost(8) * 0.5
BIarr = [BI1, BI2, BI3, BI4, BI5, BI6, BI7, BI8]

# coefficients constant
CF1 = 1.07
CF2 = 1.15
CF3 = 1.14
CF4 = 1.13
CF5 = 1.12
CF6 = 1.11
CF7 = 1.10
CF8 = 1.09
coefficients = [CF1, CF2, CF3, CF4, CF5, CF6, CF7, CF8]

# amount of task
a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = 1
amounts = [a1, a2, a3, a4, a5, a6, a7, a8]


# draws the task boxes
def task(statVar, x, y, n):
    buyTxt = light.render("BUY TASK - $%.2f" % calcReqCost(n), 1, LIGHT1)
    buyTxtCan = light.render("BUY TASK - $%.2f" % calcReqCost(n), 1, DARK4)
    textWidth, textHeight = light.size("BUY TASK - $%.2f" % calcReqCost(n))

    button = pygame.Rect(x, y, boxW, boxH)

    if money >= calcReqCost(n) and statVar == 0:  # Can Buy
        pygame.draw.rect(screen, LIGHT1, button)
        textX = x + (boxW - textWidth) // 2
        textY = y + (boxH - textHeight) // 2
        textRect = pygame.Rect(textX, textY, textWidth, textHeight)
        screen.blit(buyTxtCan, textRect)
    elif statVar == 0:  # Cannot Buy
        pygame.draw.rect(screen, LIGHT1, button, 2)
        textX = x + (boxW - textWidth) // 2
        textY = y + (boxH - textHeight) // 2
        textRect = pygame.Rect(textX, textY, textWidth, textHeight)
        screen.blit(buyTxt, textRect)
    elif statVar == 1:  # Bought
        # text
        income = BIarr[n - 1] * amounts[n - 1]
        text = "$%.2f" % income
        incomeTxt = regularS.render(text, 1, LIGHT1)
        textWidthR, textHeightR = regularS.size(text)
        textXR = x + boxW / 4 - 5 + (boxW / (4 / 3) + 7 - textWidthR) // 2
        textYR = y + (boxH / 2 - textHeightR) // 2
        textRectR = pygame.Rect(textXR, textYR + 4, textWidthR, textHeightR)
        screen.blit(incomeTxt, textRectR)

        text = "Buy x1 - %.2f" % calcTaskCost(n)
        textWidthL, textHeightL = lightS.size(text)
        textXL = x + boxW / 4 - 5 + (boxW / (4 / 3) / 1.4 + 7 - textWidthL) // 2
        textYL = y + boxH / 2 + (boxH / 2 - textHeightL) // 2
        textRectL = pygame.Rect(textXL, textYL, textWidthL, textHeightL)

        # boxes
        pygame.draw.rect(screen, LIGHT1, (x, y, boxW, boxH), 5)  # whole task box
        pygame.draw.rect(screen, LIGHT1, (x, y, boxW / 4, boxH))  # picture box
        pygame.draw.rect(
            screen,
            LIGHT1,
            (x + boxW / 4 - 5, y + boxH / 2, boxW / (4 / 3) + 6, boxH / 2),
            5,
        )  # bottom action box
        if money >= calcTaskCost(n):
            pygame.draw.rect(
                screen,
                LIGHT1,
                (x + boxW / 4 - 5, y + boxH / 2, boxW / (4 / 3) / 1.4 + 6, boxH / 2),
            )
            buyTxt2 = lightS.render(text, 1, DARK4)
            screen.blit(buyTxt2, textRectL)
        else:
            pygame.draw.rect(
                screen,
                LIGHT1,
                (x + boxW / 4 - 5, y + boxH / 2, boxW / (4 / 3) / 1.4 + 6, boxH / 2),
                5,
            )
            buyTxt2 = lightS.render(text, 1, LIGHT1)
            screen.blit(buyTxt2, textRectL)


def taskClick(n, x, y, bx, by):
    global money

    if mx > x and mx < x + boxW and my > y and my < y + boxH:
        if statuses[n - 1] == 0 and money >= calcReqCost(n):
            statuses[n - 1] = 1
            money -= calcReqCost(n)
        elif (
            statuses[n - 1] == 1
            and money < calcTaskCost(n)
            and mx > bx
            and mx < bx + buyW
            and my > by
            and my < by + buyH
        ):
            return
        elif (
            statuses[n - 1] == 1
            and money >= calcTaskCost(n)
            and mx > bx
            and mx < bx + buyW
            and my > by
            and my < by + buyH
        ):
            money -= calcTaskCost(n)
            amounts[n - 1] += 1
        elif statuses[n - 1] == 1:
            money += BIarr[n - 1] * amounts[n - 1]


playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            button = event.button

    if button == 1:
        count = 1
        for i in range(1, 9):
            if i == 5:
                count = 1
            yPos = [boxY1, boxY2, boxY3, boxY4, buyY4, buyY3, buyY2, buyY1]
            if i < 5:
                taskClick(i, boxRX, yPos[count - 1], buyRX, yPos[-count])
                count += 1
            else:
                taskClick(i, boxRX2, yPos[count - 1], buyRX2, yPos[-count])
                count += 1

        button = 0

    # background
    screen.fill(DARK4)
    pygame.draw.rect(screen, LIGHT1, (1, 2, 999, 698), 2)

    # header
    pygame.draw.rect(screen, LIGHT1, (1, 1, 999, 125), 2)
    moneyText = regular.render("$%.2f" % money, 1, LIGHT1)
    screen.blit(moneyText, (100, 27.5))

    ## TASKS ##

    count = 1
    for i in range(1, 9):
        if i == 5:
            count = 1
        yPos = [boxY1, boxY2, boxY3, boxY4]
        if i < 5:
            task(statuses[i-1], boxRX, yPos[count - 1], i)
            count += 1
        else:
            task(statuses[i-1], boxRX2, yPos[count - 1], i)
            count += 1

    pygame.display.update()

pygame.quit()
