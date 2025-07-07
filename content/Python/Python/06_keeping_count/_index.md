---
title: "6. Keeping Count"
weight: 6
chapter: true
---

So now we have some objects in our ocean - but we want to keep track of them using a scoreboard system.

Just above our game logic, towards the end of our code we want to add 

```python

def update_display():
    score_writer.clear()
    health_writer.clear()
    score_writer.write(f"Score: {score}", font=("Arial", 16, "bold"))
    health_writer.write(f"Health: {health}", font=("Arial", 16, "bold"))

update_display()

```
You'll notice we already had `score_writer` and `health_writer` set up in our code but we weren't doing anything with them because our scoreboard wasn't operational. Here we are making a function called `update_display()` which is going to first clear whatever was there, and then write our score in, and our health checker.

If we run our code now it won't work, we also want to update our `def fall()` one more time to the below:

```python

def fall():
    global score, health
    y = falling.ycor() - 10
    falling.sety(y)

    if falling.distance(rescueturtle) < 40 and falling.ycor() < -230:
        if falling.shape() == "can.gif":
            score += 1
        else:
            health -= 1
        update_display()
        falling.hideturtle()
    elif y > -300:
        screen.ontimer(fall, 100)
```

Can you spot the difference between the code we had before and what we have now? We've added the global variables `score`, and `health` which we used in the code block we just wrote. We also added in `score += 1` and `health -= 1` to make our scoreboard reflect the action that's taking place on the screen, and we've added in our newly built function `update_display()` to be called each time the falling shape collides with our turtle.

We're so close gals! Let's keep swimming.