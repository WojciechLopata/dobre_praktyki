import random
from turtle import pos
import win_check
import pygame
import button
import time
class sprites():
    def __init__(self,image,pos):
        self.image=pygame.image.load(image)
        (x,y)=pos
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def draw(self,surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))



class game(win_check.state_check):
    def __init__(self):
        self.size=7
        self.placing_aid=[0 for i in range(self.size)]
        self.board=[[" " for i in range(self.size)] for j in range(self.size)]
        self.symbol="X"
        self.win_con=4
        self.state=True
        self.turn=0
        self.pvp=False
        self.result="W trakcie"
    def render(self):
        #for x in self.board:
            #for i in x:
                #print("|",i,"|",end="",sep="")
            print()
    def place(self,col,symbol):
        
        
        row=self.size-self.placing_aid[col]-1
        if(row==0):
            
            setattr(objects[col],"clicked",True)
        self.placing_aid[col]+=1
        if(self.board[row][col]==" "):
            self.board[row][col]=symbol
            pos=(board_left+((width-50)/7)*(col)+35,board_top+height-self.placing_aid[col]*100)
            if(symbol=="X"):ball=sprites("images/red.png",pos)
            else:ball=sprites("images/yellow.png",pos)
            balls.append(ball)
            
            self.render()
        else:return False
        return True        
    def begin(self):
        self.pvp=False
        start=random.randint(0,1)
        if(start==0 or self.pvp):
                
                self.opponnent()           
                
                      
        
    def play(self,position):
        if(self.turn%2==0):
            self.symbol="X"
        else: self.symbol="O"
        self.render()
        
        while not self.place(position,self.symbol):
            print()
            
           
        if(win_check.state_check.check(self.board,self.win_con)):
            self.state=False
            self.render()
            self.end("wygrałeś")
            return True
        self.turn+=1
        if(win_check.state_check.check_draw(self.turn,self.size**2)):
            self.render()
            self.end("Remis")
            return True
        if(self.pvp):self.play()
        else: self.opponnent()
    def opponnent(self):
        if(self.turn%2==0):
            self.symbol="X"
        else: self.symbol="O"
        position=random.randint(1,self.size)-1
        
        while not self.place(position,self.symbol):
            position=random.randint(0,self.size)
        if(win_check.state_check.check(self.board,self.win_con)):
            self.state=False
            self.render()
            self.end("Przegrałeś")
            return True
        self.turn+=1
        if(win_check.state_check.check_draw(self.turn,self.size**2)):
            self.render()
            self.end("Remis")
            return True
    def end(self,result):
            self.result=result
            for object in objects:
                
                setattr(object,"clicked",True)
def status(result):
    text = font.render(f"{result}", True, green, blue)
    textRect = text.get_rect()
    textRect.center=(370,820)
    screen.blit(text, textRect)

        
        
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
x=754
y=958        
screen=pygame.display.set_mode((x,y))
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)       
board=pygame.image.load('images/connect_4.png')        
width=board.get_width()
height=board.get_height()
board_left=(x-width)/2
board_top=(y-height)/2
objects=[button.Button([board_left+((width-50)/7)*(i)+35,50],"images/arrow.png",1,False) for i in range(7)]   
restart=button.Button([500,800],"images/restart.png",1,False)
go_back=button.Button([0,780],"images/go_back.jpg",0.5,False)
red=pygame.image.load("images/red.png")
yellow=pygame.image.load("images/yellow.png")
balls=[]


def connect_4():        
##napraw zmieniające się symboli   
#     
    a=game()
    state=True
    screen.fill((0,0,0))
    while(state):
       
        click=False                         
        #a.begin()
        for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        state=False
                        global play
                        play=False
                        return False
                    for object in objects:
                        if(object.draw(screen,None)):
                            
                            print("KLIK")
                            click=True
                            position=objects.index(object)
                            a.play(position)
        
        screen.blit(board,(board_left,board_top))
        global balls
        for ball in balls:
            ball.draw(screen)
            
            
            
    
        i=0
        status(a.result)
        if(restart.draw(screen,None)):
            balls=[]
            state=False
            for object in objects:
                setattr(object,"clicked",False)
            connect_4()
        if(go_back.draw(screen,None)):
            balls=[]
            for object in objects:
                setattr(object,"clicked",False)
            return True
        pygame.display.update()
                
    
    
