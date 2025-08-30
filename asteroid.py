from typing import override
from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    @override
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    @override
    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius<= ASTEROID_MIN_RADIUS:
            return
        angle= random.uniform(20,50)
        one= self.velocity.rotate(angle)
        two= self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = one *1.2
        asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid.velocity = two * 1.2
