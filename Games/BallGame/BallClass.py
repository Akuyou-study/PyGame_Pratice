import pygame
import random

class BallClass:
    def __init__(self, pos_x: int, pos_y: int, color: str, isRandomRadius: bool):
        self.survived = True
        self.position = pygame.Vector2(pos_x, pos_y)
        self.pos_x = self.position.x
        self.pos_y = self.position.y
        self.color = color

        if (isRandomRadius):
            self.radius = random.randint(5, 35)
        else:
            self.radius = 10
        self.halfRadius = self.radius / 2

    # Get the current border position value
    def borderChange(self):
        self.topBorder = self.pos_y + self.halfRadius
        self.downBorder = self.pos_y - self.halfRadius
        self.leftBorder = self.pos_x - self.halfRadius
        self.rightBorder = self.pos_x + self.halfRadius

    def draw(self, screen: pygame.surface.Surface):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
        self.borderChange()

    def move(self, border: [int], dt: float):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if (self.downBorder > border[1] + self.halfRadius):
                self.position.y -= 300 * dt
                self.borderChange()
            elif border[1] <= self.topBorder <= border[1] + self.halfRadius:
                self.position.y = border[1] + self.halfRadius
                self.borderChange()