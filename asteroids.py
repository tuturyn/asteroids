import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        center = (self.x, self.y)
        pygame.draw.circle(screen, "white", center, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (super().velocity * dt)
