import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    playerShip = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2),PLAYER_RADIUS)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    gameField = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        #playerShip.update(dt)
        for item in updatable:
            item.update(dt)
        if playerShip.shot_cooldown > 0:
            playerShip.shot_cooldown -= dt
            if playerShip.shot_cooldown < 0:
                playerShip.shot_cooldown = 0
        for asteroid in asteroids:
            if playerShip.collision_detection(asteroid):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            #print(f"asteroid type: {type(asteroid)}, position type: {type(asteroid.position)}")  # Debugging print 
            for shot in shots:
                #print(f"shot type: {type(shot)}, position type: {type(shot.position)}")  # Debugging print 
                if shot.collision_detection(asteroid):
                    asteroid.split()
                    shot.kill()
        #playerShip.draw(screen)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        gameClock.tick(60)
        dt = gameClock.tick(60) / 1000

if __name__ == "__main__":
    main()