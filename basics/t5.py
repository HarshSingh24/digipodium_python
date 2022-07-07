from turtle import *

speed(100)
bgcolor('black')
pencolor('pink')


penup()
setpos(50,50)
pendown()
for i in range(200,0,-2):
    forward(i)
    left(90)

penup()
setpos(-350,40)
pendown()
for i in range(200,0,-2):
    forward(i)
    left(90)

penup()
setpos(-350,-260)
pendown()
for i in range(200,0,-2):
    forward(i)
    left(90)

penup()
setpos(50,-250)
pendown()
for i in range(200,0,-2):
    forward(i)
    left(90)

mainloop()