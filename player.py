import pygame
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOT_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOT_COOLDOWN
from shot import Shot
from circleshape import CircleShape

class Player(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.shot_cooldown = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            left_rotation = dt * (-1)
            self.rotate(left_rotation)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move((dt * (-1)))
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown == 0:
                self.shoot()
                self.shot_cooldown += PLAYER_SHOT_COOLDOWN
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        ship_position = self.position
        self.current_x = ship_position.x
        self.current_y = ship_position.y
        fired_shot = Shot(self.current_x,self.current_y, SHOT_RADIUS)
        base_velocity = pygame.Vector2(0, 1)
        rotated_velocity = base_velocity.rotate(self.rotation)
        fired_shot.velocity = rotated_velocity * PLAYER_SHOT_SPEED
        #print("Pew Pew")