import pygame
import random as randint
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        #Load an aelin image
        self.load_image=pygame.image.load('alien.bmp')
        self.image=pygame.transform.scale(self.load_image,(50,50))
        self.rect=self.image.get_rect()
        #Start each new alien from the top left of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        #store the aliens exact horizontal position
        self.x=float(self.rect.x)
    