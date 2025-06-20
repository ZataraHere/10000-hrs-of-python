#	Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

def reverse():

    num = input("Enter a 4 digit number: ")
    rev =  num[::-1]
    if int(num) == int(rev):
        print(f"Reverse number is: {rev} and reverse is True")
    else :
        print(f"Reverse number is: {rev} and reverse is False")
    

reverse()