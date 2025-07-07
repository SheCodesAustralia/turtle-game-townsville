---
title: "8. That's a Wrap"
weight: 8
chapter: true
---

Check your code, it should look like the below.

Congratulations, you built yourself a Python game, learnt some things about turtles, and helped save the ocean.

``` python

import turtle
import random

# --- SETUP ---
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.bgpic('image.gif')
screen.title("Turtle Rescue Mission")
screen.setup(width=600, height=600)
screen.tracer(0)

screen.addshape("coral.gif")
screen.addshape("bag.gif")
screen.addshape("can.gif")
screen.addshape("bottle.gif")

# --- OCEAN FACTS / MESSAGES ---
ocean_facts = [
    "Did you know? A plastic bottle can take 450 years to decompose.",
    "Did you know? Sea turtles often mistake plastic bags for jellyfish!",
    "Did you know? Coral reefs support over 25% of all marine life.",
    "Did you know? Only 9% of plastic ever produced has been recycled.",
    "Did you know? Every minute, one garbage truck of plastic enters our oceans.",
]

# --- PLAYER rescueturtle ---
rescueturtle = turtle.Turtle()
rescueturtle.color("pink")
rescueturtle.shape("turtle")
rescueturtle.penup()
rescueturtle.setheading(90)
rescueturtle.goto(0, -250)

# --- SCORE + HEALTH ---
score = 0
health = 3

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.color("white")
score_writer.penup()
score_writer.goto(-250, 260)

health_writer = turtle.Turtle()
health_writer.hideturtle()
health_writer.color("lightpink")
health_writer.penup()
health_writer.goto(150, 260)

# --- OCEAN FACT DISPLAY ---
fact_writer = turtle.Turtle()
fact_writer.hideturtle()
fact_writer.penup()
fact_writer.goto(0, -280)  # Bottom of screen
fact_writer.color("white")
fact_writer.write(random.choice(ocean_facts), align="center", font=("Arial", 17, "italic"))


# --- OBJECTS IN THE OCEAN ---
ocean_objects = []

def create_object():
    obj = turtle.Turtle()
    obj.penup()
    obj.speed(0)
    obj.goto(random.randint(-280, 280), 300)

    # Define multiple options
    trash_options = [
        {"shape": "can.gif", "color": None},
        {"shape": "bottle.gif", "color": None},
        {"shape": "bag.gif", "color": None},
    ]

    reef_options = [
        {"shape": "coral.gif", "color": None},
    ]

    # Choose type
    if random.random() < 0.3:
        obj_data = random.choice(trash_options)
        obj.type = "trash"
    else:
        obj_data = random.choice(reef_options)
        obj.type = "reef"

    # Apply shape and color
    obj.shape(obj_data["shape"])
    if obj_data["color"]:
        obj.color(obj_data["color"])

    ocean_objects.append(obj)

# --- DISPLAY UPDATER ---
def update_display():
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=("Arial", 16, "bold"))
    health_writer.clear()
    health_writer.write("Health: " + str(health), font=("Arial", 18, "bold"))

# --- KEYBOARD MOVEMENT ---
def move_left():
    x = rescueturtle.xcor() - 40
    if x < -280:
        x = -280
    rescueturtle.setx(x)

def move_right():
    x = rescueturtle.xcor() + 40
    if x > 280:
        x = 280
    rescueturtle.setx(x)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

def fall(item):
    global score, health
    item.sety(item.ycor() - 10)

    if item.distance(rescueturtle) < 40 and item.ycor() < -230:
        if item.type == "trash":
            score += 1
        elif item.type == "reef":
            health -= 1
        item.hideturtle()
        ocean_objects.remove(item)

    elif item.ycor() < -300:
        item.hideturtle()
        ocean_objects.remove(item)

# --- MAIN GAME LOOP ---
def game_loop():
    global score, health

    if random.random() < 0.1:
        create_object()

    for obj in ocean_objects:
        fall(obj)

    update_display()

    if health <= 0:
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.goto(0, 0)
        game_over.write("💀 GAME OVER 💀", align="center", font=("Arial", 24, "bold"))
    else:
        screen.update()
        screen.ontimer(game_loop, 100)

# --- START GAME ---
update_display()
game_loop()
turtle.done()


```