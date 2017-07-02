############################
# The goal of this project was to practice the use of functions, with a focus on parameter passing 
# and to use conditionals withing functions to create different parts which will depict a coherent picture.
############################

import turtle
import random

def spaceHouse(house,xcoord,ycoord,size):
    '''
    Draws the body, windows and roof of a house. As input parameters it takes a turtle, the x- and y- coordinates
    for the position of the house, and a size of the house's side
    '''
    house.color("black")
    house.shape("blank")
    house.up()
    house.goto(xcoord,ycoord)
    house.down()
    house.forward(size)
    house.left(90)
    house.forward(size+size/2)
    house.left(90)
    house.forward(size)
    house.left(90)
    house.forward(size+size/2)
    house.up()
    house.goto(xcoord+70,ycoord+5*(size/4))
    house.down()
    #if the house's side is bigger than 150 it draws two windows
    #else it draws just one
    if (size>150):
        for s in range(4):
            house.forward(40)
            house.right(90)
        house.up()
        house.goto(xcoord+150,ycoord+5*(size/4))
        house.down()
        for s in range(4):
            house.forward(40)
            house.right(90)
    else:
        for s in range(4):
            house.forward(40)
            house.right(90)
    house.up()
    house.goto(xcoord,ycoord+size+size/2)
    house.down()
    #the following code draws the roof
    house.color("FireBrick")
    house.begin_fill()
    house.left(90)
    house.forward(size)
    house.left(135)
    house.forward(size-size/3.5)
    house.left(90)
    house.forward(size-size/3.5)
    house.end_fill()
    house.left(135)
def draw_stars(x,size,color):
    '''
    This function draws a star. As an input it takes a turtle, the size of the star, and its color.
    '''
    x.down()
    x.color(color)
    x.begin_fill()
    x.left(45)
    x.backward(size/2)
    x.forward(size/2)
    x.forward(size)
    x.right(70)
    x.forward(size+size/2)
    x.left(140)
    x.forward(size+size/2)
    x.right(65)
    x.forward(size+size/2)
    x.left(130)
    x.forward(size+size/4)
    x.right(45)
    x.forward(size+size/2)
    x.left(120)
    x.forward(size+size/2)
    x.right(45)
    x.forward(size+size/4)
    x.left(130)
    x.forward(size+size/4)
    x.right(80)
    x.forward(size+size/2)
    x.end_fill()

def smiley_sun(x):
    '''
    The function draws a sun which is smiling. As an input parameter it only takes one turtle.
    '''
    x.speed(0)
    x.pensize(40)
    x.color("yellow")
    x.up()
    x.goto(350,240)
    x.down()
    x.begin_fill()
    x.circle(60)
    x.end_fill()
    x.up()
    #the next few lines draw the eyes
    x.pensize(10)
    x.color("black")
    x.goto(330,310)
    x.down()
    x.circle(10)
    x.up()
    x.goto(370,310)
    x.down()
    x.circle(10)
    x.up()
    x.goto(310,280)
    x.down()
    x.right(85)
    x.circle(35,180) #draws a semi-circle with radius 35 for the smile
def main():
    window=turtle.Screen()
    star=turtle.Turtle()
    star.pensize(10)
    star.shape("blank")
    window.bgcolor("Navy")
    colors=["HoneyDew","DeepSkyBlue","Violet","HotPink","Red","Maroon","SandyBrown","Khaki","GreenYellow"]
    star.up()
    star.goto(-330,310)
    for s in range(4):
        for x in range(7):
            star.pensize(10-x)
            #uses random.choice to choose a random color for the stars
            draw_stars(star,20-2*x,random.choice(colors))
            star.up()
            #the position of every new star is determined by x, which goes from 0 to 6
            #if that number is divisible by 2, then it goes forward, if it is divisible
            #by 5 it goes left, else it goes right
            if(x%2==0):
                star.forward(106)
            elif(x%5==0):
                star.left(79)
            else:
                star.right(56)
        star.up()
        star.forward(150)

    sun=turtle.Turtle()
    smiley_sun(sun)
    spaceH=turtle.Turtle()
    spaceH.pensize(10)
    spaceHouse(spaceH,-240,-300,200) #drawing the bigger house
    spaceHouse(spaceH,-350,-300,100) #drawing the smaller house
    window.exitonclick()
main() #calling of the main function
