'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example:

Input: strs = ["flower","flow","flight"]
Output: "fl" '''

def longestcommonprefix(strs):

    res = ""
    pref = strs[0]
    for i in range(len(pref)):        # Looping through length of first word
        for str in strs:              # Looping through each word in strs
            if str[i] != pref[i] or i == len(pref):
                return res
        res += pref[i]
    return res

