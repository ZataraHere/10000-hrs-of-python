# Write a program that will tell the number of dogs and chicken are there when the user will provide the 
# value of total heads and legs.

'''
chickens + dogs = Total number of heads
2 x chickens + 4 x dogs = total number of legs 
'''
def heads_legs():

    heads = int(input("Enter total number of heads: "))
    legs  = int(input("Enter the total number of legs:"))

    #c+d = heads => c = heads - d
    #2c+4d = legs => 2(heads - d) + 4d = legs => d = (legs -heads)/2

    if legs % 2 != 0:
        return "Invalid input! Number of legs must be even."

    d = (legs - 2 * heads) / 2
    c = heads - d

    if d < 0 or c < 0 or not d.is_integer() or not c.is_integer():
        return "Invalid input! No such combination of chickens and dogs."

    return int(c), int(d)

result = heads_legs()

if isinstance(result, tuple):
    c, d = result
    print(f"Total number of chickens is {c} and total number of dogs is {d}")
else:
    print(result)

