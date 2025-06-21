# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

def ang_tri():

    first_angle = int(input("Enter first angle: "))
    second_angle = int(input("Enter first angle: "))
    third_angle = int(input("Enter first angle: "))

    if first_angle+second_angle+third_angle == 180:
        print("It will form a triangle")
    else:
        print("It will not form a triangle")

ang_tri()
