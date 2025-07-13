#	Print all the armstrong numbers in the range of 100 to 1000

def armstrong():

    num = input("Enter a number: ")
    pow = len(num)
    sum = 0

    for i in num:

        sum += int(i)**pow
    if sum == int(num):
        print("Its a armstrong number")

    else:
        print("Its not a armstrong number")    

armstrong()

