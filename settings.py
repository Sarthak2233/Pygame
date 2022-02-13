background=[1,2,2,2,1,2]
screen=[0]*6
for i in range(0,6):
    screen[i]=background[i]
player=5
while player>=0:
    screen[player]=8
    print(screen)
    screen[player]=background[player]
    player-=1
    
    
    
    
class Settings:
    #A class to store all the settings for alien invasion
    def __init__(self):
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)
        self.ship_speed=1.5
        
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_speed=1
        self.bullet_allowed=3