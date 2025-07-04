'''
Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).

Note: It may be assumed that the rectangles are parallel to the coordinate axis.

Example :

Input: L1=(0,10), R1=(10,0), L2=(5,5), R2=(15,0)
Output: 1
Explanation: The rectangles overlap.
'''

def doOverlap( L1, R1, L2, R2):
    if R1[0]>0 and L2[0]>0:

        if L2[0]>R1[0]:
            print(False)
        else:
            print(True)
    
    elif L2[0] > 0 and R1[0]<0:
        
        print(False)

    else:
        if L2[0]<R1[0]:
            print(False)
        else:
            print(True)
        
    
doOverlap(L1=(0,2), R1=(1,1), L2=(-2,0), R2=(0,-3))

