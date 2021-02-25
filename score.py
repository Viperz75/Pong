from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        #Left Side Score
        self.clear()
        self.goto(-110, 210)
        self.color("blue")
        self.write(self.l_score, align="center", font=("Arial", 50, "normal"))
        #Right Side Score
        self.goto(110, 210)
        self.color("red")
        self.write(self.r_score, align="center", font=("Arial", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()