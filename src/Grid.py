import pygame
from random import randint, shuffle
import math
import tkinter as tk
from tkinter import messagebox
from Cube import Cube

class Grid:

    def __init__(self,rows,cols):

        self.table = []
        for i in range(rows):
            self.table.append([0]*cols)

        self.rows = rows
        self.cols = cols
        self.width = cols*25
        self.height = rows*25
        self.num_bombs=int((self.rows*self.cols)/6.4)
        self.bomb_pos=[]
        self.cubes=[[Cube(self.table[i][j],i,j,self.width/self.cols,self.height/self.rows) for j in range(self.cols)] for i in range(self.rows)]

    # This function is in charge of drawing everything in the playing window
    def draw_grid(self,win):
        marge=15
        gap= [self.width/self.cols,self.height/self.rows]
        #draw the lines of the grid
        for i in range(self.cols+1):
            pygame.draw.line(win,(0,0,0),(int(marge+i*gap[0]),60),(int(marge+i*gap[0]),60+self.height),2)
        for j in range(self.rows+1):
            pygame.draw.line(win,(0,0,0),(marge,int(60+j*gap[1])),(marge+self.width,int(60+j*gap[1])),2)
        # Draw the cubes of the grid
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)


    # Create the random position of the bombs in the grid
    def set_bombs(self):
        self.bomb_pos=[]
        list_bombs=list(range(self.rows*self.cols))
        shuffle(list_bombs)
        for i in range (self.num_bombs):
            self.bomb_pos.append([list_bombs[i] % self.rows,list_bombs[i]//self.cols])
            self.table[self.bomb_pos[i][0]][self.bomb_pos[i][1]]=-1
            self.cubes[self.bomb_pos[i][0]][self.bomb_pos[i][1]].update_value(-1)
        return self.bomb_pos

    # Generate the values of the quantity of bombs that is surrounding in each square
    def neighbors(self,bomb_pos):
        for pos in bomb_pos:
            if pos[0]>0 and pos[1]>0 and self.table[pos[0]-1][pos[1]-1]!=-1:
                self.table[pos[0]-1][pos[1]-1]+=1
                self.cubes[pos[0]-1][pos[1]-1].increment()
            if pos[0]>0 and self.table[pos[0]-1][pos[1]]!=-1:
                self.table[pos[0]-1][pos[1]]+=1
                self.cubes[pos[0]-1][pos[1]].increment()
            if pos[0]>0 and pos[1]<self.cols-1 and self.table[pos[0]-1][pos[1]+1]!=-1:
                self.table[pos[0]-1][pos[1]+1]+=1
                self.cubes[pos[0]-1][pos[1]+1].increment()
            if pos[1]>0 and self.table[pos[0]][pos[1]-1]!=-1:
                self.table[pos[0]][pos[1]-1]+=1
                self.cubes[pos[0]][pos[1]-1].increment()
            if pos[1]<self.cols-1 and self.table[pos[0]][pos[1]+1]!=-1:
                self.table[pos[0]][pos[1]+1]+=1
                self.cubes[pos[0]][pos[1]+1].increment()
            if pos[0]<self.rows-1 and pos[1]>0 and self.table[pos[0]+1][pos[1]-1]!=-1:
                self.table[pos[0]+1][pos[1]-1]+=1
                self.cubes[pos[0]+1][pos[1]-1].increment()
            if pos[0]<self.rows-1 and self.table[pos[0]+1][pos[1]]!=-1:
                self.table[pos[0]+1][pos[1]]+=1
                self.cubes[pos[0]+1][pos[1]].increment()
            if pos[0]<self.rows-1 and pos[1]<self.rows-1 and self.table[pos[0]+1][pos[1]+1]!=-1:
                self.table[pos[0]+1][pos[1]+1]+=1
                self.cubes[pos[0]+1][pos[1]+1].increment()

    # Get the position of the mouse click
    def click_grid(self, pos):
        gap_x = self.width // self.rows
        gap_y = self.height // self.cols
        x = (pos[0]-15) // gap_x
        y = (pos[1]-60) // gap_y
        pos_grid = [int(y),int(x)]
        self.cubes[pos_grid[0]][pos_grid[1]].activate_selected()

        if self.table[pos_grid[0]][pos_grid[1]]==0:
            self.expand(pos_grid)
        elif self.table[pos_grid[0]][pos_grid[1]]==-1:
            return True
        return False

    # Expand the squares in case that the value is 0
    def expand(self,pos):
        aux_list=[]
        ls=[-1,0,1]
        for i in ls:
            for j in ls:
                if 0<=pos[0]-i<=self.rows-1 and 0<=pos[1]-j<=self.cols-1:
                    self.cubes[pos[0]-i][pos[1]-j].activate_selected()
                    if self.table[pos[0]-i][pos[1]-j]==0:
                        aux_list.append([pos[0]-i,pos[1]-j])

        for zeros in aux_list:
            for i in ls:
                for j in ls:
                    if 0<=zeros[0]-i<=self.rows-1 and 0<=zeros[1]-j<=self.cols-1:
                        self.cubes[zeros[0]-i][zeros[1]-j].activate_selected()
                        if self.table[zeros[0]-i][zeros[1]-j]==0 and [zeros[0]-i,zeros[1]-j] not in aux_list:
                            aux_list.append([zeros[0]-i,zeros[1]-j])

    # Reset all the values of the grid
    def reset(self):
        for i in range (len(self.table)):
            for j in range(len(self.table[i])):
                self.table[i][j] = 0

        for i in range (len(self.cubes)):
            for j in range (len(self.cubes[i])):
                self.cubes[i][j].reset_variables()
        bomb_pos=self.set_bombs()
        self.neighbors(bomb_pos)

    # Check if the player wins
    def win(self):
        cont_win=0
        for i in range(self.cols):
            for j in range(self.rows):
                if self.cubes[j][i].selected==0:
                    cont_win+=1
        if cont_win==self.num_bombs:
            return True
        return False
    # Draw all the bombs on the grid
    def draw_bombs(self,win):
        for pos in self.bomb_pos:
            self.cubes[pos[0]][pos[1]].activate_selected()
            self.cubes[pos[0]][pos[1]].draw(win)
