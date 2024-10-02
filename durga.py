from turtle import *
from random import randint

# Set up the turtle
speed(10000)
bgcolor("black")
colormode(255)

# Draw colorful spiral pattern
x = 1
while x < 300:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    pencolor(r, g, b)
    fd(50 + x)
    rt(90.911)
    x += 1

# Function to create multicolored vibrating text
def draw_vibrating_text(text, size):
    penup()
    goto(0, -50)  # Position for the text
    pendown()
    for _ in range(30):  # Number of vibrations
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        pencolor(r, g, b)
        write(text, align="center", font=("Arial", size, "bold"))
        penup()
        goto(randint(-5, 5), randint(-5, 5))  # Random position for vibration effect
        pendown()
        clear()  # Clear the previous text

# Draw "মহালয়া" with a vibrating effect
draw_vibrating_text("মহালয়া", 48)

# Finish up
exitonclick()
