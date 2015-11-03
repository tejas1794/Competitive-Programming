'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
'''

#Approach: Extremely simple logic here: I'm using inbuilt python functions to break the given string after each space. Finally, I return the last segment.

class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split(' ')[-1])
        