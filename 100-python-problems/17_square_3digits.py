#	Write a program that will take three digits from the user and add the square of each digit.

def sum_of_squares():
     
     num1 = float(input("Enter first no.: "))
     num2 = float(input("Enter second no.: "))
     num3 = float(input("Enter third no.: "))

     sum = num1**2 + num2**2 + num3**2

     return sum

print("Sum of squares of three numbers is:",sum_of_squares())