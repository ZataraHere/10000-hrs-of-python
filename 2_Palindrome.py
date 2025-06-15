'''Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.'''

def isPalindrome(x):
    x = str(x)

    if x == x[::-1]:
        return True
    else:
        return False
x = input("Enter a number or a name: ")
print(isPalindrome(x))