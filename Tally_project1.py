# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Taylor Shackelford
# Section:        ENGR 102 537
# Assignment:     Lab 12b
# Date:           26/ 11/ 2019
import turtle


def vert_line(x, y, h):  # function to repeatedly call upon to draw a vertical line with x, y coordinates
    """ The function, vert_line, will create vertical lines that serve as tallies in the turtle graphic """
    turtle.up()  # pull pen up
    turtle.goto(x, y)  # go to specified position
    turtle.down()  # put pen down on coordinate to iniate the drawing process
    turtle.goto(x, y - h)  # draw the line to new coordinate


# function to draw tally mark set
def line_set(x, y, h):
    """The function, line_set, will form a set of lines using the vert_line function continuously until
    four lines are created"""
    x1 = x
    # 4 vert lines
    for j in range(4):
        vert_line(x1, y, h)
        x1 += 20
    # drawing the line crossing the other lines
    turtle.up()  # pick the pen up, sir
    turtle.goto(x - 5, y - h / 2)  # go to this point, pls
    turtle.down()  # put the pen down, sir
    turtle.goto(x1 - 15, y - h / 4)  # draw until this specific point, pls


def incomplete(x, y, h, total):  # function to draw tally marks that are < 5
    """The function, incomplete, creates lines for a group of tallies that does not have five and will
    also draw a singular line"""
    x2 = x  # set variable equal to x
    for j in range(total):
        vert_line(x2, y, h)
        x2 += 10


num = int(input("Please enter a integer between 1-100 please: "))  # prompt user for integer for tally count
set = num // 5  # using // to find the amount of sets needed
extra = num % 5  # using modulo division to find the amount left over that doesn't quite make a set
# creating turtle window
turtle.setup(width=500, height=500)  # setting height and width in turtle graphic window
turtle.pensize(5)  # setting the width of the pen
turtle.speed(3)  # I like to watch turtle draw slower... you should too
turtle.title('Tally Marks')  # labels turtle pop up window
x = -240  # starting x coordinate in turtle graphic window
y = 250  # starting y in turtle window
h = 78  # the height of one tally line
for i in range(1, set + 1):  # drawing the complete set of tally marks
    line_set(x, y, h)  # call function for drawing tally mark sets
    x += h  # move coordinates to draw
    if i % 5 == 0:  # moving below the five sets to dra more sets
        x = -240  # reset x position and the y  too
        y -= h + 50
if extra > 0:  # if an extra set exits it will be drawn
    incomplete(x, y, h, extra)  # call incomplete set function to draw the incomeplete set
turtle.st()  # show me the turtle when drawing pls
turtle.done()  # end turtle drawing
# thanks
