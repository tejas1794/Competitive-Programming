'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

MORE INFO BELOW (SPOILER ALERT!)

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if str(x)[0]=='-': res = -1*int(str(-1*x)[::-1])
        else: res = int(str(x)[::-1])
        if res > 2147483647 or res < -2147483647:
            return 0
        return res