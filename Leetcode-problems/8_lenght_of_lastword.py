'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example :

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''

def lastword(s):

    new = s.split()
    last_word = len(new[-1])
    return last_word


print(lastword("luffy is still joyboy"))

