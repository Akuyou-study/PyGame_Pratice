from Games.BallGame.BallClass import BallClass

class LogClass:
    tag_list = ["[Debug]", "[Info]", "[Warning]", "[ERROR]"]

    def log(self, context: str, level: int):
        if level == 1: tag = LogClass.tag_list[1]
        elif level == 2: tag = LogClass.tag_list[2]
        elif level == 3: tag = LogClass.tag_list[3]
        else: tag = LogClass.tag_list[0]

        print(tag + ": " + context)

    def printBallAttr(self, ball: BallClass):
        self.log("The survived is: " + str(ball.survived), 0)
        self.log("The x axis is: " + str(ball.pos_x), 0)
        self.log("The y axis is: " + str(ball.pos_y), 0)
        self.log("The position is: " + str(ball.position), 0)
        self.log("The color is: " + ball.color, 0)
        self.log("The radius is: " + str(ball.radius), 0)