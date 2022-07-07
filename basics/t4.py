from turtle import *

speed('slowest')
pencolor('blue')
sides = 10
for i in range(sides):
    forward(75)
    left(360/sides)
    dot(30)

mainloop()
    