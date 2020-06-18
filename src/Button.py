import pygame
pygame.font.init()
class Button:

    def __init__(self,x,y,text):
        self.color=(120,120,120)
        self.x=x
        self.y=y
        self.width=200
        self.height=50
        self.text=text

    def draw(self,win,detect=0):

        if detect == 1:
            pygame.draw.rect(win,self.color,(self.x-self.width/2,self.y-self.height/2,self.width,self.height))
            pygame.draw.rect(win,(0,0,0),(self.x-self.width/2,self.y-self.height/2,self.width,self.height),2)
        else:
            pygame.draw.rect(win,self.color,(self.x-self.width/2,self.y-self.height/2,self.width,self.height))
            pygame.draw.rect(win,(0,0,0),(self.x-self.width/2,self.y-self.height/2,self.width,self.height),2)

        fnt = pygame.font.SysFont("comicsans", 30)
        text = fnt.render(self.text, 1, (0,0,0))
        textpos = text.get_rect()
        textpos.centerx = win.get_rect().centerx
        win.blit(text, (textpos[0],self.y-10))


    def check_pos(self,pos):
        if self.x-self.width/2<pos[0]<self.x+self.width:
            if self.y-self.height/2<pos[1]<self.y+self.height:
                return True
        return False

    def change_color(self,color):
        self.color=color
