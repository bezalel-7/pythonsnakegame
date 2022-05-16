from turtle import Turtle

file = open("score.txt", mode="r")
score = int(file.read())
file1 = open("score.txt", mode="w")


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hightscore = score
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.upadate_scoreboard()
        self.hideturtle()

    def upadate_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} Highest Score:{self.hightscore}", align="center", font=("Arial", 25, "normal"))

    def reset(self):
        if self.score > self.hightscore:
            self.hightscore = self.score
            file1.write(str(self.hightscore))
            self.score = 0
            self.upadate_scoreboard()

    def increase_score(self):
        self.score += 1
        self.upadate_scoreboard()
