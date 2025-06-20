# 3.	User will input (2numbers).Write a program to swap the numbers
# Take input from user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Display before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swapping logic
a, b = b, a

# Display after swapping
print(f"After swapping: a = {a}, b = {b}")
