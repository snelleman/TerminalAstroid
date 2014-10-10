#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class MObject():

    mobString = [[]]
    width = 0
    heigth = 0
    posX = 0
    posY = 0
    speedX = 0
    speedY = 0

    def __init__(self, initMObString, posX, posY, speedX, speedY):
        self.mObString = initMObString
        self.height    = len(initMObString)
        self.width     = len(initMObString[0])
        self.posX = posX
        self.posY = posY
        self.speedX = speedX
        self.speedY = speedY

    def get(self):
        return mobString


    def move(self, width, height):
        self.posX+=self.speedX
        self.posY+=self.speedY
        Y = int(self.posY)
        X = int(self.posX)
        if(-self.height<=Y and Y<height+self.height and -self.width<=X and X<width+self.width):
            return False
        else:
            return True

    def paint(self, canvas, width, height):
        for y in range(self.height):
            for x in range(self.width):
                c = self.mObString[y][x]
                if(c != " "):
                    Y = int(y+self.posY)
                    X = int(x+self.posX)
                    if(0<=Y and Y<height and 0<=X and X<width):
                        canvas[Y][X] = c

    def collideWith(self, mObject):
        y = 0
        while(y < self.height):
            x = 0
            while(x < self.width):
                Y = y + int(self.posY - mObject.posY)
                X = x + int(self.posX - mObject.posX)
                if(0<=Y and Y<mObject.height and 0<=X and X<mObject.width):
                    if(mObject.mObString[Y][X] != " " and self.mObString[y][x] != " "):
                        return (x+self.posX, y+self.posY)
                x+=1
            y+=1
        return None
