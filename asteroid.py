from circleshape import *
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rnd_angle = random.uniform(20, 50)
            first_velocity_angle = self.velocity.rotate(rnd_angle)
            second_velocity_angle = self.velocity.rotate(-rnd_angle)
            small_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, small_asteroid_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, small_asteroid_radius)
            first_asteroid.velocity = first_velocity_angle * 1.2
            second_asteroid.velocity = second_velocity_angle * 1.2


