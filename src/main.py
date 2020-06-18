import pygame

from Grid import Grid, Cube
from Initial_win import initial_win
from Utilities import *
from Cube import Cube
pygame.font.init()


def main():
    correct=False       # Variable of control for clicking a correct square
    run=True            # Running control variable
    check_bomb=False    # Checking if the player press a square bomb
    check_win=False     # Checking if the player wins

    # Pop up the selection levels of the game
    rows,cols,width,heigth=configure_level()
    win = pygame.display.set_mode((width,heigth))
    pygame.display.set_caption("Minesweeper")
    board=Grid(rows,cols)
    board_init(board,win,width,correct)

    clock = pygame.time.Clock()
    while run:
        pygame.time.delay(50)
        clock.tick(10) #This clock avoid the game goes more than 10fps. It goes 10 blocks/s shorted by the previous delay
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if width//2-15<=pos[0]<=width//2+15 and 15<=pos[1]<=45:
                    board.reset()
                    draw_window(win,board,width,correct)
                elif 15 < pos[0] < width-15 and 60 < pos[1] < heigth-15:
                    check_bomb=board.click_grid(pos)
                    check_win=board.win()
                    correct=True
        draw_window(win,board,width,correct)
        pygame.display.update()

        if check_win:
            winning(board,win,width)
            check_win=False
        if check_bomb:
            losing(board,win,width)
            check_bomb=False

        correct=False

main()
pygame.quit()
