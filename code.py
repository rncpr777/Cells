import turtle

turtle.penup()
turtle.goto(-250, -250)
x = -250
turtle.width(10)
for i in range(11):
    turtle.pendown()
    turtle.goto(x, 150)
    turtle.penup()
    x = x + 40
    turtle.goto(x, -250)
turtle.goto(-250, -250)
y = -250
for i in range(11):
    turtle.pendown()
    turtle.goto(150, y)
    turtle.penup()
    y = y + 40
    turtle.goto(-250, y)
turtle.goto(-250, -250)
turtle.done()
