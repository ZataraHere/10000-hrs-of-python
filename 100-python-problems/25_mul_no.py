#	Write a program that can multiply 2 numbers provided by the user without using the * operator
import math
def mul():

    num1 = float(input("Enter first no.: "))
    num2 = float(input("Enter second no.: "))

    output = 0

    if num1 == 0 or num2 == 0:
        output = 0

    for i in range(1,num2+1):
        output += num1

    return output

print("Multiplication of two numbers:", mul())
