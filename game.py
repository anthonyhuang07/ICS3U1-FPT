# GAME INSPIRED BY ADVENTURE CAPITALIST #
# MATHEMATICAL SOURCES USED BELOW #
# https://www.youtube.com/watch?v=Ogdo271YWsw #
# https://adventure-capitalist.fandom.com/wiki/Businesses #
# SAME MATHEMATICAL FORMULAS AS ADVENTURE CAPITALIST ARE USED! #

# -TERMINIMOLOGY- #
# Investment - Buy Extra of a Task to increase its profit #
# Manager - Automatically performs a task for you

# pygame setup
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1000, 700))

"""pygame.mixer.music.load("./assets/sounds/bgm.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.2)"""

pygame.display.set_caption('ByteBucks')

pygame_icon = pygame.image.load('./assets/images/icon_512x512@2x.png')
pygame.display.set_icon(pygame_icon)

# colors
LIGHT1 = (22, 219, 101)
DARK1 = (5, 140, 66)
DARK2 = (4, 71, 28)
DARK3 = (13, 40, 24)
DARK4 = (2, 2, 2)

# fonts
medium = pygame.font.Font("./assets/fonts/ChakraPetch-Medium.ttf", 60)
regular = pygame.font.Font("./assets/fonts/ChakraPetch-Regular.ttf", 60)
regularS = pygame.font.Font("./assets/fonts/ChakraPetch-Regular.ttf", 25)
regularXS = pygame.font.Font("./assets/fonts/ChakraPetch-Regular.ttf", 23)
light = pygame.font.Font("./assets/fonts/ChakraPetch-Light.ttf", 30)
lightS = pygame.font.Font("./assets/fonts/ChakraPetch-Light.ttf", 23)

# states
button = 0
shopStatus = 0

# time related (cooldowns)
clock = pygame.time.Clock()

s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = True
tm1 = tm2 = tm3 = tm4 = tm5 = tm6 = tm7 = tm8 = pygame.time.get_ticks()

c1 = 0.6 * 1000
c2 = 3 * 1000
c3 = 6 * 1000
c4 = 12 * 1000
c5 = 24 * 1000
c6 = 48 * 1000
c7 = 96 * 1000
c8 = 192 * 1000

canClick = [s1, s2, s3, s4, s5, s6, s7, s8]
timers = [tm1, tm2, tm3, tm4, tm5, tm6, tm7, tm8]
cooldowns = [c1, c2, c3, c4, c5, c6, c7, c8]

# base moneys
money = 0.00
baseMoney = 60.00

# region TASKS
# task names
t1 = "Recycled Cables"
t2 = "Battery Recycling"
t3 = "Refurbished Computers"
t4 = "Solar Panel Installation"
t5 = "Electric Cars"
t6 = "Windmill Installation"
t7 = "World Green Tech Event"
t8 = "Recycled Tech Plant"
names = [t1, t2, t3, t4, t5, t6, t7, t8]

# purchase status
t1s = 1
t2s = t3s = t4s = t5s = t6s = t7s = t8s = 0
statuses = [t1s, t2s, t3s, t4s, t5s, t6s, t7s, t8s]

# amount of task
a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = 1
amounts = [a1, a2, a3, a4, a5, a6, a7, a8]

# task box coordinates
boxW = 385
boxH = 100
boxRX = 100
boxRX2 = 515
boxY1 = 160
boxY2 = 295
boxY3 = 430
boxY4 = 565

# buy (investment) button coordinates
buyW = boxW / (4 / 3) / 1.4 + 6
buyH = boxH / 2
buyRX = boxRX + boxW / 4 - 5
buyRX2 = boxRX2 + boxW / 4 - 5
buyY1 = boxY1 + boxH / 2
buyY2 = boxY2 + boxH / 2
buyY3 = boxY3 + boxH / 2
buyY4 = boxY4 + boxH / 2

# endregion

# region MANAGERS
# manager names
m1 = "Jessica Bluewoman" # jesse pinkman
m2 = "Fade Dixon" # wade nixon
m3 = "Linux Bastion" # linus sebastian
m4 = "Mr. Best" # mrbeast
m5 = "Alan Mask" # elon musk
m6 = "Weston Aquawater" # wes bluemarine
m7 = "Tatiana Mongoose" # tana mongeau
m8 = "Jim Baker" # tim cook
manNames = [m1, m2, m3, m4, m5, m6, m7, m8]

# manager costs
m1c = 1000
m2c = 15000
m3c = 100000
m4c = 500000
m5c = 1200000
m6c = 10000000
m7c = 111111111
m8c = 555555555
manCosts = [m1c, m2c, m3c, m4c, m5c, m6c, m7c, m8c]

# purchase status
m1s = m2s = m3s = m4s = m5s = m6s = m7s = m8s = 0
manStats = [m1s, m2s, m3s, m4s, m5s, m6s, m7s, m8s]

# manager box coordinates
mBoxW = 425
mBoxH = 100
mBoxRX = 65
mBoxRX2 = 510
mBoxY1 = 215
mBoxY2 = mBoxY1 + 113.33
mBoxY3 = mBoxY2 + 113.33
mBoxY4 = mBoxY3 + 113.33

# endregion

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

# calculates task cost requirements (e.g. task 2 is $60)
def calcReqCost(n):
    if n == 1:
        final = 3.738317757
    else:
        final = baseMoney * (12 ** (n - 2))
    return final

def calcInvCost(n):
    if statuses[n - 1] == 0:
        final = (calcReqCost(n) * (1 - coefficients[n - 1]**buyMultiplier)) / (1 - coefficients[n-1])
    else:
        final = ((calcReqCost(n) * (coefficients[n - 1] ** amounts[n - 1])) * (1 - coefficients[n - 1]**buyMultiplier)) / (1 - coefficients[n-1])

    return final

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

multStatus = 0
buyMultiplier = 1

# function that centers text input - all parameters specified
def centerText(txt, font, col, x, y, w, h):
    a = txt
    aw, ah = font.size(a)
    aX = x + (w - aw) // 2
    aY = y + (h - ah) // 2
    ar = pygame.Rect(aX, aY, aw, ah)
    at = font.render(a, 1, col)
    screen.blit(at, ar)

def numberText(num, case):
    number = "%.2f" % num
    if num >= 1000000000000000:
        if case == 1:
            number = "%.2f Quadrillion" % (num/1000000000000000)
        else:
            number = "%.2fQ" % (num/1000000000000000)
    elif num >= 1000000000000:
        if case == 1:
            number = "%.2f Trillion" % (num/1000000000000)
        else:
            number = "%.2fT" % (num/1000000000000)
    elif num >= 1000000000:
        if case == 1:
            number = "%.2f Billion" % (num/1000000000)
        else:
            number = "%.2fB" % (num/1000000000)
    elif num >= 1000000:
        if case == 1:
            number = "%.2f Million" % (num/1000000)
        else:
            number = "%.2fM" % (num/1000000)
    elif num >= 1000:
        if case != 1:
            number = "%.2fK" % (num/1000)
    return number

# draws the task boxes
def task(statVar, x, y, n):
    global money

    button = pygame.Rect(x, y, boxW, boxH)

    if money >= calcInvCost(n) and statVar == 0:  # Can Buy - Buy Task turns Green
        pygame.draw.rect(screen, LIGHT1, button)
        centerText(names[n - 1], light, DARK4, x, y - 20, boxW, boxH)
        centerText(numberText(calcInvCost(n), 1), light, DARK4, x, y + 20, boxW, boxH)
    elif statVar == 0:  # Cannot Buy - Buy Task stays Black
        pygame.draw.rect(screen, LIGHT1, button, 2)
        centerText(names[n - 1], light, LIGHT1, x, y - 20, boxW, boxH)
        centerText(numberText(calcInvCost(n), 1), light, LIGHT1, x, y + 20, boxW, boxH)
    elif statVar == 1:  # Task is Bought...
        # COOLDOWN, AND ADD MONEY WHEN COOLDOWN ENDS
        if canClick[n-1] == False:
            cd = cooldowns[n-1] - (pygame.time.get_ticks() - timers[n-1])
            pygame.draw.rect(screen, DARK1, (x + boxW / 4, y+5, (boxW / (4 / 3) - 4) - (cd/(cooldowns[n-1]/(boxW / (4 / 3) - 4))), boxH / 2))
            secs = math.floor(cd/1000 % 60)
            mins = math.floor(cd/60000)
            if mins >= 1:
                cooldown = '%im %is' % (mins, secs)
            else:
                cooldown = '%is' % (secs)
            if cd <= 0:
                canClick[n-1] = True
                money += BIarr[n - 1] * amounts[n - 1]
                cooldown = "0s"
            centerText(cooldown, lightS, LIGHT1, x + boxW / 4 - 10 + boxW / (4 / 3) / 1.4 + 6, y + boxH / 2 + 1, boxW / (4.66) + 5, boxH / 2)
        else:
            cd = cooldowns[n-1]
            secs = math.floor(cd/1000 % 60)
            mins = math.floor(cd/60000)
            if mins >= 1:
                cooldown = '%im %is' % (mins, secs)
            else:
                cooldown = '%is' % (secs)
            centerText(cooldown, lightS, LIGHT1, x + boxW / 4 - 10 + boxW / (4 / 3) / 1.4 + 6, y + boxH / 2 + 1, boxW / (4.66) + 5, boxH / 2)

        # boxes
        pygame.draw.rect(screen, LIGHT1, (x, y, boxW, boxH), 5)  # whole task box
        pygame.draw.rect(screen, LIGHT1, (x, y, boxW / 4, boxH))  # left hand box
        pygame.draw.rect(
            screen,
            LIGHT1,
            (x + boxW / 4 - 5, y + boxH / 2, boxW / (4 / 3) + 6, boxH / 2),
            5,
        )  # bottom action box - Buy and Cooldown

        centerText(str(amounts[n - 1]), regularS, DARK4, x, y + boxH / 2, boxW / 4, boxH / 2)

        inc = BIarr[n - 1] * amounts[n - 1] # income
        centerText(numberText(inc, 0),regularS,LIGHT1,x + boxW / 4 - 5,y + 4,boxW / (4 / 3) + 7,boxH / 2)

        # INVESTMENT BUYING LOGIC
        if money >= calcInvCost(n):  # Can buy Investment - Buy button turns Green
            pygame.draw.rect(
                screen,
                LIGHT1,
                (x + boxW / 4 - 5, y + boxH / 2, boxW / (4 / 3) / 1.4 + 6, boxH / 2),
            )
            centerText(
                "Buy x%i - %s" % (buyMultiplier, numberText(calcInvCost(n), 0)),
                lightS,
                DARK4,
                x + boxW / 4 - 5,
                y + boxH / 2,
                boxW / (4 / 3) / 1.4 + 7,
                boxH / 2,
            )
        else:  # Can't Buy Investment - Buy button stays Black
            pygame.draw.rect(
                screen,
                LIGHT1,
                (x + boxW / 4 - 5, y + boxH / 2, boxW / (4 / 3) / 1.4 + 6, boxH / 2),
                5,
            )
            centerText(
                "Buy x%i - %s" % (buyMultiplier, numberText(calcInvCost(n), 0)),
                lightS,
                LIGHT1,
                x + boxW / 4 - 5,
                y + boxH / 2,
                boxW / (4 / 3) / 1.4 + 7,
                boxH / 2,
            )

def taskClick(n, x, y, bx, by):
    global money

    if mx > x and mx < x + boxW and my > y and my < y + boxH:
        if statuses[n - 1] == 0 and money >= calcInvCost(n):  # buy task
            statuses[n - 1] = 1
            amounts[n-1] = buyMultiplier
            money -= calcInvCost(n)
        elif (
            statuses[n - 1] == 1
            and money < calcInvCost(n)
            and mx > bx
            and mx < bx + buyW
            and my > by
            and my < by + buyH
        ):  # do nothing when pressing the buy button without sufficient funds
            return
        elif (
            statuses[n - 1] == 1
            and money >= calcInvCost(n)
            and mx > bx
            and mx < bx + buyW
            and my > by
            and my < by + buyH
        ):  # buy investment
            money -= calcInvCost(n)
            amounts[n - 1] += buyMultiplier
        elif statuses[n - 1] == 1:
            if canClick[n-1] == True:
                timers[n-1] = pygame.time.get_ticks()
                canClick[n-1] = False

def manager(mStatVar, x, y, n):
    global money

    pygame.draw.rect(screen, LIGHT1, (x, y, mBoxW, mBoxH), 2)  # whole task box
    pygame.draw.rect(screen, LIGHT1, (x, y, mBoxW*(4/5), mBoxH), 2)
    centerText(manNames[n-1],regularS,LIGHT1,x,y-30,mBoxW*(4/5),mBoxH)
    centerText("Runs " + names[n-1],lightS,LIGHT1,x,y,mBoxW*(4/5),mBoxH)
    centerText("$" + numberText(manCosts[n-1],1),regularS,LIGHT1,x,y+30,mBoxW*(4/5),mBoxH)
    pygame.draw.rect(screen, LIGHT1, (x+mBoxW*(4/5)-2, y, mBoxW*(1/5)+2, mBoxH), 2)
    centerText("Hire!",regularS,LIGHT1,x+mBoxW*(4/5)-2, y, mBoxW*(1/5)+2, mBoxH)

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
        if mx >= 865 and mx <= 985 and my >= 15 and my <= 60:
            multStatus += 1
            if multStatus == 1:
                buyMultiplier = 10
            elif multStatus == 2:
                buyMultiplier = 100
            elif multStatus == 3:
                multStatus = 0
                buyMultiplier = 1
        elif mx >= 865 and mx <= 985 and my >= 70 and my <= 115:
            if shopStatus == 0:
                shopStatus = 1
            elif shopStatus == 1:
                shopStatus = 0
        elif mx >= 875 and mx <= 975 and my >= 150 and my <= 200:
            if shopStatus == 1:
                shopStatus = 0

        button = 0

    # background
    screen.fill(DARK4)
    pygame.draw.rect(screen, LIGHT1, (1, 2, 999, 698), 2)

    ## HEADER ##

    # header and money
    pygame.draw.rect(screen, LIGHT1, (1, 1, 999, 125), 2)
    text = medium.render("$"+numberText(money, 1), 1, LIGHT1)
    screen.blit(text, (100,27.5))

    # buy multiplier button
    pygame.draw.rect(screen, LIGHT1, (865, 15, 120, 45))
    centerText("Buy x%i" % buyMultiplier, regularXS, DARK4, 865, 15, 120, 45)

    # shop
    pygame.draw.rect(screen, LIGHT1, (865, 70, 120, 45))
    centerText("Shop", regularXS, DARK4, 865, 70, 120, 45)


    # tasks
    count = 1
    for i in range(1, 9):
        if i == 5:
            count = 1
        yPos = [boxY1, boxY2, boxY3, boxY4]
        if i < 5:
            task(statuses[i - 1], boxRX, yPos[count - 1], i)
            count += 1
        else:
            task(statuses[i - 1], boxRX2, yPos[count - 1], i)
            count += 1

    # shop
    if shopStatus == 1:
        pygame.draw.rect(screen, DARK4, (25, 150, 950, 525))
        pygame.draw.rect(screen, LIGHT1, (25, 150, 950, 525), 5)
        pygame.draw.rect(screen, LIGHT1, (25, 150, 950, 50), 5)
        pygame.draw.rect(screen, LIGHT1, (875, 150, 100, 50))
        centerText("X",regularS,DARK4,875,150+2,100,50)
    
        count = 1
        for i in range(1, 9):
            if i == 5:
                count = 1
            yPos = [mBoxY1, mBoxY2, mBoxY3, mBoxY4]
            if i < 5:
                manager(manStats[i - 1], mBoxRX, yPos[count - 1], i)
                count += 1
            else:
                manager(manStats[i - 1], mBoxRX2, yPos[count - 1], i)
                count += 1

    pygame.display.update()
    clock.tick(60)

pygame.quit()
