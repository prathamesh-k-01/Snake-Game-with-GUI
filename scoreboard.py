from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")
with open("data.txt", mode="r") as file:
    content = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = content
        self.penup()
        self.color("white", "black")
        self.goto(0, 265)
        self.hideturtle()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)
    #     self.goto(0, -30)
    #     self.write(f"Your Score: {self.score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(f"{self.high_score}")

        self.score = 0
        self.update_score()
