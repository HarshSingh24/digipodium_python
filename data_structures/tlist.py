from turtle import *
speed('fastest')
bgcolor('pink')
colors = ['red','blue','green','yellow','purple','orange']

for i in range(500):
    s = len(colors)
    c = colors[i % s]
    pencolor(c)
    forward(i + 25)
    left(360/s)
    for j in range(s):
        forward(100)
        left(60)

mainloop()