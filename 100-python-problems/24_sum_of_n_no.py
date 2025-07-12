# Write a program to find the sum of first n numbers, where n will be provided by the user. 
# Eg if the user provides n=10 the output should be 55.

def sum_of_n(n):
    sum = 0
    for i in range(n+1):
        sum += i

    return sum

print(" sum of n numbers:", sum_of_n(100))
