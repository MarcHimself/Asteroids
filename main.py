import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (updatable_group, drawable_group, asteroid_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (updatable_group, drawable_group, shot_group)
    
    # Instanciate classes on init
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    
    while(True):
        # Check if the player has close the window (x button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("#000000")
        # Update
        updatable_group.update(dt)
        # Collision
        for asteroid in asteroid_group:
            if asteroid.collision(player):
                print("Game Over!")
                pygame.quit()
                sys.exit()
            
            for shot in shot_group:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()                
        # Draw
        for thing in drawable_group:
            thing.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        player.shot_cooldown -= dt
        
if __name__ == "__main__":
    main()
