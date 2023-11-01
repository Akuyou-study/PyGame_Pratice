import pygame
import time

from Games.BallGame.BallClass import BallClass
from Utilities import Log

# Set up the global variable of Ball Game
logRecord = Log.LogClass()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
border = [
    screen.get_height(), # Top border   - 0
    0,                   # Down border  - 1
    screen.get_width(),  # Right border - 2
    0                    # Left border  - 3
]

def running(obj_list: [BallClass]):
    running = True
    dt = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        # Object operation
        for obj in obj_list:
            obj.draw(screen)
            obj.move(border, dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


def gameStart():
    pygame.init()

    player_obj = BallClass(border[0] / 2, border[2] / 2, "white", False)
    logRecord.printBallAttr(player_obj)
    obj_list = [player_obj]
    running(obj_list)

    pygame.QUIT()