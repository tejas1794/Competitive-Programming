'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

#Approach: Naive algorithm first try - I'm essentially traversing through the list and returning the location of str(needle) or -1.
#Since this is essentially linear search, perhaps implementing binary search would help getting a linear runtime.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenOfNeedle = len(needle)
        if needle == "": return 0
        for i in xrange(len(haystack)):
            if haystack[i:i+lenOfNeedle]==needle: return i
        return -1