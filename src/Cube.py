import pygame

bomb=pygame.image.load('../images/greybomb23.png')
flag=pygame.image.load('../images/flag.png')

class Cube:

    def __init__(self,value,row,col,width,height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.mineselected = False

    def draw (self,win):
        x = self.col * self.width+17
        y = self.row * self.height+62
        if self.selected == True:
            if self.value==-1:
                pygame.draw.rect(win,(255,0,0),(x,y,self.width-2,self.height-2))
                win.blit(bomb,(x,y))
            elif self.value==0:
                pygame.draw.rect(win,(130,130,130),(x,y,self.width-2,self.height-2))
            elif self.value==-2:
                # Draw the flag to indicate the mine
                pygame.draw.rect(win,(0,255,0),(x,y,self.width-4,self.height-4))
            else:
                pygame.font.init()
                fnt = pygame.font.SysFont("comicsans",40)
                pygame.draw.rect(win,(130,130,130),(x,y,self.width-2,self.height-2))
                text = fnt.render(str(self.value), 1, (0, 0, 0))
                win.blit(text, (int(x), y))
            self.mineselected = False
        elif self.mineselected == True:
            # Draw the flag to indicate the mine
            win.blit(flag,(x,y))

    def increment(self):
        self.value+=1

    def update_value(self,value):
        self.value = value

    def activate_selected(self):
        self.selected = True

    def mine_preselected(self):
        self.mineselected = True

    def reset_variables(self):
        self.selected=False
        self.value = 0
        self.mineselected = False
