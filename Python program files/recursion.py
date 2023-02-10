import turtle
import operator 
import random

def poly_angle(sides):
    angle=  ((sides-2)*180/sides)
    return angle


def poly(sides, t, l,c):
    if l > sides*2:
        # for i in range(len(c)):
        #     if c[i] <=50:
        #         c[i] = 255
        # rand = random.randint(0,2)
        # c[rand] -= random.randint(20,50)
        # c[rand] -= 50
        # print(c)
        angle = poly_angle(sides)
        for i in range(sides):
            poly(sides,t,int((l*(sides/2))/(sides)),c)
            t.color(tuple(c))
            t.fd(l)
            t.rt(angle-180)
        t.fd(l)

poly_c = input("enter the number of polygon sides: ")

s_turtle = turtle.getscreen()
t = turtle.Turtle()
s_turtle.bgcolor("black")
t.pencolor("white")
t.color("white")
t.speed(200)
t.penup()
s_turtle.screensize(2000,2000)
t.goto(0,-900)
t.pendown()
s_turtle.colormode(255)
c=[255,255,255]

poly(int(poly_c),t,150,c)

input("Press any key to exit ...")