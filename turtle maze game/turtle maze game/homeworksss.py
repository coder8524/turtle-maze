import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Globals
obstacle = []
power_ups = []
can_pass_wall = False
speed_boost_active = False

# Constants
TILE_SIZE = 24
OFFSET_X = -288
OFFSET_Y = 288

# Maze grid
maze = [
    "XXXXXXXXXXXXXXX",
    "X   X         X",
    "X XXXXX XXXXX X",
    "X X     X     X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X XXX",
    "X     X X X   X",
    "XXXXX X X X XXX",
    "X     X   X   X",
    "X XXXXX XXXXX X",
    "X             X",
    "XXXXXXXXXXXXX F"
]

# Create maze from characters
def create_maze():
    global finish
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            character = maze[i][j]
            screenx = OFFSET_X + (j * TILE_SIZE)
            screeny = OFFSET_Y - (i * TILE_SIZE)
            if character == "X":
                wall = turtle.Turtle()
                wall.shape("square")
                wall.color("black")
                wall.penup()
                wall.goto(screenx, screeny)
                obstacle.append(wall)
            elif character == "F":
                finish = turtle.Turtle()
                finish.shape("circle")
                finish.color("green")
                finish.penup()
                finish.goto(screenx, screeny)

# Place power-ups in random open spots
def place_power_ups():
    types = ["speed", "teleport", "wallpass"]
    shapes = {"speed": "triangle", "teleport": "circle", "wallpass": "classic"}
    colors = {"speed": "red", "teleport": "purple", "wallpass": "yellow"}

    for _ in range(5):
        while True:
            i = random.randint(0, len(maze) - 1)
            j = random.randint(0, len(maze[0]) - 1)
            if maze[i][j] == " ":
                screenx = OFFSET_X + (j * TILE_SIZE)
                screeny = OFFSET_Y - (i * TILE_SIZE)

                ptype = random.choice(types)
                pu = turtle.Turtle()
                pu.shape(shapes[ptype])
                pu.color(colors[ptype])
                pu.penup()
                pu.goto(screenx, screeny)
                pu.ptype = ptype  # Custom attribute
                power_ups.append(pu)
                break

# Check if move is valid or allow wall pass
def valid_move(x, y):
    global can_pass_wall
    for wall in obstacle:
        if wall.xcor() == x and wall.ycor() == y:
            if can_pass_wall:
                can_pass_wall = False
                return True
            return False
    return True

# Reset speed boost
def reset_speed():
    global speed_boost_active
    speed_boost_active = False
    player.speed(1)

# Check for power-up collision
def check_power_ups():
    global can_pass_wall, speed_boost_active
    for pu in power_ups:
        if player.distance(pu) < 10:
            if pu.ptype == "teleport":
                while True:
                    i = random.randint(0, len(maze) - 1)
                    j = random.randint(0, len(maze[0]) - 1)
                    if maze[i][j] == " ":
                        new_x = OFFSET_X + (j * TILE_SIZE)
                        new_y = OFFSET_Y - (i * TILE_SIZE)
                        player.goto(new_x, new_y)
                        break
            elif pu.ptype == "wallpass":
                can_pass_wall = True
            elif pu.ptype == "speed":
                speed_boost_active = True
                player.speed(10)
                screen.ontimer(reset_speed, 3000)
            pu.hideturtle()
            power_ups.remove(pu)
            break

# Check for reaching the finish
def check_win():
    if player.distance(finish) < 10:
        player.hideturtle()
        finish.hideturtle()
        print("Congratulations! You completed the maze!")
        screen.bye()

# Movement functions
def move_up():
    newx = player.xcor()
    newy = player.ycor() + TILE_SIZE
    if valid_move(newx, newy):
        player.goto(newx, newy)
        check_power_ups()
        check_win()

def move_down():
    newx = player.xcor()
    newy = player.ycor() - TILE_SIZE
    if valid_move(newx, newy):
        player.goto(newx, newy)
        check_power_ups()
        check_win()

def move_left():
    newx = player.xcor() - TILE_SIZE
    newy = player.ycor()
    if valid_move(newx, newy):
        player.goto(newx, newy)
        check_power_ups()
        check_win()

def move_right():
    newx = player.xcor() + TILE_SIZE
    newy = player.ycor()
    if valid_move(newx, newy):
        player.goto(newx, newy)
        check_power_ups()
        check_win()

# Player turtle setup
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(1)

# Key bindings
screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

# Run game
create_maze()
place_power_ups()
player.goto(OFFSET_X + (1 * TILE_SIZE), OFFSET_Y - (1 * TILE_SIZE))
screen.mainloop()
