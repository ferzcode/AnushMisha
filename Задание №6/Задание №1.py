from turtle import *

screensize(7000, 7000)
tracer(0)
k = 12

for i in range(3):
    forward(39 * k)
    right(90)
    forward(48 * k)
    right(90)
penup()
forward(27 * k)
right(90)
forward(24 * k)
left(90)
pendown()
for i in range(3):
    forward(29 * k)
    right(90)
    backward(18 * k)
    right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()