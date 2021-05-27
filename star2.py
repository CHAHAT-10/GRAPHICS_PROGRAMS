from turtle import *
speed(10)
bgcolor("black")
color ('red','yellow')
begin_fill()
while True:
   forward(500)
   left(170)
   if abs(pos())<1:
      break
end_fill()
done()