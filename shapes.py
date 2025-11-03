import turtle
screen = turtle.Screen()
t=turtle.Turtle()

# #Draw a square
# for i in range(4):
#      t.forward(100)
#      t.right(90)

# #draw a triangle 
# for i in range(3):
#      t.forward(100)
#      t.right(120)

# color and filling shapes
# t.color("blue", "yellow")
# t.begin_fill()
# t.circle(50)
# t.end_fill()


# Drawing patterns with loops
# t.speed(10)

# for i in range(36):
#      t.forward(100)
#      t.right(170)

# t.shape("turtle")
# t.speed(1)
# for i in range(100):
#      t.forward(5)
#      t.right(5)

# move turtle with  arrow key 

def move_up():
   t.setheading(90)
   t.forward(20)

def move_down():
   t.setheading(270)
   t.forward(20)

def move_left():
   t.setheading(180)
   t.forward(20)

def move_right():
   t.setheading(0)
   t.forward(20)


screen.listen()

screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")

screen.mainloop()



turtle.done() 