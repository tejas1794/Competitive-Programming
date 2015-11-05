'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		
		#Approach: Pretty naive, essentially, I traverse the array for each element and if its a 0, I swap it with the next non zero element, finally I add a 0 at the end and remove the extra instance of the swapped element.
		#Because of it's naivity it takes O(n^2) time with O(1) space complexity to solve the problem. Might be able to do a little better using sort, I'll update as soon as I get that idea working.
        for i in xrange(len(nums)):
            if nums[i] == 0:
                j = i
                while nums[j]==0 and j<len(nums)-1: j+=1
                nums[i]=nums[j]
                nums.append(0)
                nums.pop(j)