import pygame

pygame.init()

screen=pygame.display.set_mode((600,600))

class Circle():
    def __init__(self,size,color,x,y,width):
        self.size=size
        self.c=color
        self.x=x
        self.y=y
        self.width=width
        self.screen=screen
    def draw(self):
        pygame.draw.circle(self.screen,self.c,(self.x,self.y),self.size,self.width)
    def grow(self):
        self.size+=10
        pygame.draw.circle(self.screen,self.c,(self.x,self.y),self.size,self.width)

circle1=Circle(50,(0,255,0),300,300,0)

playing=True

while playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            circle1.draw()
        elif event.type==pygame.MOUSEBUTTONUP:
            circle1.grow()
    pygame.display.update()
    
