'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true
'''
#Approach: In this solution, I'm using semi-efficient algorithm to search.
#I start with linear search for first dimension of array, and follow it by 
#binary search for the next dimension.
#Runtime for this algorithm is O(n) * (logn) respectively for linear and binary
#search => O(nlogn) general runtime. This may be made better by doing a binary
#search on both dimensions (both dimensions are actually sorted) which will give
#us a better runtime of O(logm)*O(logn).
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in xrange(len(matrix)):
            low = 0
            high = len(matrix[i])-1
            while low <= high: 
                mid = (low+high)//2
                if matrix[i][mid] > target: high = mid-1
                elif matrix[i][mid] < target: low = mid+1
                else: return True
        return False