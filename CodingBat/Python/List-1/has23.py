'''
Given an int array length 2, return True if it contains a 2 or a 3. 

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
'''

def has23(nums):
  return(nums[0] in range(2,4) or nums[1] in range(2,4))

