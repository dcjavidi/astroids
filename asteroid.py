import circleshape
import constants
import pygame
from logger import log_state, log_event
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, constants.LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            spawn_1 = Asteroid(self.position[0], self.position[1], new_radius)
            spawn_2 = Asteroid(self.position[0], self.position[1], new_radius)
            spawn_1.velocity = vector_1 * 1.2
            spawn_2.velocity = vector_2 * 1.2

