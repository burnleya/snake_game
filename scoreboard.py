from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")
POS_X = 0
POS_Y = 280


def read_file():
    with open("score.txt", mode="r") as f:
        score = f.read()
        return score


def update_file(score):
    with open("score.txt", mode="w") as f:
        f.write(score)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(POS_X, POS_Y)
        self.score = 0
        self.high_score = int(read_file())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            update_file(str(self.high_score))
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


















