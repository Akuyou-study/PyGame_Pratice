import pygame
import random
import time

from Utilities import Log

pygame.init()
logRecord = Log.LogClass()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0
topLimit = screen.get_height()
downLimit = 0
rightLimit = screen.get_width()
leftLimit = 0

class Ball:
    survived = True

    def __init__(self, pos_x: int, pos_y: int, color: str, isRandomRadius: bool):
        self.position = pygame.Vector2(pos_x, pos_y)
        self.color = color
        if isRandomRadius:
            self.radius = random.randint(5, 35)
        else:
            self.radius = 10
        self.topLimit =  self.position.y + self.radius / 2
        self.downLimit =  self.position.y - self.radius / 2
        self.leftLimit =  self.position.x - self.radius / 2
        self.rightLimit =  self.position.x + self.radius / 2

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def limitChange(self):
        self.topLimit = self.position.y + self.radius / 2
        self.downLimit = self.position.y - self.radius / 2
        self.leftLimit = self.position.x - self.radius / 2
        self.rightLimit = self.position.x + self.radius / 2

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if (self.downLimit > downLimit + self.radius / 2):
                self.position.y -= 300 * dt
                self.limitChange()
            elif downLimit <= self.topLimit <= downLimit + self.radius / 2:
                self.position.y = downLimit + self.radius / 2
                self.limitChange()
            logRecord.log("Press w key", 0)
            logRecord.printPosition(self.position)

        if keys[pygame.K_s]:
            if (self.topLimit < topLimit - self.radius / 2):
                self.position.y += 300 * dt
                self.limitChange()
            elif (topLimit - self.radius / 2 <= self.topLimit <= topLimit):
                self.position.y = topLimit - self.radius / 2
                self.limitChange()
            logRecord.log("Press s key", 0)
            logRecord.printPosition(self.position)

        if keys[pygame.K_a]:
            if (self.leftLimit > leftLimit + self.radius / 2):
                self.position.x -= 300 * dt
                self.limitChange()
            elif (leftLimit <= self.leftLimit <= leftLimit + self.radius / 2):
                self.position.x = leftLimit + self.radius / 2
                self.limitChange()
            logRecord.log("Press a key", 0)
            logRecord.printPosition(self.position)

        if keys[pygame.K_d]:
            if (self.rightLimit < rightLimit - self.radius / 2):
                self.position.x += 300 * dt
                self.limitChange()
            elif (rightLimit - self.radius / 2 <= self.rightLimit <= rightLimit):
                self.position.x = rightLimit - self.radius / 2
                self.limitChange()
            # self.position.x += 300 * dt
            logRecord.log("Press d key", 0)
            logRecord.printPosition(self.position)
            
def gamingRunning():
    

    player_obj = Ball(screen.get_width() / 2, screen.get_height() / 2, "white", False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # logRecord.log(str(keys), 3)
                running = False

        screen.fill("black")

        player_obj.draw()
        player_obj.move()

        pygame.display.flip()

        # clock.tick(60)

        dt = clock.tick(60) / 1000
    
    pygame.QUIT()
