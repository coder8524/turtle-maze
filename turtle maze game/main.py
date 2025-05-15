import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
obstacle = []

def create_maze():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            character = maze[i][j]
            screenx = -288+(i * 24)
            screeny = 288-(j * 24)
            if character == "X":
                obstacles = turtle.Turtle()
                obstacles.shape("square")
                obstacles.color("black")
                obstacles.penup()
                obstacles.goto(screenx,screeny)
                obstacle.append(obstacles)

            if character == "F":
                finish = turtle.Turtle()
                finish.shape("circle")
                finish.color("green")
                finish.penup()
                finish.goto(screenx,screeny)
                finish.pendown()

                
def valid_move(x,y):
    for obstacless in obstacle:
        if obstacless.xcor()== x and obstacless.ycor() == y:
            return False
    return True
def check_win():
    if player.distance(finish) < 10:
        player.hideturtle()
        finish.hideturtle()
        screen.bye()
        print("congratulations you completed the maze")

def move_up():
    newx = player.xcor() 
    newy = player.ycor() + 24
    if valid_move(newx,newy):
        player.goto(newx,newy)
        check_win()

def move_right():
    newx = player.xcor() + 24
    newy = player.ycor()
    if valid_move(newx,newy):
        player.goto(newx,newy)
        check_win()

def move_left():
    newx = player.xcor() -24
    newy = player.ycor()
    if valid_move(newx,newy):
        player.goto(newx,newy)
        check_win()

def move_down():
    newx = player.xcor()
    newy = player.ycor() - 24
    if valid_move(newx,newy):
        player.goto(newx,newy)
        check_win()
# Register shapes
turtle.shape("square")
turtle.speed(100)


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

# Turtle setup
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)

screen.listen()
screen.onkey(move_down,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(move_up,"w")

create_maze()
player.goto(-264,264)
screen.mainloop()