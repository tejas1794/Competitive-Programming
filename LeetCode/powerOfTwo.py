'''
Given an integer, write a function to determine if it is a power of two.
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1 or n==2):return True
        if n%2 == 0:
            while(n>2 and n%2<1):
                print n;
                n = n/2;
                if(n<=2): return True
        return False