import turtle
obj = turtle.Turtle()
wn= turtle.Screen()
wn.bgcolor("black")
obj.color("white")
obj.speed(0)
for i in range(120):
   obj.circle(i+8)
   obj.left(30)

turtle.done()