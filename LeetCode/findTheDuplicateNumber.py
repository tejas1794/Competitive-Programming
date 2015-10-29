'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = quickSort(nums) #sorting the input so I can minimize the check for duplicate number
        for i in xrange(len(nums)):
            if nums[i] == nums[i+1]: return nums[i] #Now that the list is sorted, clearly there will be two numbers one after other. If there's such a number, return that number.
#The for loop in the original method takes linear time with constant space.                 
#Quick sort gives O(nlogn); Sorting is essentially in-place so extra space use is constant => O(1)
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more