'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
		#My approach here is to change the integer list to number, add one to it, convert it back to list of int and return it.
        digits = ''.join(str(x) for x in digits)
        print digits
        digits = int(digits)
        digits += 1
        print digits
        digits = [int(x) for x in str(digits)]
        return digits
        
        