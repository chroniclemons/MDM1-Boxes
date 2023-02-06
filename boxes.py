import pandas as pd
import numpy as np
import turtle


# Variables
cl = 100
box_dimx = 4
box_dimy = 10
length = box_dimy*cl
width = box_dimx*cl


def RollData(box_dimns, len_in_squares):
    return pd.DataFrame(np.zeros((box_dimns, len_in_squares)))

# Class to better viaually represent the roll
class draw_it():
    def __init__(self, roll_width=400, Section_length=1400):
        self.len = Section_length
        self.wid = roll_width

    def draw_roll(self, length, wid):
        brad = turtle.Turtle()
        brad.speed(10)
        brad.penup()
        brad.setposition(-(length)/2, wid/2)
        brad.pendown()
        brad.forward(length)
        brad.right(90)
        brad.forward(wid)
        brad.right(90)
        brad.forward(length)
        brad.right(90)
        brad.forward(wid)
        brad.right(90)
        brad.penup()
        brad.hideturtle()

    def draw_grid(self, length, width, box_dimnx, box_dimny, cl):
        bruh = turtle.Turtle()
        bruh.speed(10)
        bruh.penup()
        bruh.setposition(-(length)/2, width/2)
        bruh.pendown()
        for i in range(box_dimnx - 1):
            bruh.right(90)
            bruh.forward(cl)
            bruh.pendown()
            bruh.left(90)
            bruh.forward(length)
            bruh.penup()
            bruh.backward(length)
        bruh.setposition(-(length)/2, width/2)
        for i in range(box_dimny - 1):
            bruh.forward(cl)
            bruh.right(90)
            bruh.pendown()
            bruh.forward(width)
            bruh.penup()
            bruh.backward(width)
            bruh.left(90)
        bruh.hideturtle()
        

roll = RollData(box_dimx, box_dimy)

window = turtle.Screen()
window.screensize(1080, 1080)
window.bgcolor("white")
Drawn = draw_it()
Drawn.draw_roll(length, width)
Drawn.draw_grid(length, width, box_dimx, box_dimy, cl)
window.exitonclick()
