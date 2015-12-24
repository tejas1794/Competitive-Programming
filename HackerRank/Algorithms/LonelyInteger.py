'''
Problem Statement

There are N integers in an array A. All but one integer occur in pairs. Your task is to find the number that occurs only once.

Input Format

The first line of the input contains an integer N, indicating the number of integers. The next line contains N space-separated integers that form the array A.

Constraints

1=N<100 
N % 2=1 (N is an odd number) 
0=A[i]=100,?i?[1,N]
Output Format

Output S, the number that occurs only once.

Sample Input:1

1
1
Sample Output:1

1
Sample Input:2

3
1 1 2
Sample Output:2

2
Sample Input:3

5
0 0 1 2 1
Sample Output:3

2
Explanation

In the first input, we see only one element (1) and that element is the answer. 
In the second input, we see three elements; 1 occurs at two places and 2 only once. Thus, the answer is 2. 
In the third input, we see five elements. 1 and 0 occur twice. The element that occurs only once is 2.
'''

#!/usr/bin/py
def lonelyinteger(a):
    a.sort()
    answer = a[0]
    for i in xrange(0,len(a)-2,2):
        if a[i]!=a[i+1]: 
            return a[i]
    if len(a)!=1: return a[-1]
    else: return answer

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
	
#This is one of the most direct solutions I thought of.
#As this problem resides in Bit Manipulation Sub Domain, the same solution
#may be derived using bitwise xor (basically just change the for loop such that
#answer = answer ^ a[i])