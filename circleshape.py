import pygame

# Base class for game objects
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

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision_detection(self,other):
        self_vector = self.position
        other_vector = other.position
        #print(f"self.position type: {type(self_vector)}, other.position type: {type(other_vector)}")  # Debugging print
        distance = self_vector.distance_to(other_vector)
        self_radius = self.radius
        other_radius = other.radius
        collision_distance = self_radius + other_radius
        if distance > collision_distance:
            return False
        return True