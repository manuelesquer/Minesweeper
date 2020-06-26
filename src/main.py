import pygame

from Grid import Grid, Cube
from Initial_win import initial_win
from Utilities import *
from Cube import Cube
pygame.font.init()

def initiation():
        rows,cols,width,height=configure_level()
        win = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Minesweeper")
        board=Grid(rows,cols)
        button=Button(20,20,"Back",60,30,(100,100,100),(120,120,120))
        board_init(board,win,width,button)
        clock = pygame.time.Clock()
        return win,board,height,width,button,clock

def main():
    correct=False       # Variable of control for clicking a correct square
    run=True            # Running control variable
    check_bomb=False    # Checking if the player press a square bomb
    check_win=False     # Checking if the player wins

    # Pop up the selection levels of the game
    win,board,height,width,button,clock = initiation()
    while run:
        pygame.time.delay(50)
        clock.tick(10) #This clock avoid the game goes more than 10fps. It goes 10 blocks/s shorted by the previous delay
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                if button.check_pos(pos):
                    button.change_color(True)
                else:
                    button.change_color(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if width//2-15<=pos[0]<=width//2+15 and 15<=pos[1]<=45:
                        board.reset()
                        draw_window(win,board,width,correct,button)
                    elif 15 < pos[0] < width-15 and 60 < pos[1] < height-15:
                        check_bomb=board.click_grid(pos,event.button)
                        check_win=board.win()
                        correct=True
                    if button.check_pos(pos):
                        win,board,height,width,button,clock = initiation()
                elif event.button == 3:
                    check_bomb=board.click_grid(pos,event.button)

        draw_window(win,board,width,correct,button)
        pygame.display.update()

        if check_bomb:
            losing(board,win,width)
            check_bomb=False
            check_win=False
        if check_win:
            winning(board,win,width)
            check_win=False


        correct=False

main()
pygame.quit()
