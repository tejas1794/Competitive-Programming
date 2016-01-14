'''
Day 6: Let's Review!

Your teacher has given you the task of drawing a staircase structure. Being an expert programmer, you decided to make a program to draw it for you instead. Given the required height, can you print a staircase as shown in the example? 
Note: The last line has zero spaces before it.

Good luck!

Constraints 
1=N=100
Input Format

You are given an integer N depicting the height of the staircase.

Output Format

Print a staircase of height N that consists of # symbols and spaces as given in Sample Output.

Sample Input

6

Sample Output

     #
    ##
   ###
  ####
 #####
######
'''

#!/bin/python

import sys


n = int(raw_input().strip())
for i in xrange(1,n+1):
    for j in xrange(n-i):
        sys.stdout.write(' ')
    for k in xrange(i):
        sys.stdout.write('#')
    sys.stdout.write('\n')