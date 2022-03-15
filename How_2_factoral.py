# Code to calc factorial w/o packages


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
