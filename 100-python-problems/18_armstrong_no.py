# Write a program that will check whether the number is armstrong number or not.

def armstrong():

    num = int(input("Enter a number to check if its an armstrong number: "))
    s = str(num)
    sum = 0
    for n in s:
        sum += int(n)**len(s)

    if sum == num:
        print(True)

    else:
        print(False)

armstrong()