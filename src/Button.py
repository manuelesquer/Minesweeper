import pygame

class Button:

    def __init__(self,x,y,text,width,height,selcolour,unselcolour):
        self.colour=unselcolour
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.selcolour=selcolour
        self.unselcolour=unselcolour

    def draw(self,win,detect=0):
        pygame.font.init()
        if detect == 1:
            pygame.draw.rect(win,self.colour,(self.x,self.y,self.width,self.height))
            pygame.draw.rect(win,(0,0,0),(self.x,self.y,self.width,self.height),2)
        else:
            pygame.draw.rect(win,self.colour,(self.x,self.y,self.width,self.height))
            pygame.draw.rect(win,(0,0,0),(self.x,self.y,self.width,self.height),2)

        fnt = pygame.font.SysFont("comicsans", int(self.height-self.height/3))
        text = fnt.render(self.text, 1, (0,0,0))
        text_width,text_height = fnt.size(self.text)
        textpos = text.get_rect()
        textpos.centerx = win.get_rect().centerx
        win.blit(text, (self.x+self.width/2-text_width/2,self.y+self.height/2-text_height/2))


    def check_pos(self,pos):
        if self.x-self.width/2<pos[0]<self.x+self.width:
            if self.y-self.height/2<pos[1]<self.y+self.height:
                return True
        return False

    def change_color(self,trigger):
        if trigger ==True:
            self.colour=self.selcolour
        if trigger == False:
            self.colour=self.unselcolour
