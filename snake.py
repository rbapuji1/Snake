#NEW CHANGE

import pygame as pg
import random as r

pg.init()
 
WHITE  = (255, 255, 255)
YELLOW = (252, 192,   3)
BLACK  = (  0,   0,   0)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = ( 12,  16,  97)
 
screen_w = 600
screen_h = 400
score_h = 50

ICON = pg.image.load('snake-icon.png')
pg.display.set_icon(ICON)

 
screen = pg.display.set_mode((screen_w, screen_h + score_h))
pg.display.set_caption('Snake')
 
clock = pg.time.Clock()
 
snakeBlock = 10
snakeSpeed = 15
 
mainfont = pg.font.Font("scorefont.ttf", 30)

def scorePanel(score, best):
    pg.draw.rect(screen, BLUE, [0, screen_h, screen_w, score_h])
    printScore(score)
    printBest(score)

def printScore(score):
    value = mainfont.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [470, screen_h])

def printBest(best):
    value = mainfont.render("Best: " + str(best), True, WHITE)
    screen.blit(value, [20, screen_h])
 
def drawSnake(snakeBlock, snakeList):
    for x in snakeList:
        pg.draw.rect(screen, GREEN, [x[0], x[1], snakeBlock, snakeBlock])
 
def finalmsg():
    yl = mainfont.render("You Lost!", True, YELLOW)
    options = mainfont.render("SPACE - Play Again   Q - Quit", True, YELLOW)

    screen.blit(yl, [230,125])
    screen.blit(options, [120, 175])
 
def gameLoop(bestScore):
    gameOver = False
    gameClose = False
 
    x1 = screen_w / 2
    y1 = screen_h / 2
 
    x1_v = 0
    y1_v = 0
 
    snakeList = []
    snakeLength = 1
 
    applex = int(r.randrange(0, screen_w - snakeBlock) / 10.0) * 10
    appley = int(r.randrange(0, screen_h - snakeBlock) / 10.0) * 10

    
 
    while not gameOver:
 
        while gameClose == True:
            screen.fill(BLACK)
            finalmsg()
            printScore(snakeLength - 1)
            pg.display.update()
 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameOver = True
                    gameClose = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pg.K_SPACE:
                        gameLoop(bestScore)
 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameOver = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    if x1_v == 0 or snakeLength == 1:
                        x1_v = -snakeBlock
                        y1_v = 0
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    if x1_v == 0 or snakeLength == 1:
                        x1_v = snakeBlock
                        y1_v = 0
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    if y1_v == 0 or snakeLength == 1:
                        y1_v = -snakeBlock
                        x1_v = 0
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    if y1_v == 0 or snakeLength == 1:
                        y1_v = snakeBlock
                        x1_v = 0
 
        if x1 >= screen_w or x1 < 0 or y1 >= screen_h or y1 < 0:
            gameClose = True

        x1 += x1_v
        y1 += y1_v

        screen.fill(BLACK)

        # APPLE
        pg.draw.rect(screen, RED, [applex, appley, snakeBlock, snakeBlock])

        snakeHead = [x1, y1]

        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]
 
        # head meets tail
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True
 
        drawSnake(snakeBlock, snakeList)

        score = snakeLength - 1

        if score > bestScore:
            bestScore = score

        scorePanel(score, bestScore)

        pg.display.update()
 
        if x1 == applex and y1 == appley:
            applex = int(r.randrange(0, screen_w - snakeBlock) / 10.0) * 10
            appley = int(r.randrange(0, screen_h - snakeBlock) / 10.0) * 10
            snakeLength += 1
 
        clock.tick(snakeSpeed)
 
    pg.quit()
    quit()


if __name__ == "__main__":
    bestScore = 0
    gameLoop(bestScore)
