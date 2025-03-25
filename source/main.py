import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
def main():
    pygame.init()
    # Create a clock object that holds the time
    clock = pygame.time.Clock()
    # delta time variable
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for element in drawable:
            element.draw(screen)
        for element in updateable:
            element.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game Over")
                sys.exit()
            for shot in shots:
                if shot.check_collisions(asteroid):
                    asteroid.split()
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()