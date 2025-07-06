# 	Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%),
#  and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).

def salary():
    org = int(input("Enter the total salary:"))
    k = org - 0.18*org
    if 500000 <= org <= 1000000:
        in_hand_sal = k - 0.1*org

    elif 1100000 <= org <= 2000000:
        in_hand_sal = k - 0.2*org

    elif org > 2000000:
        in_hand_sal = k - 0.3*org

    else:
        in_hand_sal = k

    return in_hand_sal

print("The in-hand salary after deduction of HRA,DA,PF,and tax is",salary())