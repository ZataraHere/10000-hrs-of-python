# 	User will provide 2 numbers you have to find the HCF of those 2 numbers

def hcf():

    num1= int(input("Enter first no. : "))
    num2 = int(input("Enter second no. : "))
    
    
    while num1 > 0 and num2 > 0:
        
        if num1 > num2:
            num1 = num1%num2

        else:
            num2 = num2%num1

    if num1 == 0:
        print(num2)
    
    else:
        print(num1)

hcf()