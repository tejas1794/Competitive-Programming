'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array
'''
#Approach: Literally a no brainer. Min function does not depend upon the sorting of array. Since the pivot is unknown,
#it will be hard to get a constant runtime answer. I'll try Binary search though and see if that's faster than Min().

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)