from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame

class Shot(CircleShape) :
    def __init__(self):
        super().__init__(0,0,SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)