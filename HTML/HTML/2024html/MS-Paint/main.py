#make 4 more func that do special cmd when a key was pressed
import turtle as t
def forward():
  t.forward(47)
def backwards():
  t.left(180)
  t.forward(47)
def Left():
  t.left(60)
def right():
  t.right(60)
def penup():
  t.penup()
def pendown():
  t.pendown()
def square():
  pass  
t.color("blue")
t.pensize(42)
screen = t.Screen()
screen.listen()
screen.onkey(forward,"f")
screen.onkey(backwards,"b")
screen.onkey(Left,"l")
screen.onkey(right,"r")
screen.exitonclick()
