import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
obstacles = []

def maze():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            character = maze[i][j]
            screenx = -288+(i * 24)
            screeny = 288-(j * 24)
            if character == "X":
                obstacles = turtle.Turtle()
                obstacles.shape("square")
                obstacles.color("black")


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
screen.mainloop()