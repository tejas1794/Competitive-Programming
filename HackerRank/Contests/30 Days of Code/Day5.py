'''
Day 5: Loops!

In this problem you will test your knowledge of loops. Given three integers a, b, and N, output the following series:

a+20b,a+20b+21b,......,a+20b+21b+...+2N-1b
Input Format

The first line will contain the number of testcases T. Each of the next T lines will have three integers, a, b, and N.

Constraints

0=T=500
0=a,b=50
1=N=15
Output Format

Print the answer to each test case in a separate line.

Sample Input

2    
5 3 5
0 2 10
Sample Output

8 14 26 50 98
2 6 14 30 62 126 254 510 1022 2046
Explanation

There are two test cases. 
In the first case: a=5, b=3 ,N=5 
1st term =   5+(20×3)=8 
2nd term = 5+(20×3)+(21×3)=14 
3rd term =  5+(20×3)+(21×3)+(22×3)=26 
4th term =  5+(20×3)+(21×3)+(22×3)+(23×3)=50 
5th term =  5+(20×3)+(21×3)+(22×3)+(23×3)+(24×3)=98
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in xrange(int(raw_input())):
    arr = map(int,raw_input().strip().split())
    a = arr[0]
    b = arr[1]
    n = arr[2]
    start = a
    k = []
    for j in xrange(n):
        start = start+b*(2**(j))
        k.append(start)
    k = map(str,k)
    print " ".join(k)
    