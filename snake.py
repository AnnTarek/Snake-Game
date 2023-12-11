from turtle import Turtle
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        x = 0
        for snake in range(0, 3):
            square = self.new_sege()
            square.setposition(x=x, y=0)
            self.snakes.append(square)
            x -= 20

    def new_sege(self):
        square = Turtle("square")
        square.color("white")
        square.penup()
        return square

    def update(self):
        square = self.new_sege()
        self.snakes.append(square)

    def move(self):
        for seg in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg - 1].xcor()
            new_y = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DIST)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def hit_a_wall(self):
        if self.snakes[0].xcor() > 280 or self.snakes[0].ycor() > 290 \
                or self.snakes[0].xcor() < -280 or self.snakes[0].ycor() < -290:
            return True
        return False

    def hit_tail(self):
        for segment in self.snakes[1:]:
            if segment\
                    .distance(self.snakes[0]) < 10:
                return True
        return False

    def snake_reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
