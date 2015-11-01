'''

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

'''

#Unoptimized solution
class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        for i in xrange(1, len(nums)): # from left to right 
            res[i] = res[i-1] * nums[i-1]
        tmp = 1
        for i in xrange(len(nums)-2, -1, -1): # from right to left
            tmp *= nums[i+1]
            res[i] *= tmp
        return res
        
        