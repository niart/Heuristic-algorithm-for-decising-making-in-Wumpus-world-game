# link.py
#
# The code that defines the behaviour of Link. You should be able to
# do all you need in here, using access methods from world.py, and
# using makeMove() to generate the next move.
#
# Written by: Simon Parsons
# Modified by: Ni Wang 
# Last Modified: 25/01/2021

import world
import random
import utils
from utils import Directions

class Link():

    def __init__(self, dungeon):

        # Make a copy of the world an attribute, so that Link can
        # query the state of the world
        self.gameWorld = dungeon
        self.flag=0
        # What moves are possible.
        self.moves = [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]
        
    def check(self,x,y):

        pit=self.gameWorld.getPitsLocation()
        w=self.gameWorld.getWumpusLocation()
        gold=self.gameWorld.getGoldLocation()
        if self.flag and x==gold[0].x and y==gold[0].y:return 0
        for i in w:
            if(abs(x-i.x)+abs(y-i.y)<=1):return 2
        for i in pit:
            if(x==i.x and y==i.y):return 1
        return 0
    def dis(self,a,b):
        return abs(a.x-b.x)+abs(a.y-b.y)
    def makeMove(self):
        # This is the function you need to define

        # For now we have a placeholder, which always moves Link
        # directly towards the gold.
        # 
        # Get the location of the gold.
        pit=self.gameWorld.getPitsLocation()
        gold=self.gameWorld.getGoldLocation()
        my=self.gameWorld.getLinkLocation()
        x=self.gameWorld.getWumpusLocation()
        self.flag+=self.gameWorld.justLooted()
        # if()
        # exit(0)
        allGold = self.gameWorld.getGoldLocation()
        nextGold=allGold[0]
        for i in allGold:
            if self.dis(my,i)<self.dis(my,nextGold):
                nextGold = i
        cause=0


        # If not at the same x coordinate, reduce the difference
        if nextGold.x > my.x and self.check(my.x+1,my.y)==0:
            return Directions.EAST and print（my.x, my.y）
        else:cause=max(cause,self.check(my.x+1,my.y))
        if nextGold.x < my.x and self.check(my.x-1,my.y)==0:
            return Directions.WEST and print（my.x, my.y）
        else:cause=max(cause,self.check(my.x-1,my.y))
        # If not at the same y coordinate, reduce the difference
        if nextGold.y > my.y and self.check(my.x,my.y+1)==0:
            return Directions.NORTH and print（my.x, my.y）
        else:cause=max(cause,self.check(my.x,my.y+1))
        if nextGold.y < my.y and self.check(my.x,my.y-1)==0:
            return Directions.SOUTH and print（my.x, my.y）
        else:cause=max(cause,self.check(my.x,my.y-1))
        if cause==2 and self.check(my.x,my.y)==0:return 0
        if my.x<9 and self.check(my.x+1,my.y)==0:return Directions.EAST and print（my.x, my.y）
        if my.x>0 and self.check(my.x-1,my.y)==0:return Directions.WEST and print（my.x, my.y）
        if my.y<9 and self.check(my.x,my.y+1)==0:return Directions.NORTH and print（my.x, my.y）
        if my.y>0 and self.check(my.x,my.y-1)==0:return Directions.SOUTH and print（my.x, my.y）
