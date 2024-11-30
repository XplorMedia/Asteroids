import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    playerShip = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2),PLAYER_RADIUS)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    gameField = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        #playerShip.update(dt)
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if playerShip.collision_detection(asteroid):
                print("Game over!")
                sys.exit()
        #playerShip.draw(screen)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        gameClock.tick(60)
        dt = gameClock.tick(60) / 1000

if __name__ == "__main__":
    main()