# Calculates y=mx+b as well as y-int and y 
print('This program will calculate the best fit line for all the points you input')
print('you will then have the user input an x value and finds its y value along the best fit line')

# Part 1: setting variables and storing data points
n = 'start'
x = 0
x_axis = []
y = 0
y_axis = []
print('Enter as many coordinates as you\'d like. Type \'stop\' to stop')
# this loop is so that we can keep on asking the user for inputs
while n != 'stop':
    n = input('Enter in x,y coordinates:') # user inputs the coordinates in the form x,y
    if n != 'stop':
        coordinate = n.split(',', 2)  # converts the input into a list with the x element in index 0, and y element
        # in index 1
        x = float(coordinate[0])  # converts the x-coor into a float since it was a string
        x_axis.append(x)  # adds the x to a list for just the x-coor
        y = float(coordinate[1])  # converts the y-coor into a float since it was a string
        y_axis.append(y)  # adds the y to a list for just the y-coor
    else:
        continue

# Part 2: finding the mean of entered values
x2 = sum(x_axis) / (len(x_axis))  # this is the mean value of all the x's
y2 = sum(y_axis)/(len(y_axis))  # this is the mean value of all the y's
sum1 = 0  # defines the variable sum1 to be 0
sum2 = 0  # defines the variable sum2 to be 0
# the formula we used is the sum of all the y's minus the mean(y) * all the x's minus the mean(x)
# then all of that divided by the sum of all the y's minus the mean(y) squared
for i in x_axis:
    i -= x2  # x minus the mean for all x's
    for j in y_axis:
        y_axis.remove(j)  # removes the y so it wont loop again for the next x
        j -= y2  # y minus the mean for all y's
        sum1 += (i*j)  # adds the product of the x-mean(x) times y-mean(y)
        sum2 += (i ** 2)  # adds y squared
        break  # breaks it because we only want to to the evaluation with the x and its corresponding y

# Part 3: calculating slope of best fit line and y-int
slope = sum1/sum2  # finds the slope of the best fit line
print(round(slope, 2), 'is the slope of the best fit line') # outputs the slope and rounds it to the tenth place
y_int = y2 - (slope * x2)  # solve for the y intercept with the slope and the mean of both x and y
print(round(y_int, 2), 'is the y intercept')  # outputs the y-int and rounds it to the tenth place

# Part 4: determining the y value using linear interpretation
value_x = float(input('Enter a value for x:'))  # asks the user to input an x value
# this will then be plugged into the line formula and will give us a y value
y_bl = slope * value_x + y_int
print("Y value for given x:")
print(round(y_bl, 2))  # outputs the y value and rounds it to the tenth place
# Thanks

