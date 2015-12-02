'''

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

'''
#Approach: Simply looping through the string and adding anything which is alphanumeric to an array. Finally, we simply use python slicing to check if a reverse of the array is same as array (thus marking the palindrome). 
#Runtime Analysis: Because of two seperate loops(one to make the array and other to check elements) makes it a linear algorithm. Basically, it has a run complexity of O(n) and space complexity of O(n)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        for i in xrange(len(s)):
            if s[i].isalnum(): a.append(s[i].lower())
        return a[::-1]==a