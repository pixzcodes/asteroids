import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # if its a small asteroid do nothing
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # calc the new directions for the asteroids
        random_angle = random.uniform(20, 50)
        vec_one = self.velocity.rotate(random_angle)
        vec_two = self.velocity.rotate(-random_angle)

        # calc new radius of the asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create new asteroids
        new_asteroid_one = Asteroid(
            self.position.x, self.position.y, new_radius)
        new_asteroid_two = Asteroid(
            self.position.x, self.position.y, new_radius)

        # set new velocities
        new_asteroid_one.velocity = vec_one * 1.2
        new_asteroid_two.velocity = vec_two * 1.2
