'''
Day 16: Sorting!

Given a list A={a0,a1,…,aN-1} of unsorted integers, find and print the pair (or pairs) of elements having the minimum absolute difference.

Note: More than one pair of elements may have the same absolute difference.

Input Format

The first line contains a single integer N, denoting the length of list A. 
The second line contains N space-separated integers, a0,a1,…,aN-1, representing the elements in A.

Constraints

2=N=2×105
-107=Ai=107
Ai?Aj,where 0=i<j=N-1
Output Format

Print the space-separated pair of elements having the minimum absolute difference in ascending order. If more than one pair meets this criterion, print them consecutively, separated by a space, in ascending order on a single line. Because we are printing space-separated pairs, some elements may appear more than once in your output.

Sample Input 1

10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 
Sample Output 1

-20 30
Explanation 
The minimum absolute difference is 50 (ABS(30-(-20))=50). The only pair having this difference is (-20,30).

Sample Input 2

12
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470 
Sample Output 2

-520 -470 -20 30
Explanation 
Our minimum absolute difference is 50. The pairs (-470,-520) and (-20,30) both have this difference.

Sample Input 3

4
5 4 3 2
Sample Output 3

2 3 3 4 4 5
Explanation 
Our minimum absolute difference is 1. The pairs (2,3), (3,4), and (4,5) all have this difference. Notice that 3 and 4 appear multiple times, because they are components of more than one pair.

Note: Recall that pairs in the output must be printed in ascending order.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
arraylen = int(raw_input())
array = map(int, raw_input().strip().split())
array.sort()
arr = []
if arraylen>1:
    start = array[1]-array[0]
for i in xrange(arraylen-1):
    comp = array[i+1]-array[i]
    if comp < start: start = comp
for j in xrange(arraylen-1):
    if array[j+1]-array[j]==start: 
        arr.append(str(array[j]))
        arr.append(str(array[j+1]))
print " ".join(arr)