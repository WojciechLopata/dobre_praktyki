import pygame
class Button:
    def __init__(self,pos,file_name,scale,one_click=True):
        self.image=pygame.image.load(file_name)
        print(pos)
        (x,y)=pos
        width=self.image.get_width()
        height=self.image.get_height()
        self.image=pygame.transform.scale(self.image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
        self.one_click=one_click
    def draw(self,surface,file_name=None):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and  self.clicked==False:
                if self.one_click : self.clicked=True
                
                if (file_name):
                    self.image=pygame.image.load(f"{file_name}.png")
                action=True
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action