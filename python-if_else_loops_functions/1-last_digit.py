#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 0
if (number < 0):
    number = number * -1
    flag = 1
lastd = number % 10
if (flag == 1):
    number = number * -1
    lastd = -1 * lastd
if (lastd > 5):
    print(f"Last digit of {number} is {lastd} and is greater than 5")
elif (lastd == 0):
    print(f"Last digit of {number} is {lastd} and is 0")
else:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
