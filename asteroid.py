from circleshape import * 
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x_or_pos, y_or_vel=None, radius=None):
        if y_or_vel is None:
            # Called as Asteroid(position_vector, velocity, radius)
            position = x_or_pos
            velocity = y_or_vel
            super().__init__(position.x, position.y, radius)
        else:
            # Called as Asteroid(x, y, radius)
            super().__init__(x_or_pos, y_or_vel, radius)
        
        if isinstance(y_or_vel, pygame.Vector2):
            self.velocity = y_or_vel
        

    def draw(self, screen):
       pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, width = 2)
    

        

    def update(self, dt):
         
          self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
         
        random_angle = random.uniform(20,50)
        veevee1 = pygame.Vector2(self.velocity.rotate(random_angle))
        veevee2 = pygame.Vector2(self.velocity.rotate(-random_angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        veevee1 = veevee1 * 1.2
        veevee2 = veevee2 * 1.2
        asteroid1 = Asteroid(self.position, veevee1, new_radius)
        asteroid2 = Asteroid( self.position, veevee2, new_radius)

        if hasattr(self, 'containers'):
            for container in self.containers:
                container.add(asteroid1)
                container.add(asteroid2)
            
class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"#96FF96", self.position, SHOT_RADIUS, width = 1)
        
    
    def update(self, dt):
        
        self.position += self.velocity * dt
        