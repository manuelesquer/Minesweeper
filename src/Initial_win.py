import pygame

from Button import Button
pygame.font.init()

def draw_win(win,easy,inter,diff):
    win.fill((150,150,150))
    easy.draw(win)
    inter.draw(win)
    diff.draw(win)

    fnt = pygame.font.SysFont("comicsans", 45)
    text = fnt.render("MINESWEEPER", 1, (0,0,0))
    textpos = text.get_rect()
    textpos.centerx = win.get_rect().centerx
    win.blit(text, (textpos[0],40))

    fnt = pygame.font.SysFont("comicsans", 30)
    text = fnt.render("Select level", 1, (0,0,0))
    textpos = text.get_rect()
    textpos.centerx = win.get_rect().centerx
    win.blit(text, (textpos[0],100))


def initial_win():

    easybutton=Button(150,175,"Easy")
    interbutton=Button(150,300,"Intermediate")
    diffbutton=Button(150,425,"Difficult")

    selcolor=(100,100,100)
    unselcolor=(120,120,120)
    win = pygame.display.set_mode((300,500))
    run=True
    clock = pygame.time.Clock()
    while run:
        pygame.time.delay(50)
        clock.tick(20) #This clock avoid the game goes more than 10fps. It goes 10 blocks/s shorted by the previous delay
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                if easybutton.check_pos(pos):
                    easybutton.change_color(selcolor)
                else:
                    easybutton.change_color(unselcolor)
                if interbutton.check_pos(pos):
                    interbutton.change_color(selcolor)
                else:
                    interbutton.change_color(unselcolor)
                if diffbutton.check_pos(pos):
                    diffbutton.change_color(selcolor)
                else:
                    diffbutton.change_color(unselcolor)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easybutton.check_pos(pos):
                    print("Easy")
                    pygame.quit()
                    return 1
                elif interbutton.check_pos(pos):
                    print("Intermediate")
                    pygame.quit()
                    return 2
                elif diffbutton.check_pos(pos):
                    print("Difficult")
                    pygame.quit()
                    return 3
        draw_win(win,easybutton,interbutton,diffbutton)
        pygame.display.update()
