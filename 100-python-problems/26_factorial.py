# Write a program that can find the factorial of a given number provided by the user.

def fact():

    num = int(input("Enter a number: "))

    fact = 1
    if num == 0:
        fact = 1
    for _ in range(1,num):
        num *= _
        fact = num

    return fact

print("Factorial: ", fact())