# Write a program that asks the user how many Fibonnaci numbers
# and a draw a visualization with turtle.

import turtle


fibo = {1: 1, 2: 2}

for i in range(3, int(input())):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

turtle.pendown()
i = 0
for k, v in fibo.items():
    turtle.width(1 if k < 8 else i)
    for i in range(4):
        turtle.forward(v)
        turtle.right(90)
    turtle.right(90)
    i += 1
    turtle.forward(v)
turtle.done()
