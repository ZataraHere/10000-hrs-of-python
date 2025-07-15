#	Write a program to print all the unique combinations of 1,2,3 and 4

import itertools
def comb():

    nums = [1,2,3,4]
    for i in range(1, len(nums)+1):
        for combo in itertools.combinations(nums, i):
            print(combo)

comb()
