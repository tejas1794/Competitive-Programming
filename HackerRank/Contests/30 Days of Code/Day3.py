'''
Day 3: If-Else Statements!

This problem will test your knowledge on "if-else" statements.

Given an integer N as input, check the following:

If N is odd, print "Weird".
If N is even and, in between the range of 2 and 5(inclusive), print "Not Weird".
If N is even and, in between the range of 6 and 20(inclusive), print "Weird".
If N is even and N>20, print "Not Weird".
We have given you partially completed code in the editor, complete it to solve the problem.

Input Format

There is a single line of input: integer N.

Constraints 
1=N=100
Output Format

Print "Weird" if the number is weird. Otherwise, print "Not Weird". Do not print the quotation marks.

Sample Input 1

3
Sample Output 1

Weird

Explanation 
N=3, is odd hence the its a Weird Number.

Sample Input 2

24
Sample Output 2

Not Weird

Explanation 
N=24, is >20 hence its not a Weird Number.
'''

#!/bin/python

import sys


N = int(raw_input().strip())
if (N%2!=0) or (N%2==0 and N in xrange(6,21)): print "Weird"
if (N%2==0 and ((N in xrange(2,6)) or N>20)): print "Not Weird"