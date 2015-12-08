'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        phi = (1 + 5**0.5) / 2.
        return int(round((phi**(n+1) - (1-phi)**(n+1)) / 5**0.5))