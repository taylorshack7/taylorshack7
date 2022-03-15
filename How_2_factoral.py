# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Taylor Shackelford
# Section:        ENGR 102 537
# Assignment:     THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:           DAY MONTH YEAR

print('Just for fun')
print()

print("Please enter a number:", end=' ')
n = int(input())
while n >= 0:
    for i in range(1, n):
        n *= i
    print("Factoral is", n)
    break
if n < 0:
    print("error")