# Write a program to print whether a given number is prime number or not

def prime():
    
    num = int(input("Enter a number: "))

    if num < 2:
        print(num,"is not a prime number") 
        return
    
    if num == 2:
        print(num, "is prime number")
        return

    for i in range(2,num):

        if num%i == 0:
            print(num, "is not a prime number")
            return

    print(num,"is prime number")

prime()