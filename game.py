# GAME INSPIRED BY ADVENTURE CAPITALIST #
# MATHEMATICAL SOURCES USED BELOW #
# https://www.youtube.com/watch?v=Ogdo271YWsw #
# https://adventure-capitalist.fandom.com/wiki/Businesses #
# https://adventure-capitalist.fandom.com/wiki/Cash_Upgrades #
# https://adventure-capitalist.fandom.com/wiki/Unlocks_(Earth) #
# SAME (or similar) MATHEMATICAL FORMULAS AS ADVENTURE CAPITALIST ARE USED! #
# 911 LINES TOTAL WRITEN! #

"""
                  ICS3U1-FPT :                              Total
                 Editor time :                            5.8 hrs
            Active code time :                            2.8 hrs
         Lines of code added :                              1,451
       Lines of code deleted :                                680
            Total keystrokes :                             21,300
"""

# region PYGAME
import pygame
import math
import webbrowser

pygame.init()
screen = pygame.display.set_mode((1000, 700))  # width 1000, height 700

# icon and window title

pygame.display.set_caption("ByteBucks")

pygame_icon = pygame.image.load("./assets/images/icon_512x512@2x.png")
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
lightXS = pygame.font.Font("./assets/fonts/ChakraPetch-Light.ttf", 21)

# endregion

# region MUSIC
music = 1  # turns music on or off, DEFAULT 1

# background music
bgm = pygame.mixer.music.load("./assets/sounds/bgm.mp3")
pygame.mixer.music.set_volume(0.5)

# sound effects
buy = pygame.mixer.Sound("./assets/sounds/buy.wav")
toggle = pygame.mixer.Sound("./assets/sounds/toggle_click.wav")
upgrade = pygame.mixer.Sound("./assets/sounds/upgrade.wav")

if music == 1:
    pygame.mixer.music.play(-1)

# endregion

# region IMAGES
i1 = pygame.transform.scale(pygame.image.load("./assets/images/icons/1.png"),(60,60))
i2 = pygame.transform.scale(pygame.image.load("./assets/images/icons/2.png"),(60,60))
i3 = pygame.transform.scale(pygame.image.load("./assets/images/icons/3.png"),(60,60))
i4 = pygame.transform.scale(pygame.image.load("./assets/images/icons/4.png"),(60,60))
i5 = pygame.transform.scale(pygame.image.load("./assets/images/icons/5.png"),(60,60))
i6 = pygame.transform.scale(pygame.image.load("./assets/images/icons/6.png"),(60,60))
i7 = pygame.transform.scale(pygame.image.load("./assets/images/icons/7.png"),(60,60))
i8 = pygame.transform.scale(pygame.image.load("./assets/images/icons/8.png"),(60,60))
images = [i1, i2, i3, i4, i5, i6, i7, i8]
    
# endregion

# region STATES
CHEAT = 0  # sets base income crazy high for testing purposes if true, DEFAULT 0
button = 0  # button pressed
shopStatus = 0  # shop opened or closed
sMenuStatus = 0  # manager or upgrade window

# endregion

# region COOLDOWNS
clock = pygame.time.Clock()

s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = True  # click statuses
tm1 = (
    tm2
) = (
    tm3
) = (
    tm4
) = tm5 = tm6 = tm7 = tm8 = pygame.time.get_ticks()  # timers used for cooldown math

# cooldowns (in ms)
c1 = 0.6 * 1000
c2 = 2 * 1000
c3 = 4 * 1000
c4 = 8 * 1000
c5 = 16 * 1000
c6 = 32 * 1000
c7 = 64 * 1000
c8 = 128 * 1000

canClick = [s1, s2, s3, s4, s5, s6, s7, s8]
timers = [tm1, tm2, tm3, tm4, tm5, tm6, tm7, tm8]
cooldowns = [c1, c2, c3, c4, c5, c6, c7, c8]

# endregion

# region TASKS
# task names
t1 = "Recycled Cables"
t2 = "Battery Recycling"
t3 = "Refurbished Computers"
t4 = "Solar Panel Installation"
t5 = "Electric Cars"
t6 = "Wind Turbine Installation"
t7 = "World Green Tech Event"
t8 = "Recycled Tech Facility"
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
m1 = "Jessica Bluewoman"  # jesse pinkman
m2 = "Fade Dixon"  # wade nixon
m3 = "Linux Bastion"  # linus sebastian
m4 = "Mr. Best"  # mrbeast
m5 = "Alan Mask"  # elon musk
m6 = "Weston Aquawater"  # wes bluemarine
m7 = "Tatiana Mongoose"  # tana mongeau
m8 = "Jim Baker"  # tim cook
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

# region UPGRADES
# upgrade names
u1 = "Cable Ties"
u2 = "Phone Batteries"
u3 = "Gaming Computers"
u4 = "Solar Farm"
u5 = "Autopilot"
u6 = "Delta4000 Turbine"  # wes bluemarine
u7 = "Big Corporations"  # tana mongeau
u8 = "Green Robots"  # tim cook
upNames = [u1, u2, u3, u4, u5, u6, u7, u8]

# upgrade costs
u1c = 250000
u2c = 500000
u3c = 1000000
u4c = 5000000
u5c = 10000000
u6c = 25000000
u7c = 500000000
u8c = 10000000000
upCosts = [u1c, u2c, u3c, u4c, u5c, u6c, u7c, u8c]

# purchase status
u1s = u2s = u3s = u4s = u5s = u6s = u7s = u8s = 0
upStats = [u1s, u2s, u3s, u4s, u5s, u6s, u7s, u8s]

# endregion

# region UNLOCKS

# unlock statuses of each milestone
us11 = us12 = us13 = us14 = us15 = us16 = us17 = us18 = 0  # 25
us21 = us22 = us23 = us24 = us25 = us26 = us27 = us28 = 0  # 50
us31 = us32 = us33 = us34 = us35 = us36 = us37 = us38 = 0  # 100
us41 = us42 = us43 = us44 = us45 = us46 = us47 = us48 = 0  # 200
us51 = us52 = us53 = us54 = us55 = us56 = us57 = us58 = 0  # 300
us61 = us62 = us63 = us64 = us65 = us66 = us67 = us68 = 0  # 400
us71 = us72 = us73 = us74 = us75 = us76 = us77 = us78 = 0  # 500

unlocks1 = [us11, us12, us13, us14, us15, us16, us17, us18]
unlocks2 = [us21, us22, us23, us24, us25, us26, us27, us28]
unlocks3 = [us31, us32, us33, us34, us35, us36, us37, us38]
unlocks4 = [us41, us42, us43, us44, us45, us46, us47, us48]
unlocks5 = [us51, us52, us53, us54, us55, us56, us57, us58]
unlocks6 = [us61, us62, us63, us64, us65, us66, us67, us68]
unlocks7 = [us71, us72, us73, us74, us75, us76, us77, us78]

# endregion

# region MONEY


# calculates task cost requirements (e.g. task 2 is $60)
def calcReqCost(n):
    if n == 1:
        final = 3.738317757
    else:
        final = baseMoney * (12 ** (n - 2))
    return final


# calculates investment cost requirements, also used for displaying prices with multipliers
def calcInvCost(n):
    if statuses[n - 1] == 0:
        final = (calcReqCost(n) * (1 - coefficients[n - 1] ** buyMultiplier)) / (
            1 - coefficients[n - 1]
        )
    else:
        final = (
            (calcReqCost(n) * (coefficients[n - 1] ** amounts[n - 1]))
            * (1 - coefficients[n - 1] ** buyMultiplier)
        ) / (1 - coefficients[n - 1])

    return final


# base money amounts
money = 0.00  # total money
baseMoney = 60.00  # base money - for calculations

# coefficients constant, for investment cost calculation
CF1 = 1.07
CF2 = 1.15
CF3 = 1.14
CF4 = 1.13
CF5 = 1.12
CF6 = 1.11
CF7 = 1.10
CF8 = 1.09
coefficients = [CF1, CF2, CF3, CF4, CF5, CF6, CF7, CF8]

# base income of each task
if CHEAT == 0:
    BI1 = 1.00
else:
    BI1 = 10**15
BI2 = calcReqCost(2)
BI3 = calcReqCost(3) * 0.75
BI4 = calcReqCost(4) * 0.5
BI5 = calcReqCost(5) * 0.5
BI6 = calcReqCost(6) * 0.5
BI7 = calcReqCost(7) * 0.5
BI8 = calcReqCost(8) * 0.5
BIarr = [BI1, BI2, BI3, BI4, BI5, BI6, BI7, BI8]

multStatus = 0  # buy multiplier status
buyMultiplier = 1  # buy multiplier (1, 10, 100)

# endregion

# region MAIN FUNCTIONS


# function that centers text input - all parameters specified
def centerText(txt, font, col, x, y, w, h):
    a = txt
    aw, ah = font.size(a)
    aX = x + (w - aw) // 2
    aY = y + (h - ah) // 2
    ar = pygame.Rect(aX, aY, aw, ah)
    at = font.render(a, 1, col)
    screen.blit(at, ar)


# converts normal numbers to text (e.g. 1000000 -> 1 million)
def numberText(num, case):
    number = "%.2f" % num
    if num >= 10**33:
        if case == 1:
            number = "%.2f Decillion" % (num / 10**33)
        else:
            number = "%.2fD" % (num / 10**33)
    elif num >= 10**30:
        if case == 1:
            number = "%.2f Nonillion" % (num / 10**30)
        else:
            number = "%.2fN" % (num / 10**30)
    elif num >= 10**27:
        if case == 1:
            number = "%.2f Octillion" % (num / 10**27)
        else:
            number = "%.2fO" % (num / 10**27)
    elif num >= 10**24:
        if case == 1:
            number = "%.2f Septillion" % (num / 10**24)
        else:
            number = "%.2fS" % (num / 10**24)
    elif num >= 10**21:
        if case == 1:
            number = "%.2f Sextillion" % (num / 10**21)
        else:
            number = "%.2fs" % (num / 10**21)
    elif num >= 10**18:
        if case == 1:
            number = "%.2f Quintillion" % (num / 10**18)
        else:
            number = "%.2fQ" % (num / 10**18)
    elif num >= 10**15:
        if case == 1:
            number = "%.2f Quadrillion" % (num / 10**15)
        else:
            number = "%.2fq" % (num / 10**15)
    elif num >= 10**12:
        if case == 1:
            number = "%.2f Trillion" % (num / 10**12)
        else:
            number = "%.2fT" % (num / 10**12)
    elif num >= 10**9:
        if case == 1:
            number = "%.2f Billion" % (num / 10**9)
        else:
            number = "%.2fB" % (num / 10**9)
    elif num >= 10**6:
        if case == 1:
            number = "%.2f Million" % (num / 10**6)
        else:
            number = "%.2fM" % (num / 10**6)
    elif num >= 10**3:
        if case != 1:
            number = "%.2fK" % (num / 10**3)
    return number


# draws the task boxes, and everything that happens within a task
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
        # region COOLDOWNS
        if (
            canClick[n - 1] == False
        ):  # if the cooldown is currently going on (you cant click the task)
            cd = cooldowns[n - 1] - (pygame.time.get_ticks() - timers[n - 1])
            if (boxW / (4 / 3) - 4) - (
                cd / (cooldowns[n - 1] / (boxW / (4 / 3) - 4))
            ) >= (
                boxW / (4 / 3) - 4
            ):  # if the cooldown bar exceeds the overall box, set it to a max value
                pygame.draw.rect(
                    screen,
                    DARK1,
                    (
                        x + boxW / 4,
                        y + 5,
                        (boxW / (4 / 3) - 4),
                        boxH / 2,
                    ),
                )
            else:
                pygame.draw.rect(
                    screen,
                    DARK1,
                    (
                        x + boxW / 4,
                        y + 5,
                        (boxW / (4 / 3) - 4)
                        - (cd / (cooldowns[n - 1] / (boxW / (4 / 3) - 4))),
                        boxH / 2,
                    ),
                )
            secs = math.floor(cd / 1000 % 60)
            mins = math.floor(cd / 60000)
            if mins >= 1:  # if higher than 1 minute
                cooldown = "%im %is" % (mins, secs)
            else:
                cooldown = "%is" % (secs)
            if cd <= 0:  # when cooldown is up
                canClick[n - 1] = True
                money += BIarr[n - 1] * amounts[n - 1]
                cooldown = "0s"
            centerText(
                cooldown,
                lightS,
                LIGHT1,
                x + boxW / 4 - 10 + boxW / (4 / 3) / 1.4 + 6,
                y + boxH / 2 + 1,
                boxW / (4.66) + 5,
                boxH / 2,
            )
        else:  # when task isnt running - static
            if manStats[n - 1] == 1:
                canClick[n - 1] = False
                timers[n - 1] = pygame.time.get_ticks()
            cd = cooldowns[n - 1]
            secs = math.floor(cd / 1000 % 60)
            mins = math.floor(cd / 60000)
            if mins >= 1:
                cooldown = "%im %is" % (mins, secs)
            else:
                cooldown = "%is" % (secs)
            centerText(
                cooldown,
                lightS,
                LIGHT1,
                x + boxW / 4 - 10 + boxW / (4 / 3) / 1.4 + 6,
                y + boxH / 2 + 1,
                boxW / (4.66) + 5,
                boxH / 2,
            )

        # endregion

        # region BOXES
        pygame.draw.rect(screen, LIGHT1, (x, y, boxW, boxH), 5)  # whole task box
        pygame.draw.rect(screen, LIGHT1, (x, y, boxW / 4, boxH))  # left hand box
        pygame.draw.rect(
            screen,
            LIGHT1,
            (x + boxW / 4 - 5, y + boxH / 2, boxW / (4 / 3) + 6, boxH / 2),
            5,
        )  # bottom action box - Buy and Cooldown

        screen.blit(images[n-1],(x + 17.5, y)) # show icon
        centerText(
            str(amounts[n - 1]), regularS, DARK4, x, y + boxH / 2, boxW / 4, boxH / 2
        )  # amount of investments

        inc = BIarr[n - 1] * amounts[n - 1]  # income
        centerText(
            numberText(inc, 0),
            regularS,
            LIGHT1,
            x + boxW / 4 - 5,
            y + 4,
            boxW / (4 / 3) + 7,
            boxH / 2,
        )

        # endregion

        # region INVESTMENT BUTTON
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

        # endregion

        # region MILESTONES
        if amounts[n - 1] >= 25 and unlocks1[n - 1] == 0:
            cooldowns[n - 1] /= 2
            unlocks1[n - 1] = 1
            upgrade.play()
        if amounts[n - 1] >= 50 and unlocks2[n - 1] == 0:
            cooldowns[n - 1] /= 2
            unlocks2[n - 1] = 1
            upgrade.play()
        if amounts[n - 1] >= 100 and unlocks3[n - 1] == 0:
            cooldowns[n - 1] /= 2
            unlocks3[n - 1] = 1
            upgrade.play()
        if amounts[n - 1] >= 200 and unlocks4[n - 1] == 0:
            cooldowns[n - 1] /= 2
            unlocks4[n - 1] = 1
            upgrade.play()
        if amounts[n - 1] >= 300 and unlocks5[n - 1] == 0:
            cooldowns[n - 1] /= 2
            unlocks5[n - 1] = 1
            upgrade.play()
        if amounts[n - 1] >= 400 and unlocks6[n - 1] == 0:
            cooldowns[n - 1] /= 2
            unlocks6[n - 1] = 1
            upgrade.play()
        if amounts[n - 1] >= 500 and unlocks7[n - 1] == 0:
            if n == 1:
                BIarr[n - 1] *= 4
            elif n == 2:
                BIarr[6 - 1] *= 11
            else:
                BIarr[n - 1] *= 2
            unlocks7[n - 1] = 1
            upgrade.play()

        # endregion


# manages what happens when you click a task
def taskClick(n, x, y, bx, by):
    global money

    if (
        mx > x and mx < x + boxW and my > y and my < y + boxH and shopStatus == 0
    ):  # regular mode - buying tasks (shop cant be enabled)
        if statuses[n - 1] == 0 and money >= calcInvCost(n):  # buy task
            money -= calcInvCost(n)
            statuses[n - 1] = 1
            amounts[n - 1] = buyMultiplier
            buy.play()
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
            buy.play()
        elif statuses[n - 1] == 1:  # start cooldown!!
            if canClick[n - 1] == True:
                timers[n - 1] = pygame.time.get_ticks()
                canClick[n - 1] = False


# draws the shop
def shop(x, y, n):
    global money

    if (
        sMenuStatus == 0 and manStats[n - 1] == 0
    ):  # if on managers page and the manager hasnt been bought
        pygame.draw.rect(screen, LIGHT1, (x, y, mBoxW, mBoxH), 2)  # whole task box
        pygame.draw.rect(
            screen, LIGHT1, (x, y, mBoxW * (4 / 5), mBoxH), 2
        )  # information box
        centerText(manNames[n - 1], regularS, LIGHT1, x, y - 30, mBoxW * (4 / 5), mBoxH)
        centerText("Runs " + names[n - 1], lightS, LIGHT1, x, y, mBoxW * (4 / 5), mBoxH)
        centerText(
            "$" + numberText(manCosts[n - 1], 1),
            regularS,
            LIGHT1,
            x,
            y + 30,
            mBoxW * (4 / 5),
            mBoxH,
        )
        if (
            money >= manCosts[n - 1] and manStats[n - 1] != 1
        ):  # dark hire button if cant afford
            pygame.draw.rect(
                screen, LIGHT1, (x + mBoxW * (4 / 5) - 2, y, mBoxW * (1 / 5) + 2, mBoxH)
            )  # hire button
            centerText(
                "Hire!",
                regularS,
                DARK4,
                x + mBoxW * (4 / 5) - 2,
                y,
                mBoxW * (1 / 5) + 2,
                mBoxH,
            )
        else:  # light hire button to buy (can afford)
            pygame.draw.rect(
                screen,
                LIGHT1,
                (x + mBoxW * (4 / 5) - 2, y, mBoxW * (1 / 5) + 2, mBoxH),
                2,
            )  # hire button
            centerText(
                "Hire!",
                regularS,
                LIGHT1,
                x + mBoxW * (4 / 5) - 2,
                y,
                mBoxW * (1 / 5) + 2,
                mBoxH,
            )
    elif sMenuStatus == 1 and upStats[n - 1] == 0:  # upgrades instead of managers
        pygame.draw.rect(screen, LIGHT1, (x, y, mBoxW, mBoxH), 2)  # whole task box
        pygame.draw.rect(
            screen, LIGHT1, (x, y, mBoxW * (4 / 5), mBoxH), 2
        )  # information box
        centerText(upNames[n - 1], regularS, LIGHT1, x, y - 30, mBoxW * (4 / 5), mBoxH)
        centerText(
            names[n - 1] + " profit x3", lightXS, LIGHT1, x, y, mBoxW * (4 / 5), mBoxH
        )
        centerText(
            "$" + numberText(upCosts[n - 1], 1),
            regularS,
            LIGHT1,
            x,
            y + 30,
            mBoxW * (4 / 5),
            mBoxH,
        )
        if money >= upCosts[n - 1] and upStats[n - 1] != 1:
            pygame.draw.rect(
                screen, LIGHT1, (x + mBoxW * (4 / 5) - 2, y, mBoxW * (1 / 5) + 2, mBoxH)
            )  # buy button
            centerText(
                "Buy!",
                regularS,
                DARK4,
                x + mBoxW * (4 / 5) - 2,
                y,
                mBoxW * (1 / 5) + 2,
                mBoxH,
            )
        else:
            pygame.draw.rect(
                screen,
                LIGHT1,
                (x + mBoxW * (4 / 5) - 2, y, mBoxW * (1 / 5) + 2, mBoxH),
                2,
            )  # buy button
            centerText(
                "Buy!",
                regularS,
                LIGHT1,
                x + mBoxW * (4 / 5) - 2,
                y,
                mBoxW * (1 / 5) + 2,
                mBoxH,
            )


# manages what happens when you click a shop element
def shopClick(x, y, n):
    global money

    if (
        money >= manCosts[n - 1] and manStats[n - 1] != 1 and sMenuStatus == 0
    ):  # if can buy a manager!
        if (
            button == 1
            and mx >= x + mBoxW * (4 / 5) - 2
            and mx <= x + mBoxW * (4 / 5) - 2 + mBoxW * (1 / 5) + 2
            and my >= y
            and my <= y + mBoxH
        ):
            manStats[n - 1] = 1
            money -= manCosts[n - 1]
            upgrade.play()
    elif (
        money >= upCosts[n - 1] and upStats[n - 1] != 1 and sMenuStatus == 1
    ):  # if can buy an upgrade!
        if (
            button == 1
            and mx >= x + mBoxW * (4 / 5) - 2
            and mx <= x + mBoxW * (4 / 5) - 2 + mBoxW * (1 / 5) + 2
            and my >= y
            and my <= y + mBoxH
        ):
            upStats[n - 1] = 1
            money -= upCosts[n - 1]
            BIarr[n - 1] *= 3
            upgrade.play()


# endregion

playing = True
while playing:
    for event in pygame.event.get():  # pygame events
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            button = event.button

    if button == 1:  # button pressed
        count = 1
        for i in range(1, 9):  # check for clicks for TASKS
            if i == 5:
                count = 1
            yPos = [boxY1, boxY2, boxY3, boxY4, buyY4, buyY3, buyY2, buyY1]
            if i < 5:
                taskClick(i, boxRX, yPos[count - 1], buyRX, yPos[-count])
                count += 1
            else:
                taskClick(i, boxRX2, yPos[count - 1], buyRX2, yPos[-count])
                count += 1
        if shopStatus == 1:  # check for clicks for SHOP
            count = 1
            for i in range(1, 9):
                if i == 5:
                    count = 1
                yPos = [mBoxY1, mBoxY2, mBoxY3, mBoxY4]
                if i < 5:
                    shopClick(mBoxRX, yPos[count - 1], i)
                    count += 1
                else:
                    shopClick(mBoxRX2, yPos[count - 1], i)
                    count += 1
        if (
            mx >= 865 and mx <= 985 and my >= 15 and my <= 60
        ):  # header - buy multiplier button
            multStatus += 1
            if multStatus == 1:
                buyMultiplier = 10
            elif multStatus == 2:
                buyMultiplier = 100
            elif multStatus == 3:
                multStatus = 0
                buyMultiplier = 1
            toggle.play()
        elif (
            mx >= 865 and mx <= 985 and my >= 70 and my <= 115
        ):  # shop button - open and close
            if shopStatus == 0:
                shopStatus = 1
            elif shopStatus == 1:
                shopStatus = 0
            buy.play()
        elif (
            mx >= 875 and mx <= 975 and my >= 150 and my <= 200
        ):  # shop X button - close shop
            if shopStatus == 1:
                shopStatus = 0
        elif (
            mx >= 25 and mx <= 175 and my >= 150 and my <= 200 and shopStatus == 1
        ):  # switch to managers in shop
            sMenuStatus = 0
        elif (
            mx >= 175 and mx <= 325 and my >= 150 and my <= 200 and shopStatus == 1
        ):  # switch to upgrades in shop
            sMenuStatus = 1
        elif mx >= 735 and mx <= 855 and my >= 15 and my <= 60:  # save button
            file = open("save.txt", "w")
            file.write(str(money))
            file.close()
        elif mx >= 735 and mx <= 855 and my >= 70 and my <= 115:  # load button
            file = open("save.txt", "r")
            money = float(file.read())
            file.close()
        elif mx >= 605 and mx <= 725 and my >= 15 and my <= 60:  # music button
            if music == 1:
                music = 0
                pygame.mixer.music.stop()
            else:
                music = 1
                pygame.mixer.music.play(-1)
        elif mx >= 605 and mx <= 725 and my >= 70 and my <= 115:  # instructions button
            webbrowser.open(
                "https://github.com/anthonyhuang07/ICS3U1-FPT/blob/main/docs/instructions.md"
            )

        button = 0

    # background
    screen.fill(DARK4)
    pygame.draw.rect(screen, LIGHT1, (1, 2, 999, 698), 2)

    # region HEADER

    # header and money
    pygame.draw.rect(screen, LIGHT1, (1, 1, 999, 125), 2)
    text = medium.render("$" + numberText(money, 1), 1, LIGHT1)
    screen.blit(text, (100, 27.5))

    # buy multiplier button
    pygame.draw.rect(screen, LIGHT1, (865, 15, 120, 45))
    centerText("Buy x%i" % buyMultiplier, regularXS, DARK4, 865, 15, 120, 45)

    # shop
    pygame.draw.rect(screen, LIGHT1, (865, 70, 120, 45))
    centerText("Shop", regularXS, DARK4, 865, 70, 120, 45)

    # save button
    pygame.draw.rect(screen, LIGHT1, (735, 15, 120, 45))
    centerText("Save", regularXS, DARK4, 735, 15, 120, 45)

    # load button
    pygame.draw.rect(screen, LIGHT1, (735, 70, 120, 45))
    centerText("Load", regularXS, DARK4, 735, 70, 120, 45)

    # music button
    pygame.draw.rect(screen, LIGHT1, (605, 15, 120, 45))
    centerText("Music", regularXS, DARK4, 605, 15, 120, 45)

    # instructions button
    pygame.draw.rect(screen, LIGHT1, (605, 70, 120, 45))
    centerText("Help", regularXS, DARK4, 605, 70, 120, 45)

    # endregion

    # tasks
    count = 1
    for i in range(1, 9):  # creates task boxes from 1 to 9
        if i == 5:
            count = 1
        yPos = [boxY1, boxY2, boxY3, boxY4]
        if i < 5:
            task(statuses[i - 1], boxRX, yPos[count - 1], i)
            count += 1
        else:
            task(statuses[i - 1], boxRX2, yPos[count - 1], i)
            count += 1

    # shop - draw
    if shopStatus == 1:
        pygame.draw.rect(screen, DARK4, (25, 150, 950, 525))
        pygame.draw.rect(screen, LIGHT1, (25, 150, 950, 525), 5)
        pygame.draw.rect(screen, LIGHT1, (25, 150, 950, 50), 5)
        pygame.draw.rect(screen, LIGHT1, (875, 150, 100, 50))
        centerText("X", regularS, DARK4, 875, 150 + 2, 100, 50)
        if sMenuStatus == 0:
            pygame.draw.rect(screen, LIGHT1, (25, 150, 150, 50))
            centerText("Managers", regularS, DARK4, 25, 150, 150, 50)
            pygame.draw.rect(screen, LIGHT1, (175 - 5, 150, 150, 50), 5)
            centerText("Upgrades", regularS, LIGHT1, 175 - 5, 150, 150, 50)
        else:
            pygame.draw.rect(screen, LIGHT1, (25, 150, 150, 50), 5)
            centerText("Managers", regularS, LIGHT1, 25, 150, 150, 50)
            pygame.draw.rect(screen, LIGHT1, (175 - 5, 150, 150, 50))
            centerText("Upgrades", regularS, DARK4, 175 - 5, 150, 150, 50)

        count = 1
        for i in range(1, 9):
            if i == 5:
                count = 1
            yPos = [mBoxY1, mBoxY2, mBoxY3, mBoxY4]
            if i < 5:
                shop(mBoxRX, yPos[count - 1], i)
                count += 1
            else:
                shop(mBoxRX2, yPos[count - 1], i)
                count += 1

    pygame.display.update()
    clock.tick(60)

pygame.quit()
