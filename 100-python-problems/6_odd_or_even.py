#	Write a program that will tell whether the number entered by the user is odd or even.

def odd_or_even():
    x = int(input("Enter a number:"))
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
    
print("Number is",odd_or_even())