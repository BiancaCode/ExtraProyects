# draw a red circle
# By bichicode

import turtle
from turtle import bye


turtle.penup()

# I don't like the cursor
turtle.hideturtle()

# Set position
turtle.goto(0, -75)

# draw the circle
turtle.pendown()

turtle.pencolor("red")

# color the circle
turtle.fillcolor('red')

turtle.begin_fill()

turtle.circle(150, 360)

turtle.end_fill()

turtle.penup()

# My name
turtle.goto(0, -160)

turtle.pendown()

turtle.color('purple')

style = ('Courier', 20, 'italic')

turtle.write('Bichicode', font=style, align='center')

# Close with enter
turtle.onkeypress(bye, '\r')

turtle.listen()

turtle.done()
