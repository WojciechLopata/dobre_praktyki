import pygame
import tic_tac_toe

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


def function1():
    print('Function 1')

def function2():
    print('Function 2')

#list of functions
myList = [function1, function2,tic_tac_toe.tic]

#call function using list object
myList[0]()
myList[1]()
myList[2]()