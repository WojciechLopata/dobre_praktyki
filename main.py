import pygame
import tic_tac_toe
import button
import time
import connect_4
from operator import methodcaller


pygame.init
pygame.font.init()
screen=pygame.display.set_mode((754,958))
pygame.display.set_caption("GAME COLLECTION")
icon=pygame.image.load("logo.png")
pygame.display.set_icon(icon)
game1=button.Button([100,100],"logo.png",6.4,False)
game2=button.Button([300,300],"tetris.png",1,False)
game3=button.Button([500,500],"connect-four.png",1,False)
actions=[[game1,tic_tac_toe.tic],[game2,"tetris"],[game3,connect_4.connect_4]]
state=True
screen.fill((130,100,0))
while(state):
    screen.fill((130,100,0))
    for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    state=False
    for i in range(0,len(actions)):
        object=actions[i][0]
        if(object.draw(screen,None)):
            print("klik")
            time.sleep(0.5)
            if(not actions[i][1]()):
                state=False

           
        
   
    pygame.display.update()




#tic_tac_toe.tic()