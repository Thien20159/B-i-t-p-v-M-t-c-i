import turtle

turtle.pensize(5)

turtle.pencolor("Blue")

facesize = 200

turtle.penup()

turtle.goto(0, -200)

turtle.pendown()

turtle.circle(facesize)

turtle.fillcolor ("red")

turtle.penup()

turtle.goto(-100,50)

turtle.pendown()

turtle.begin_fill()

turtle.circle(30)

turtle.end_fill()

turtle.penup()

turtle.goto(100, 50)

turtle.pendown()

turtle.begin_fill()

turtle.circle(30)

turtle.end_fill()

turtle.begin_fill()

turtle.circle(30)

turtle.end_fill()

turtle.penup()

turtle.goto(100, 50)

turtle.pendown()

turtle.begin_fill()

turtle.circle(30)

turtle.end_fill()

turtle.penup()

turtle.goto(-100, -70)

turtle.pendown()

turtle.right(90)

turtle.circle(100,180)

turtle.mainloop()