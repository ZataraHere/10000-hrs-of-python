 #Find the Index of the First Occurrence in a String

'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example :

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.'''

def strStr(haystack, needle):
    x = len(needle)
    y = len(haystack)
    if x > y:
        return -1
    else:
        for i in range(0, y - x + 1):  
            if haystack[i:i + x] == needle:
                return i
    return -1  