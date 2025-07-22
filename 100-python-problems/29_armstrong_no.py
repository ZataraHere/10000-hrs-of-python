#	Print all the armstrong numbers in the range of 100 to 1000

def armstrong(num):

    dup = num
    cnt = 0
    L = []
    sum = 0
    while num>0:
        lastdigit = num%10
        cnt += 1
        num = num//10
        L.append(lastdigit)
    for i in L:
        sum += i**cnt

    if sum == dup:
        return True
    else:
        return False
        
print(armstrong(1634))

