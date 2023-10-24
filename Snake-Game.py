"""Python Turtle Graphics Snake Game"""

"""Importing Modules"""
from math import floor
import turtle
import time
import random

"""Defining Variables"""
HEIGHT = 600
WIDTH = 600
#delay = 0.14
class delayThing:
        delayTime = 0.13
        def toggleDelay(delayTime):
                if delayTime == 0.13:
                        delayTime = 0.21
                else: delayTime = 0.13

delay = delayThing()
score = 0
high_score = 0

"""Instantiate Display Window"""
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor('#FFF9ED')
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(0)

"""Instantiate Head of Snake"""
head = turtle.Turtle()
head.shape("square")
head.color("#D9A9B9")
head.penup()
head.goto(0, 0)
head.direction = "stop"

"""Create Food"""
food = turtle.Turtle()
food.color("#666666")
food.shape("square")
food.speed(0)
food.penup()
food.goto(100, 240)
#food.goto(random(range(WIDTH)), random(range(HEIGHT)))

"""Display Text"""
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#123456")
pen.penup()
pen.hideturtle()
pen.goto(0, floor(HEIGHT*0.416))
pen.write(f"Score : {score}    High Score : {high_score}", align="center", font=("Montserrat", 24))

"""Define Key Presses and Movement"""

def go_up():
        if head.heading() != 270 or head.direction == "stop": head.setheading(90); head.direction = "go"

def go_down():
        if head.heading() != 90 or head.direction == "stop": head.setheading(270); head.direction = "go"
def go_right():
        if head.heading() != 180 or head.direction == "stop": head.setheading(0); head.direction = "go"
def go_left():
        if head.heading() != 0 or head.direction == "stop": head.setheading(180); head.direction = "go"
        



"""Instantiate Snake Segments"""
segments = []

"""Define Functions"""
def death():
        time.sleep(1) #short delay to show death
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
                segment.goto(1000, 1000)
        # I don't like this solution--it causes bloat and doesn't destroy the objects
        """segments.clear()
                                # Presumably for scope reasons, values change here but once a new food is had, values go back to what they were
        score = 0
        pen.clear()
        pen.write(f"Score : {score}    High Score : {high_score}", align="center", font=("Montserrat", 24))"""

"""Main Gameplay"""
while True:
        window.listen()
        window.onkeypress(go_up, "w")
        window.onkeypress(go_down, "s")
        window.onkeypress(go_left, "a")
        window.onkeypress(go_right, "d")
        window.onkeypress(delay.toggleDelay(), "l")
        window.update()
        
        # Wall collision
        if head.xcor() > 290 or head.xcor() < -305 or head.ycor() > 305 or head.ycor() < -290:
                death()
                segments.clear()

                score = 0
                pen.clear()
                pen.write(f"Score : {score}    High Score : {high_score}", align="center", font=("Montserrat", 24))

        # Food collision
        if head.distance(food) < 15:
                # Move food elsewhere
                randomX = random.randint(0-(WIDTH/2), (WIDTH/2 -20))
                randomX = randomX - randomX%20
                randomY = random.randint(0-(HEIGHT/2 -20), (HEIGHT/2))
                randomY = randomY - randomY%20
                food.goto(randomX, randomY)
                # Add segment to snake
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color('#DABACA')
                new_segment.penup()
                segments.append(new_segment)
                score += 10
                if score > high_score: high_score = score
                pen.clear()
                pen.write(f"Score : {score}    High Score : {high_score}", align="center", font=("Montserrat", 24))

        # Self collision
        for segment in segments:
                if segment.distance(head) < 15:
                        death()
                        segments.clear()

                        score = 0
                        pen.clear()
                        pen.write(f"Score : {score}    High Score : {high_score}", align="center", font=("Montserrat", 24))


        # Delay between game steps
        time.sleep(delay.delayTime)

        # Move snake
        if head.direction != "stop": head.forward(20)

window.mainloop()


"""
THINGS TO FIX
 - if two directions (i.e. up + left) are input quickly enough, only the second direction is followed
 - fix delay time toggle
 - make segments follow snake
 - darken head and tail to be more maroon
 - create a box around the play area (more visible if you go fullscreen)
"""
