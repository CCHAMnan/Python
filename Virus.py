from turtle import *
speed(20)
color('cyan')
bgcolor('black')
b = 200
goto(300,0)
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

a = input()