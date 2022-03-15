# This program creates a random list of ten even numbers between 0 - 100 then finds max, min, and mean

import random


def ran_operations():
    random_list = []
    for l in range(0, 10):  # runs loop ten times
        ran = random.randrange(0, 100, 2)  # gets 10 random even numbers between 0 - 100
        random_list.append(ran)
    mini = min(random_list)
    maxi = max(random_list)
    mean = sum(random_list) / len(random_list)
    return mini, maxi, mean


print("This function creates a random list of ten even numbers between 0 - 100 then finds max, min, and mean")
print(ran_operations(), "(min, max, mean)")
