# 	Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

def si():

    p = int(input("Enter principle value in Rs: "))
    r = int(input("Enter rate of interest in %: "))
    t = int(input("Enter time in years: "))

    si = p*r*t/100

    return si

print(" Simple interest :",si())