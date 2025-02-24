from circleshape import * 
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
       pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, width = 2)
    

        

    def update(self, dt):
         
          self.position += self.velocity * dt

class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"#96FF96", self.position, SHOT_RADIUS, width = 1)
        
    
    def update(self, dt):
        
        self.position += self.velocity * dt
        