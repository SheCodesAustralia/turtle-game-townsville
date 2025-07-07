import turtle
import random

# --- SETUP ---
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Falling Pong: Catch the Good, Dodge the Bad")
screen.setup(width=600, height=600)
screen.tracer(0)

# --- PLAYER PADDLE ---
paddle = turtle.Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color("darkgreen")
paddle.penup()
paddle.goto(0, -250)

# --- SCORE + HEALTH ---
score = 0
health = 3

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-250, 260)

health_writer = turtle.Turtle()
health_writer.hideturtle()
health_writer.penup()
health_writer.goto(150, 260)

# --- FALLING OBJECTS ---
falling_objects = []

def create_object():
    obj = turtle.Turtle()
    obj.penup()
    obj.speed(0)
    obj.goto(random.randint(-280, 280), 300)
    if random.random() < 0.7:
        obj.shape("circle")
        obj.color("grey")
        obj.type = "good"
    else:
        obj.shape("triangle")
        obj.color("coral")
        obj.type = "bad"
    falling_objects.append(obj)

# --- DISPLAY UPDATER ---
def update_display():
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=("Arial", 14, "bold"))
    health_writer.clear()
    health_writer.write("Health: " + str(health), font=("Arial", 14, "bold"))

# --- KEYBOARD MOVEMENT ---
def move_left():
    x = paddle.xcor() - 40
    if x < -280:
        x = -280
    paddle.setx(x)

def move_right():
    x = paddle.xcor() + 40
    if x > 280:
        x = 280
    paddle.setx(x)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# --- MAIN GAME LOOP ---
def game_loop():
    global score, health

    if random.random() < 0.05:
        create_object()

    for obj in falling_objects[:]:
        obj.sety(obj.ycor() - 10)

        if obj.distance(paddle) < 40 and obj.ycor() < -230:
            if obj.type == "good":
                score += 1
            else:
                health -= 1
            obj.hideturtle()
            falling_objects.remove(obj)

        elif obj.ycor() < -300:
            obj.hideturtle()
            falling_objects.remove(obj)

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
