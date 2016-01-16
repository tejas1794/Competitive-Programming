'''
Day 11: 2D-Arrays + More Review!

Given a 6×6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We can find 16 hourglasses in A; we define an hourglass in A to be a subset of values with indexes falling in this pattern in A's graphical representation:

a b c
  d
e f g
The sum of an hourglass is the sum of the values within it.

Your task is to calculate the sum of every hourglass in some 2D Array, A, and print the largest value (maximum of the sums) as your answer.

Input Format

There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A will be in the inclusive range of −9 to 9.

Constraints 
−9≤A[i][j]≤9 
0≤i,j≤5
Output Format

Print the largest (maximum) hourglass sum found in A.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

Sample Input A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4
'''
import sys

arr = []
for i in xrange(6):
    arr.append(map(int, raw_input().strip().split()))
    
total = -sys.maxint-1
for i in xrange(1, 5):
    for j in xrange(1,5):
        partial = arr[i][j]+arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
        if partial > total:
            total = partial
print total