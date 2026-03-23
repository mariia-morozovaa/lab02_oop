from turtle import *
from math import *


class Petal:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.center = (0, 0)
        self.angle = 0

    def set_center(self, x, y):
        self.center = (x, y)

    def set_angle(self, angle):
        self.angle = angle

    def draw(self):
        up()
        goto(self.center[0], self.center[1])
        setheading(self.angle)
        forward(self.size)
        down()
        fillcolor(self.color)
        begin_fill()
        circle(self.size)
        end_fill()
        up()
        backward(self.size)


class Leaf:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.position = (0, 0)
        self.angle = 0

    def set_position(self, x, y):
        self.position = (x, y)

    def set_angle(self, angle):
        self.angle = angle

    def draw(self):
        up()
        goto(self.position[0], self.position[1])
        setheading(self.angle)
        down()
        fillcolor(self.color)
        begin_fill()
        for _ in range(2):
            circle(self.size, 90)
            circle(self.size // 2, 90)
        end_fill()
        up()


class Stem:
    def __init__(self, length, thickness, color):
        self.length = length
        self.thickness = thickness
        self.color = color
        self.start = (0, 0)

    def set_start(self, x, y):
        self.start = (x, y)

    def draw(self):
        up()
        goto(self.start[0], self.start[1])
        setheading(270)
        pendown()
        pensize(self.thickness)
        pencolor(self.color)
        forward(self.length)
        up()
        pensize(1)


class Flower:
    def __init__(self, x, y, petal_count=8, petal_size=40, petal_color="red",
                 stem_length=120, stem_thickness=5, stem_color="green",
                 leaf_size=20, leaf_color="green"):
        self.x = x
        self.y = y
        self.petal_count = petal_count
        self.petal_size = petal_size
        self.petal_color = petal_color
        self.stem_length = stem_length
        self.stem_thickness = stem_thickness
        self.stem_color = stem_color
        self.leaf_size = leaf_size
        self.leaf_color = leaf_color

        self.petals = []
        for i in range(petal_count):
            self.petals.append(Petal(petal_size, petal_color))

        self.stem = Stem(stem_length, stem_thickness, stem_color)
        self.leaf1 = Leaf(leaf_size, leaf_color)
        self.leaf2 = Leaf(leaf_size, leaf_color)

    def draw(self):
        self.stem.set_start(self.x, self.y)
        self.stem.draw()

        leaf1_y = self.y - self.stem_length * 0.7
        self.leaf1.set_position(self.x, leaf1_y)
        self.leaf1.set_angle(30)
        self.leaf1.draw()

        leaf2_y = self.y - self.stem_length * 0.3
        self.leaf2.set_position(self.x, leaf2_y)
        self.leaf2.set_angle(-30)
        self.leaf2.draw()

        up()
        goto(self.x, self.y - self.petal_size // 3)
        fillcolor("yellow")
        begin_fill()
        circle(self.petal_size // 2)
        end_fill()

        angle_step = 360 / self.petal_count
        for i in range(self.petal_count):
            angle = i * angle_step
            petal_x = self.x + cos(radians(angle)) * (self.petal_size * 0.4)
            petal_y = self.y + sin(radians(angle)) * (self.petal_size * 0.8)

            self.petals[i].set_center(petal_x, petal_y)
            self.petals[i].set_angle(angle)
            self.petals[i].draw()

    def set_begin(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
            reset()
            speed(0)
            hideturtle()
            tracer(0)

            flowers = [
                Flower(-80, -100, petal_count=6, petal_size=15, petal_color="red"),
                Flower(0, -120, petal_count=8, petal_size=12, petal_color="pink"),
                Flower(80, -100, petal_count=8, petal_size=14, petal_color="purple")
            ]

            for flower in flowers:
                flower.draw()

            update()
            mainloop()