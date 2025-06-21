# 	Write a program to find the euclidean distance between two coordinates.

def euc_dist():

    x1,y1 = int(input("Enter x-coordinate first point: ")),int(input("Enter y-coodinate first point: "))
    x2,y2 = int(input("Enter x-coordinate second point: ")),int(input("Enter y-coodinate second point: "))

    d =  ((x2 - x1 )**2 + (y2 - y1)**2)**0.5

    return d


print("Euclidean distance betwween given two points is:" ,euc_dist())

    