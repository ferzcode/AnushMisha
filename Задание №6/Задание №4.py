from turtle import *

screensize(7000, 7000)
tracer(0)

k = 15
for i in range(9):
    forward(27 * k)
    right(90)
    forward(30 * k)
    right(90)
penup()
forward(3 * k)
right(90)
forward(6 * k)
left(90)
pendown()

for i in range(9):
    forward(77 * k)
    right(90)
    forward(66 * k)
    right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()