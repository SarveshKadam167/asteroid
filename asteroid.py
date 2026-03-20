from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self) :
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        log_event("asteroid_split")
        rand = random.uniform(20,50)
        first_asteroid_vel = self.velocity.rotate(rand)
        second_asteroid_vel = self.velocity.rotate(-rand)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(0, 0, new_radius)
        asteroid_one.position = self.position.copy()
        asteroid_one.velocity = first_asteroid_vel * 1.2
        asteroid_two = Asteroid(0, 0, new_radius)
        asteroid_two.position = self.position.copy()
        asteroid_two.velocity = second_asteroid_vel * 1.2