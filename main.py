from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event
import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)
        for thing in asteroids:
            if player.collides_with(thing):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for thing2 in shots:
                if thing.collides_with(thing2):
                    log_event("asteroid_shot")
                    thing.split()
                    thing2.kill()
                    continue
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        time = clock.tick(60)
        dt = time/1000

if __name__ == "__main__":
    main()
