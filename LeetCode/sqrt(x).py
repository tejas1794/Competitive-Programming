'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''



class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x**(0.5))