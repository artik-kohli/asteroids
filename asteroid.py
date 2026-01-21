import random
from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius=radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (dt * self.velocity)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(angle)
        velocity_2 = self.velocity.rotate(-angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

        new_asteroid_1.velocity = velocity_1 * 1.2
        new_asteroid_2.velocity = velocity_2

        
