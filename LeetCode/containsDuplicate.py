'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

#This was my preliminary approach. Extremely slow but works. Perhaps I'll work on it a little more and update a more faster version.
#Basically, I'm sorting to array so the array is in order such that I can look up the array and not have to hold any number O(1) space complexity.
#I look if any element repeats in the array by traversing it, and change my result boolean to true. If not, no duplicate elements are there and thus it returns false.
#Runtime Complexity for this is around O(nlogn) because of the sort function, as the traversal itself happens in O(n) time.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        res = False
        if len(nums)>1:
            for i in xrange(len(nums)):
                if nums[i-1] == nums[i]: res = True
        return res