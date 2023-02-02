from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 10
SPAWN_POSITION = [(0, 0), (-10, 0), (-20, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in SPAWN_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def raise_segment(self):
        self.add_segment(self.segments[-1].position())
                
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].setposition(self.segments[seg_num - 1].position())

        self.segments[0].forward(MOVE_DISTANCE)