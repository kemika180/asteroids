from constants import ASTEROID_COLORS, ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from random import uniform, choice
from logger import log_event
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.color = choice(ASTEROID_COLORS)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
