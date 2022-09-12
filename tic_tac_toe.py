
from operator import truediv
import random
from tkinter import Y, Scale
import win_check
import time
import pygame
import button

 

class game(win_check.state_check,button.Button):
    def __init__(self):
        self.size=3
        self.board=[[" " for i in range(self.size)] for j in range(self.size)]
        self.symbol="X"
        self.win_con=3
        self.turn=0
        self.pvp=False
        self.start=random.randint(0,1)
        self.result="W trakcie"
    def place(self,position):
        wiersz=int(position/self.size)
        kolumna=position%self.size
        if(self.board[wiersz][kolumna]==" "):
            self.board[wiersz][kolumna]=self.symbol
            setattr(objects[position],"image",pygame.image.load(f"images/{self.symbol}.png"))
            
            

        else:return False
        return True        
   
    def render(self):
        for x in self.board:
            for i in x:
                print("|",i,"|",end="",sep="")
            print()        
      
                
    def begin(self):
        
        if(self.start==0):
            print("Zaczynasz")
            self.opponnent()   
               
    #metoda obsługująca ruchy gracza bądź graczy gdy self.pvp zwraca wartość True      
    def play(self,position):
        #ta pętla obsługuje czy użytkownik postawił na pustym miejscu znak jeśli nie to musi powtórzyć swój ruch
        self.place(position)
        if(win_check.state_check.check(self.board,self.win_con)):
            self.end("wygrałeś")
            return True
        self.turn+=1
        if(win_check.state_check.check_draw(self.turn,self.size**2)):
            
            self.end("remis")
            return True
        if(self.turn%2==0):
            self.symbol="X"
        else: self.symbol="O"
        self.render() 
        self.opponnent()
       
        
        
    # metoda odpowiadająca za ruch komputera ustawia swoje  znaki na losowych pustych pozycjach
    def opponnent(self):
        
        
        position=random.randint(0,8)
        while not self.place(position):
            position=random.randint(0,8)
        if(win_check.state_check.check(self.board,self.win_con)):
            self.end("przegrałeś")
            return True
        self.turn+=1
        if(win_check.state_check.check_draw(self.turn,self.size**2)):
           
           self.end("remis")
           return True
        self.render()
        if(self.turn%2==0):
            self.symbol="X"
        else: self.symbol="O" 
    def end(self,result):
        self.result=result

        self.render
        for object in objects:
           
            setattr(object,"clicked",True)
        
def status(result):
    text = font.render(f"{result}", True, green, blue)
    textRect = text.get_rect()
    textRect.center=(370,820)
    screen.blit(text, textRect)
screen=pygame.display.set_mode((754,958))
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
#board=pygame.image.load('board.png')
#pygame.mouse.set_visible(1)
pola=["images/Puste.png" for i in range(9)]
pola_pos=[[15,15],[265,15],[515,15],[20,270],[265,265],[515,265],[20,520],[265,515],[515,515]]
objects=[button.Button(pola_pos[i],pola[i],1) for i in range(9)]
restart=button.Button([500,800],"images/restart.png",1,False)
go_back=button.Button([0,780],"images/go_back.jpg",0.5,False)
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)



         

def tic():
       
        state=True
        a=game()
        a.begin()
        board=pygame.image.load('images/board.png')
        boardx=0
        boardy=0
    
        

        

        while(state):               
        
        
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    state=False
                    global play
                    play=False
                    print("exit")
                    return False
            
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos=pygame.mouse.get_pos()
        
            
                global objects
                screen.fill((130,100,0))
                screen.blit(board,(boardx,boardy))
                for object in objects:
                    if(object.draw(screen)):
                        position=objects.index(object)
                        a.play(position)
                           
                    #setattr(object,"image",pygame.image.load("X.png"))
                        object.draw(screen,a.symbol)
                        

                if(restart.draw(screen,None)):
                    state=False
                    global pola
                    pola=["images/Puste.png" for i in range(9)]
                    objects=[button.Button(pola_pos[i],pola[i],1) for i in range(9)]
                    tic()
                status(a.result)
                if(go_back.draw(screen,None)):
                    
                    pola=["images/Puste.png" for i in range(9)]
                    objects=[button.Button(pola_pos[i],pola[i],1) for i in range(9)]
                    return True
                pygame.display.update()

               
    