import turtle

numDiamonds = 40
angleOfRotation = 360/numDiamonds

def draw_diamond(myTurtle, length):
   myTurtle.left(15)
   myTurtle.forward(length)
   myTurtle.right(30)
   myTurtle.forward(length)
   myTurtle.right(150)
   myTurtle.forward(length)
   myTurtle.right(30)
   myTurtle.forward(length)
   myTurtle.right(165)

def draw_diamond_flower(myTurtle, length):

   for i in range(1, numDiamonds+1):
      draw_diamond(myTurtle, length)
      myTurtle.right(angleOfRotation)

def draw_flower_stick(myTurtle, length):
   myTurtle.right(180)
   myTurtle.forward(length)

canvas = turtle.Screen()
pacman = turtle.Turtle()
pacman.shape("turtle")
pacman.shapesize(1, 1, 1)
pacman.color("black")
pacman.pensize(2)
canvas.bgcolor("white")
pacman.speed(0)

pacman.left(90)
draw_diamond_flower(pacman, 80)
draw_flower_stick(pacman, 300)
canvas.exitonclick()
