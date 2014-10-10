#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import thread
import time
import Queue

from InputWindows import Input
from Explosion import Explosion
from MObject import MObject
from Ship import Ship
from Bullet import Bullet
from AstroidClass import AstroidClass
from AstroidSpawner import AstroidSpawner

inputThread = Input()
inputThread.start()

ship = Ship(12, 12)

width=25*3
height=25*2
canvas = verts = [["E" for x in range(width)] for y in range(height)]

mObjects = []
mObjects.append(ship)

explosions = []

astroidSpawner = AstroidSpawner(width, height)

string = ""

lost = "not lost"

def collideWall():
    if(ship.posX >= width - 6 + ship.width - 1 or ship.posX <= 2):
        return True
    if(ship.posY >= height - 4 + ship.height - 1 or ship.posY <= 1):
        return True
    return False

def collision():
    pos = ship.collision(mObjects)
    if(pos != None):
        explosions.append(Explosion(pos[0], pos[1]))
        global lost
        loose = "lost"

def fillCanvas():
    #Clear canvas
    y = 0
    while(y < height):
        x = 0
        while(x < width):
            if(0<=y and y<2 or height-2<=y and y<height):
                canvas[y][x] =  "B"
            elif(0<=x and x<3 or width-3<=x and x<width):
                canvas[y][x] =  "B"
            else:
                canvas[y][x] =  " "
            x+=1
        y+=1
    #Paint mObjects
    for mObject in mObjects:
        mObject.paint(canvas, width, height)
    for explosion in explosions:
        if(explosion.paint(canvas, width, height)):
            explosions.remove(explosion)

def typeCanvas():
    s = ""
    for row in canvas:
        for c in row:
            s += c
        s += "\n"
    return s

run = "True"
while not not run:

    #Get input
    chars = inputThread.getChars()
    while not chars.empty():
        char = chars.get()
        if char==113:
            inputThread.join()
            run = False
        elif char==75: #left
            ship.posX-=3
            if(collideWall()):
                ship.posX+=3
        elif char==80: #down
            ship.posY+=2
            if(collideWall()):
                ship.posY-=2
        elif char==77: #right
            ship.posX+=3
            if(collideWall()):
                ship.posX-=3
        elif char==72: #up
            ship.posY-=2
            if(collideWall()):
                ship.posY+=2
        elif char==32: #shoot
            mObjects.append(Bullet(ship.posX+1, ship.posY))

    #spawn astroids
    astroidSpawner.spawnAstroid(mObjects)

    #Check collision
    collision()

    #move mObjects
    for mObject in mObjects:
        if(mObject.move(width, height)):
            mObjects.remove(mObject)

    #"Clear" the screen
    string = ""
    #for derp in range(500):
    #    print ""

    #Print info
    string += lost + "\n"
    string += "exit with q\n"

    #Fill canvas
    fillCanvas()

    #Type canvas
    string += typeCanvas()
    sys.stdout.write(string)


    time.sleep(0.1)

            