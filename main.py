import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import * 
from circleshape import *
import sys


def main():
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (updatable, drawable)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS, shots_group)
  

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("#000000") 
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids: 
            if player.collide(asteroid): 
                sys.exit("Game Over")
        for asteroid in asteroids:
            for shot in shots_group:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()  
                
        pygame.display.flip() 
        result = clock.tick(60)
        dt = result / 1000 
        


        

if __name__ == "__main__":
    main()

   


