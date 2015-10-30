'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

#Most Naive idea here is to simply continue asking the API if there's a bad version and return its first occurrence. A simple for loop will do the trick here but will have a O(n) runtime.


## The isBadVersion API is already defined for you.
## @param version, an integer
## @return a bool
## def isBadVersion(version):

#We do have a search algorithm which is way faster. We will use binary search here to minimize the runtime.
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #binary search for first occurrence    
        left = 1
        right = n
        while(left < right):
            mid = left + (right - left)/2 
            if(isBadVersion(mid)): right = mid #found first occurrence, return it.
            else: left = mid + 1
        return left;