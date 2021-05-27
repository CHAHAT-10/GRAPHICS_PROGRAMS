import turtle
turtle.pensize(2)
turtle.speed(15)
turtle.bgcolor("black")


for i in range(10):
   for colours in ["yellow", "blue", "white", "green", "red", "pink", "purple"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(10)
turtle.hideturtle()