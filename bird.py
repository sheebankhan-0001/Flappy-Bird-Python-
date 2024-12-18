import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self,scale_factor):
        super(Bird,self).__init__()
        self.img_list=[pg.transform.scale_by(pg.image.load("assets/birdup.png").convert_alpha(),scale_factor),
                        pg.transform.scale_by(pg.image.load("assets/birddown.png").convert_alpha(),scale_factor)]
        self.image_index=0
        self.image=self.img_list[self.image_index]
        self.rect=self.image.get_rect(center=(100,100))
        self.y_velocity=0
        self.gravity=10
        self.flap_speed=250
        self.anim_counter=0
        self.update_on=False
        self.game_over = False  

        self.top_limit = 0
        self.bottom_limit = 400  
    def update(self,dt):
        if self.update_on and not self.game_over:
            self.playAnimation()
            self.applyGravity(dt)

            # Boundary check for game-over condition
            if self.rect.top <= self.top_limit or self.rect.bottom >= self.bottom_limit:
                self.game_over = True  # Trigger game-over when limit is reached
                self.y_velocity = 0  # Stop movement
                self.rect.y = max(self.top_limit, min(self.rect.y, self.bottom_limit))


    
    def applyGravity(self,dt):
        self.y_velocity+=self.gravity*dt
        self.rect.y+=self.y_velocity
    
    def flap(self,dt):
       if not self.game_over:  # Only allow flapping if game is not over
            self.y_velocity = -self.flap_speed * dt
    def playAnimation(self):
        if self.anim_counter==5:
            self.image=self.img_list[self.image_index]
            if self.image_index==0: self.image_index=1
            else: self.image_index=0
            self.anim_counter=0
        
        

    def resetPosition(self):
        self.rect.center=(100,100)
        self.y_velocity=0
        self.anim_counter=0

        self.anim_counter+=1
    
