---
title: "7. Just Keep Swimming"
weight: 7
chapter: true
---

Our next step is to add more things to the ocean. Currently we've just got one thing falling which isn't very challenging.

Let's replace our section about creating falling objects and replace it with the below. Delete the create falling objects section, paste in the snippet below and then let's walk through it.

{{% notice tip %}}
The section we mean looks like this 
```python
# --- CREATE FALLING OBJECT ---
falling = turtle.Turtle()
falling.shape("can.gif")
falling.penup()
falling.goto(0, 300)
```
{{% /notice %}}

``` python

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

```

So let's step through this. First of all we are making an `array` with the line `ocean_objects = []`. An array is a list of things, like your shopping list or to-do list. Python saves it in a specific way so we can call upon it later on.

Next we are creating another function, just like we did earlier. Notice how similar `create_object` is to our previous code with `falling`? What we are doing is just making it a bit easier to add things to our list of objects that can fall - because we want LOTS of things in our beautiful diverse ocean. By wrapping it in a function, the computer can run the code again and again and again if we ask it to. 

Next we have a couple more arrays with `trash_options` and `reef_options`. This means we have 3 different things under the umbrella term 'trash' and one thing under the term 'reef'. The opportunities are endless here - we could absolutely add some more options for our turtle to chase through the sea. You'll notice the different types of objects are ones we downloaded earlier in our starter code - with the gifs to match the names.

Let's tackle the next block together. 

```if random.random() < 0.3:``` 

`random.random()` returns a random decimal between 0.0 and 1.0. There’s a 30% chance that this condition is true. So 30% of the time, the game will spawn trash. The other 70% of the time, it spawns a reef hazard. When you finish this page, come back to this step and play around with different values to make the game easier to harder. 

```random.choice(trash_options)```
Both trash_options and reef_options are lists that contain different types of trash or reef image data (like "bag.gif", "coral.gif", etc.). Remember how we made them just above here? `random.choice()` selects one random item from the relevant list to use for the object’s appearance.

```obj.type = "trash"```
This sets a custom property on the object so the game knows how to treat it:

If it's "trash", the game increases the score when collected.

If it's "reef", you lose health from hitting the hazard.

``` 
    obj.shape(obj_data["shape"])
    if obj_data["color"]:
        obj.color(obj_data["color"])
```
This last section is telling Python how to display the object - pulling the shape and colour out of the array we made earlier.

The last thing we are doing is `ocean_objects.append(obj)`. This bit is really important as its adding allllllll the things we just made to our ocean_objects array. Notice how at the top the array is empty (signified by []). This means when the code starts it doesn't have anything in mind when we say ocean objects - it's like its never been to the beach before! Through running our `create_object` function we are teaching the script a little bit about the ocean, adding in info about the bottle, can, bag and reef as we go. When we get down to this step we are telling it cool, take all that info we taught you and add it to the list of `ocean_objects` so we can use it later on.

## Falling Loop

We're going to play a bit of spot the difference now. We have our simple fall loop which was working before, but isn't now because we took away `falling`. Below is the before and after of our new fall loop. What's changed? Update yours.

{{< tabs >}}
{{% tab name="Before" %}}
```python
# --- SIMPLE FALL LOOP ---
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

fall()
```
{{% /tab %}}
{{% tab name="After" %}}
```python
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
```
{{% /tab %}}
{{< /tabs >}}

Did you notice how most of it actually stayed the same? We're only swapping `falling` for `item`, and instead of telling it that only the shape `can.gif` should fall we are telling it to go and look for that list of reef items and trash items we just made and pull those in. 

## The Final Countdown!

We've got one more change to make to make our code run as expected and then we are *done*.

Go all the way to the end of your code and delete the lines 
```python
update_display()

# --- START GAME ---
turtle.done()

```

We are going to be rewriting those in the below snippet so its a bit unnecessary to include it again here.

At the very bottom of your code, paste the below snippet in.

``` python

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

Does any of this look familiar now? We are creating yet another function which starts with `def game_loop()`. This will be where all our main gameplay will be happening. We need to add a global variable in of `score` and `health`. Variables that are created outside of a function are known as global variables. Global variables can be used by everyone, both inside of functions and outside. In this case we have defined the variable towards the top of our code assigning it the values 0 and 3 respectively. We then use these variables in a couple of different functions - we use it in `game_loop` and in `fall`. A global variable helps python to know that when we are talking about score, its the same one we are using all across our code.

Next we are using a bit of randomness so that the objects appear at different rates. Earlier our random.random was < 0.3 or 30%, this time its < 0.1 or 10%. So 10% of the time its creating a new object to fall from the top of our screen (and remember we made `create_object` so that it includes all the different types of reef and trash). The next snippet is telling it *what to do* once that object has been created, ie to fall.

Next we are running the function `update_display` so that its constantly checking if we've lost any health or gained any points. Try running your code without this line and see what happens - the game will still end but even if you've collected trash you won't have any points to show for it.

And finally this section at the bottom.
```
    if health <= 0:
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.goto(0, 0)
        game_over.write("💀 GAME OVER 💀", align="center", font=("Arial", 24, "bold"))
    else:
        screen.update()
        screen.ontimer(game_loop, 100)
```
This section is saying if our health reaches 0 to proceed to game over - making another turtle to write Game Over on our screen. Else, if the game isn't over yet, update the screen and keep the loop going - forever if you play well enough!!

That's our game loop done!

The last bit we needed to add was 

```
# --- START GAME ---
update_display()
game_loop()
turtle.done()
```

This bit is just saying that on startup update the game display first, then run the game loop for as long as we need to, and then when it's finished to leave the window open. The command `turtle.done()` causes the program to pause until you closes the Python Turtle Graphics window. This is so you have time to check out your score before the game closes. Without this line, the graphics window would be closed right after the program is finished.

## The finishing touch

You might notice your code is a bit jumpy when you run it. We can add this line in to our screen setup towards the top of our code in the section SETUP. It just turns off automatic screen updates which makes the play experience a bit nicer.

```python

screen.tracer(0)

```

And that's it folks! You've built yourself a game!



