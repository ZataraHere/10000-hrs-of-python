'''Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.'''

def isPalindrome(x):
    num = x
    rev = 0
    while num>0:
        last_digit = num%10
        rev = rev*10 + last_digit
        num = num//10
    if rev == x:
        return True
    else:
        return False
        
x = int(input("Enter a number or a name: "))
print(isPalindrome(x))