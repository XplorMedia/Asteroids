import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            asteroid_position = self.position
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            angle_of_diversion = random.uniform(20,50)
            base_vector = self.velocity
            asteroid1_vector = base_vector.rotate(angle_of_diversion)
            asteroid2_vector = base_vector.rotate(-angle_of_diversion)
            self.current_x = asteroid_position.x
            self.current_y = asteroid_position.y
            Asteroid1 = Asteroid(self.current_x,self.current_y, new_asteroid_radius)
            Asteroid2 = Asteroid(self.current_x,self.current_y, new_asteroid_radius)
            Asteroid1.velocity = asteroid1_vector * 1.2
            Asteroid2.velocity = asteroid2_vector * 1.2