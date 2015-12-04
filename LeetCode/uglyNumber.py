'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''

#My approach: Pretty straight forward, just iteratively go through all the test cases and keep minimizing them until
#we get a number less than 1. Since 1 is considered Ugly and 0 is not, I'm using division a/b != 0 unless a = 0
#instead of continuously substracting them.
#Runtime: O(n) with a constant space complexity, because of a single loop just changing the original number itself.

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<1: return False
        elif num == 1: return True
        while num>1:
            if num%2==0:
                num /= 2
            elif num%3==0:
                num /= 3
            elif num%5==0:
                num /= 5
            else: return False
        return True