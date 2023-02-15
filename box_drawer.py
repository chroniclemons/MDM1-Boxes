
import turtle
from PIL import Image


# Class to better viaually represent the roll
class draw_it():
    def __init__(self, dimx, dimy):
        self.len = 50*dimy
        self.wid = 50*dimx
        self.dimx = dimx
        self.dimy = dimy

    def draw_roll(self):
        brad = turtle.Turtle()
        brad.speed(10)
        brad.penup()
        brad.setposition(-(self.len)/2, self.wid/2)
        brad.pendown()
        brad.forward(self.len)
        brad.right(90)
        brad.forward(self.wid)
        brad.right(90)
        brad.forward(self.len)
        brad.right(90)
        brad.forward(self.wid)
        brad.right(90)
        brad.penup()
        brad.setposition(-(self.len)/2, self.wid/2)
        brad.hideturtle()

    def draw_grid(self):
        bruh = turtle.Turtle()
        bruh.speed(10)
        bruh.penup()
        bruh.setposition(-(self.len)/2, self.wid/2)
        bruh.pendown()
        for i in range(self.dimx - 1):
            bruh.right(90)
            bruh.forward(self.wid/self.dimx)
            bruh.pendown()
            bruh.left(90)
            bruh.forward(self.len)
            bruh.penup()
            bruh.backward(self.len)
        bruh.setposition(-(self.len)/2, self.wid/2)
        for i in range(self.dimy - 1):
            bruh.forward(self.len/self.dimy)
            bruh.right(90)
            bruh.pendown()
            bruh.forward(self.wid)
            bruh.penup()
            bruh.backward(self.wid)
            bruh.left(90)
        bruh.setposition(-(self.len)/2 , self.wid/2)
        bruh.hideturtle()
        
    def colour_square(self, X_Pos, Y_Pos, net, colour):
        bruh = turtle.Turtle()
        bruh.speed(10)
        bruh.penup()
        bruh.setposition(-(self.len)/2 + 1, self.wid/2 - 1)
        bruh.right(90)
        bruh.forward(Y_Pos*50)
        bruh.left(90)
        bruh.forward((X_Pos-1)* 50)
        bruh.fillcolor(colour)
        bruh.begin_fill()
        for _ in range(4):
            bruh.forward(49)
            bruh.right(90)
        bruh.end_fill()
        bruh.setposition(-(self.len)/2, self.wid/2 )
        bruh.hideturtle()
        

    def save_image(self, window, i):
        window.getcanvas().postscript(file='Net ' + str(i) +' Roll.jpg')
        img = Image.open('Net '+str(i)+' Roll.jpg') 
        img.save('Net '+str(i)+' Roll.jpg')  
