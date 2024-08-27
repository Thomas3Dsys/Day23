from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.width = 20
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
        
    def is_finished(self):
        return self.ycor() >= FINISH_LINE_Y
    
    def next_level(self):
        self.goto(STARTING_POSITION)
    

        

