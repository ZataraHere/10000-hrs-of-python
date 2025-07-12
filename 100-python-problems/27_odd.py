# 	Write a program to print the first 25 odd numbers
import itertools

def odd():
    counter = 0
    for i in itertools.count():
        if i % 2 != 0:
            print(i)
            counter += 1
        if counter == 25:
            break

odd()
