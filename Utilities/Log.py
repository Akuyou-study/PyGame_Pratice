import pygame

class LogClass:
    tag_list = ["[Debug]", "[Info]", "[Warning]", "[ERROR]"]

    def log(self, context: str, level: int):
        if level == 1: tag = LogClass.tag_list[1]
        elif level == 2: tag = LogClass.tag_list[2]
        elif level == 3: tag = LogClass.tag_list[3]
        else: tag = LogClass.tag_list[0]

        print(tag + ": " + context)

    def printPosition(self, pos: pygame.Vector2):
        LogClass.log(self, "The x of position is: " + str(pos.x), 0)
        LogClass.log(self, "The y of position is: " + str(pos.y), 0)