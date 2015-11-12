'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

#Approach: Simply using the inbuilt functionality of Python. Not the fastest idea, but should be the simplest.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x**(0.5))