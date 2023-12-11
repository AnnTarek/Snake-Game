from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.pen(shown=False)
        self.penup()
        self.goto(x=0, y=260)
        self.write_score()

    def write_in_file(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def get_high_score(self):
        with open("high_score.txt") as file:
            return int(file.read())
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align= "center", font=("Bold", 12, "normal"))

    def refresh_score(self):
        self.score += 1
        self.write_score()

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()
        self.write_in_file()

