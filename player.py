import pygame
from constants import *
from circleshape import *
from asteroid import *
class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):
        # we will be using this later
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self, other_object):
            distance = self.position.distance_to(other_object.position)
            radius_sum = self.radius + other_object.radius
            if distance <= radius_sum: 
                return True
            return False

class Player(CircleShape):
    def __init__(self, x, y, radius, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shots_group = shots_group

        self.rotation = 0



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self,dt): 
        self.rotation += (PLAYER_TURN_SPEED * dt)
    

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) 
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot_velocity = pygame.Vector2(0,1)
        shot_velocity = shot_velocity.rotate(self.rotation)
        shot_velocity = shot_velocity * PLAYER_SHOOT_SPEED

        new_shot.velocity = shot_velocity
        self.shots_group.add(new_shot)