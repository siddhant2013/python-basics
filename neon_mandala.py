# part 1 - import and screen setup
#turtle.screen() creates the canvas we draw on.
#bgcolor("black") sets the background -- neon colors pop on black!
#title() sets the text that appears in the window's title bar.
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")

# part 2 - create the turtle pen
# turtle.Turtle() creates our drawing pen.
#speed("fastest") skips the slow animation so it draws instantly.
#hideturtle() hides the arrow shape -- only the art is visible
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

#part 3 - outer color spiral (movement + loops + color)
# forward(n) moves the turtle forward n pixels
# right(91) turns it 91 degrees -- 1 degree extra creates the spiral drift!
# The for loop repeats 80 times, growing the distance each round.
# colors[i % len(colors)] cycles through the color list endlessly.
colors=["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)
    board.right(91)

    #part 4 - pen control:move to center and draw a filled star
    # penup() lifts the pen so moving doesnt draw a line
    # goto(0,0) teleports the turtle to the exact center of the canvas
    # pendown() puts the pen back on the canvas -- drawing starts again
    #begin_fill() + end_fill() fills the shape with the chosen color.
    # A 5 pointed star turns 144 degrees at each point.
board.penup()
board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

    # part 5 - inner petal ring(nested loop + fill)
    # the outer loop spins at 360 degrees (36 petals x 10 degrees each)
    # inner loop draws one square petal each rotation.
    #nesting loops inside loops is how complex patterns are built!
board.penup()
board.goto(0,0)
board.pendown()
petal_colors = ["cyan", "lime", "violet", "orange", "deeppink"]
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)],
                petal_colors[(i+2) % len (petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)

#keep window open
turtle.done()