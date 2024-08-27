from turtle import Turtle, Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        # b_width = 40
        # b_height = 20
        # self.screen.register_shape(
        #     "car",
        #    (
        #         (b_height / 2, 0),
        #         (-b_height / 2, 0),
        #         (-b_height / 2, b_width),
        #         (b_height / 2, b_width)
        #    )
        # )
        self.move_increment = MOVE_INCREMENT
        self.cars = []


        
    def reset_finished_cars(self):
        pass
    
    def add_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(280, random.randint(-240,240))
        new_car.setheading(180)
        new_car.color(COLORS[random.randint(0,len(COLORS)-1)])
        
        self.cars.append(new_car)

        
    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(300, random.randint(-240,240))
            else:
                car.forward(MOVE_INCREMENT)
                
    def is_car_at(self, position):
        for car in self.cars:
            if abs(car.xcor() - position[0]) < 5 and abs(car.ycor() - position[1]) < 30:
                print(f"near Miss: xdistance: {abs(car.xcor() - position[0]) } ydistance: {abs(car.ycor() - position[1])}")

            if abs(car.xcor() - position[0]) < 5 and abs(car.ycor() - position[1]) < 26:
                print(f"xdistance: {abs(car.xcor() - position[0]) } ydistance: {abs(car.ycor() - position[1])}")
                return True
            


        return False
