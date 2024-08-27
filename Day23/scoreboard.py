from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()        
        self.color("black")
        self.level = 1
        self.goto(-290,250)
        self.display()

    def kill_player(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", False, "center", FONT )
    
        
    def player_wins(self):
        self.level += 1
        

    def display(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT )
    
