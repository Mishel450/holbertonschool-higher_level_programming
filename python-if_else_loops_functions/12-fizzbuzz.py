#!/usr/bin/python3
def fizzbuzz():
    txt = "{}"
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print(txt.format("FizzBuzz"), end=" ")
        elif (i % 3 == 0 and i % 5 != 0):
            print(txt.format("Fizz"), end=" ")
        elif (i % 3 != 0 and i % 5 == 0):
            print(txt.format("Buzz"), end=" ")
        else:
            print(txt.format(i), end=" ")
