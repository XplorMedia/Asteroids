import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius)
    
    def update(self, dt):
        self.position += (self.velocity * dt)