
from turtle import Turtle

POSITION= [(0, 0), (-20, 0), (-40, 0)]
MOVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():

    def __init__(self):
        self.segments= []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for all_snakes in POSITION:
            self.add_segment(all_snakes)

    def add_segment(self,all_snakes):
        snake = Turtle("square")
        snake.color("White")
        snake.penup()
        snake.goto(all_snakes)
        self.segments.append(snake)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to a snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len( self.segments) - 1, 0, -1):
            new_x =  self.segments[seg - 1].xcor()
            new_y =  self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)