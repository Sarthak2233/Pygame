import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    #A class to manage the bullet fired from the ship
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color
        #Making the bullet rectangle
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop
        #Store the bullets float value
        self.y=float(self.rect.y)
        
    
    def update(self):
        ##Move the bullet up the screen
            #update the decimal position of the bullet
        self.y-=self.settings.bullet_speed
        #Update the Rect position
        self.rect.y=self.y
        
    def draw_bullets(self):
        #Drawing the bullets in the screen
        pygame.draw.rect(self.screen,self.color,self.rect)