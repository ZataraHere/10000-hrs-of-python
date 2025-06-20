# 3.	User will input (2numbers).Write a program to swap the numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"Before swapping: a = {a}, b = {b}")

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
