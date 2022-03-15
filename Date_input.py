# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Taylor Shackelford
# Section:        ENGR 102 537
# Assignment:     THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:           DAY MONTH YEAR

date = input("Enter Date as MM/DD/YYYY: ")
parts = date.split('/')
month = parts[0]
day = parts[1]
year = parts[2]
print('month is: ', end='')
for m in month:
    print(m, end='')
print()
print('day is: ', end='')
for d in day:
    print(d, end='')
print()
print('year is: ', end='')
for y in year:
    print(y, end='')