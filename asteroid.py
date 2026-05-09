from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rnd = random.uniform(20, 50)

        first_split_asteroid_vec = self.velocity.rotate(rnd)
        second_split_asteroid_vec = self.velocity.rotate(-rnd)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_split_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius)
        first_split_asteroid.velocity = first_split_asteroid_vec * 1.2

        second_split_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius)
        second_split_asteroid.velocity = second_split_asteroid_vec * 1.2
