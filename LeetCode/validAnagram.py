'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Approach: Pretty straight-forward, however, not most optimized. Since we have keep in mind the strings are immutable in Python and we might also get Unicode characters, so our answers should be character independent.
		#My idea thus is to convert both strings to lists, sort them, and simply compare element-wise.
		#Because of sorting, our linear runtime solution goes to O(nlogn).
        res = True
        if (s == "" and t == ""): return True
        s = list(s)
        t = list(t)
        if len(s) == len(t):
            s.sort()
            t.sort()
            for i in xrange(len(s)):
                if s[i] != t[i]: res = False
        else: res = False
        return res