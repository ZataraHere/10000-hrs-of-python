'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example :

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4]
'''

def plusone(digits):
    new_num = 0
    for i in range(len(digits)):
           nums = digits[::-1]
           new_num += nums[i]*(10**i)  

    num =str( new_num +1)
    final_num = [int(x) for x in num]

    return final_num
print(" Number",plusone([1,2,3,4]))
#plusone([1,2,3])