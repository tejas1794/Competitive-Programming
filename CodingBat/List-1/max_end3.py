'''
Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array. 

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
'''

def max_end3(nums):
  element = max(nums[0],nums[2])
  nums[0] = element
  nums[1] = element
  nums[2] = element
  return nums
