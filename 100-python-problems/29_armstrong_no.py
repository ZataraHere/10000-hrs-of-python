def armstrong(num):
    dup = num
    cnt = len(str(num)) 
    sum = 0

    while num > 0:
        last_digit = num % 10
        sum += last_digit ** cnt
        num = num // 10

    return sum == dup

print(armstrong(153))  # Output: True
print(armstrong(9474)) # Output: True
print(armstrong(123))  # Output: False
