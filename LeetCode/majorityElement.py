'''
Given an array of size n, find the majority element. The majority element is the element that appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

#My approach: Pretty straight forward, Python already has a function which gives us the max instances of an element. 
#Being a python inbuilt function, it is also extremely fast and thus gives us an answer beating almost all other specifically written
#functions.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(set(nums), key=nums.count)