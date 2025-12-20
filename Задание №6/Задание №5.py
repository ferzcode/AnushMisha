from turtle import *

tracer(0)
screensize(10000, 10000)

k = 30

for i in range(6):
    forward(20 * k)
    right(90)
    forward(24 * k)
    right(90)
penup()
forward(7 * k)
right(90)
forward(9 * k)
left(90)
pendown()
for i in range(6):
    forward(26 * k)
    right(90)
    forward(10 * k)
    right(90)

update()
done()