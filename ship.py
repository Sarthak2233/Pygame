import pygame

class Ship:
    #a class to manage the ship
    def __init__(self,ai_game):
        #instialize the ship and installl its starting position
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings
        
        self.load_image=pygame.image.load('ship.bmp')
        #load the ship image and ge its rect.
        self.image=pygame.transform.scale(self.load_image,(50,50))
        self.rect=self.image.get_rect()
        
        #Start each new ship at the bottom of the screen
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        
        #moving flag
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        elif self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        elif self.moving_up and self.rect.top>0:
            self.y-=self.settings.ship_speed
        elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.y+=self.settings.ship_speed
        self.rect.x=self.x
        self.rect.y=self.y
        
        
    def blitme(self):
       #draw a ship at its current location
        self.screen.blit(self.image,self.rect)
    