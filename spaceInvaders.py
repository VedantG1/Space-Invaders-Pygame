import pygame as pg
import random
import math as m
from pygame import mixer

pg.init()
# saving this for easyness
myDisplay = pg.display
screen = myDisplay.set_mode((800, 600))

# setting title
myDisplay.set_caption("Space Invaders")

# setting icon
icon = pg.image.load("ufo.png")
myDisplay.set_icon(icon)

# player
playerIMG = pg.image.load("player.png")
playerY = 480
playerX = 370
pnewX = 0

# enemy
enemyIMG = []
enemyX = []
enemyY = []
enewX = []
enewY = []
numOfEnemies = 6

for i in range(numOfEnemies):
    enemyIMG.append(pg.image.load("enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enewX.append(3)
    enewY.append(40)

# bullet
bulletIMG = pg.image.load("bullet.png")
bulletX = 0
bulletY = 480
bnewX = 0
bnewY = 5
bulletState = "ready"  # ready - bullet can't be seen, fire - bullet now moving

# background
bg = pg.image.load("background.png")

# background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# score
score_value = 0
font = pg.font.Font("D:/IDM Download/Compressed/Dosis/static/Dosis-Bold.ttf", 32)
textX = 10
textY = 10

# game over
overFont = pg.font.Font("D:/IDM Download/Compressed/Dosis/static/Dosis-Bold.ttf", 64)


def showScore(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def gameOverText():
    overText = overFont.render("Game Over!", True, (255, 255, 255))
    screen.blit(overText, (250, 250))


def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))


def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletIMG, (x, y))


def isCollision(bulletX, bulletY, enemyX, enemyY):
    distance = m.sqrt((m.pow(enemyX - bulletX, 2)) + (m.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# for running the windows forever
running = True
while running:
    # RGB Background
    screen.fill((0, 0, 0))
    # background
    screen.blit(bg, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("Game Quited!")
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                pnewX = -5
            if event.key == pg.K_RIGHT:
                pnewX = 5
            if event.key == pg.K_SPACE:
                if bulletState == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                pnewX = 0
    # check for boundries
    playerX += pnewX
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    for i in range(numOfEnemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(numOfEnemies):
                enemyY[j] = 2000
            gameOverText()
            break

        enemyX[i] += enewX[i]
        if enemyX[i] <= 0:
            enewX[i] = 3
            enemyY[i] += enewY[i]
        elif enemyX[i] >= 736:
            enewX[i] = -3
            enemyY[i] += enewY[i]
        # Collision
        collision = isCollision(bulletX, bulletY, enemyX[i], enemyY[i])
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"

    if bulletState == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bnewY

    player(playerX, playerY)
    showScore(textX, textY)
    pg.display.update()






























# Made By - Vedant Gupta
# Discord ID - dumb#5886
#Email - vedantguptaca@gmail.co