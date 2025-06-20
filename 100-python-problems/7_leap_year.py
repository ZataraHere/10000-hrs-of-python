# 	Write a program that will tell whether the given year is a leap year or not.

def leap_year():
    y = int(input("Enter a year: "))

    if y%4 == 0 and y%100 !=0:
        print("Given year is a leap year")
    elif y%4 ==0 and y % 100 == 0  and y % 400 == 0:
        print("Given year is a leap year")
    else:
        print("Given year is not a leap year")        

leap_year()