import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    #Use its position, radius, and a width of 2
    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            random_angle = random.uniform(20, 50)
            new_angle = self.velocity.rotate(random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            print(f"{self.position}")
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_angle
            new_asteroid_1.velocity *= 1.2

            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2.velocity = -new_angle
            new_asteroid_2.velocity *= 1.2
            
            #new_asteroid_1.velocity(angle_1) * 1.2
            #new_asteroid_2.velocity(angle_2) * 1.2