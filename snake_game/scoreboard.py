from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)

    def update_score(self):
        self.clear()
        self.write(arg=f"Score:{self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode = "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    def add_score(self):
        self.score += 1
        self.update_score()

    #def game_over(self):
     #   self.goto(0,0)
      #  self.color("white")
       # self.write(arg="Game over.",align="center",font=FONT)