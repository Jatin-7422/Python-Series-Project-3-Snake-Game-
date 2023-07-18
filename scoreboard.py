from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270 )
        self.write(f"SCORE : {self.score}",align="center",font=("Arial",10,"normal "))
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt" ,mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.clear()
        self.write(f"SCORE : {self.score} HIGH SCORE : {self.high_score}", align="center", font=("Arial", 10, "normal "))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE : {self.score} HIGH SCORE : {self.high_score}",align="center",font=("Arial",10,"normal "))

