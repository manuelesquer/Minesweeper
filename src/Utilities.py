import pygame
from random import randint, shuffle
import math
import tkinter as tk
from tkinter import messagebox

from Grid import Grid
from Cube import Cube

from Initial_win import initial_win

emoji=[pygame.image.load('../images/normal28_face.png'),
       pygame.image.load('../images/PEQ28_feliz.png'),
       pygame.image.load('../images/winemi28.png'),
       pygame.image.load('../images/emoji28_muerto.png')]

def winning(board,win,width):
    draw_emoji(win,2,width)
    board.draw_bombs(win)
    pygame.display.update()
    message_box('Congratulation','You win!')
    board.reset()

def losing(board,win,width):
    draw_emoji(win,3,width)
    board.draw_bombs(win)
    pygame.display.update()
    message_box('BOOM','You lose. Try it again!')
    board.reset()

def board_init(board,win,width,correct):
    bomb_pos=board.set_bombs()
    board.neighbors(bomb_pos)
    draw_window(win,board,width,correct)
    pygame.display.update()

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost",True)
    root.withdraw()
    messagebox.showinfo(subject,content)
    try:
        root.destroy()
    except:
        pass

def draw_window(win,board,width,correct):
    win.fill((200,200,200))
    board.draw_grid(win)

    # Draw the cube of reset
    pygame.draw.rect(win,(100,100,100),(width/2-15,15,30,30))
    # Draw the emojis of the reset button
    if correct:
        draw_emoji(win,1,width)
    else:
        draw_emoji(win,0,width)
    #Draw the frame of the reset button
    pygame.draw.rect(win,(0,0,0),(width/2-15,15,30,30),2)

def draw_emoji(win,type,width):
    win.blit(emoji[type],(width/2+2-15,15+2))
    pygame.draw.rect(win,(0,0,0),(width/2-15,15,30,30),2)

def configure_level():
    level=initial_win()
    if level==1:
        rows=8
        cols=8
    elif level==2:
        rows=16
        cols=16
    elif level ==3:
        rows=20
        cols=20

    width=cols*25+30
    heigth=rows*25+75
    return rows,cols,width,heigth
