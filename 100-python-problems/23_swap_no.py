# 	Write a program that will swap numbers

def swap():
    num1 = input("Enter first number : ")
    num2 = input("Enter second number : ")
    print(f"Before swapping: num1 = {num1} and num2 = {num2}")

    num1, num2 = num2, num1
    print(f"After swapping: num1 = {num1} and num2 = {num2}")

swap()