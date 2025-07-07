---
title: "5. Let's Clean Some Oceans"
weight: 5
chapter: true
---

Next we're going to add some objects to move in our ocean. By the end of this tutorial we will have a few different pieces of rubbish for our turtle rescuer to go and collect - cans, bottles, and plastic bags - as well as some coral reefs that we really don't want our rescue turtle to run into and destroy.

To get started though we are just going to get one object 'falling' through our ocean.

```python

# --- CREATE FALLING OBJECT ---
falling = turtle.Turtle()
falling.shape("can.gif")
falling.penup()
falling.goto(0, 300)

# --- SIMPLE FALL LOOP ---
def fall():
    y = falling.ycor() - 10
    falling.sety(y)
    if y > -300:
        screen.ontimer(fall, 100)

fall()

```
        
What we are are doing is first making our shape to fall - we're telling it to use the image `can.gif` as the shape, and setting it to start at the top of our screen. 

Then we are defining another function using the y coordinates (remember how we editted the x axis earlier?) and telling it to go down 10 pixels at a time. We include a loop so it keeps falling until its at -300 which is the bottom of our page. Finally the last line is calling the function - hey computer - do the thing we called `fall()`.

Nice one! 

Now let's fish that trash out of the ocean when it collides with our rescue turtle.

Replace your fall function with the below (making sure you still leave in the section for creating the falling object, and the line at the end calling the function - `fall()`)

```python

def fall():
    y = falling.ycor() - 10
    falling.sety(y)

    if falling.distance(rescueturtle) < 40 and falling.ycor() < -230:
        falling.hideturtle()

    elif y > -300:
        screen.ontimer(fall, 100)

```

So what's happening here? You'll notice the function starts the same, but we've now got an `if` and `elif` statement. Let's break those down.

```
if falling.distance(rescueturtle) < 40 and falling.ycor() < -230:
        falling.hideturtle()
```

This section is checking if the distance between our rescue turtle and our falling objects is less than 40 pixels AND if the falling object is lower than -230 pixels on the screen. The first part is to check if we collided with something (we can assume in this case if we are within 40 pixels its a collision), but we're also double checking our work by adding the second element - making sure the object is low enough down the screen where our turtle is based. This helps us weed out any unexpected behaviour. 

`elif` stands for else if, in other words we are saying do the first thing and if you can't, do this second thing instead. In this elif we are just telling the falling object to continue falling if its not collided with.

Nice work - we've got some trash appearing, and a mechanism to collide with it and make it disappear from the ocean when we do so. Let's make it a bit harder shall we?