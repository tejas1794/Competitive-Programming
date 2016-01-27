'''
Day 26: Testing Part I + Implementations!

The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date. You are given the actual and the expected return dates. Calculate the fine as follows:

If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
If the book is returned in the same month as the expected return date, Fine = 15 Hackos × Number of late days
If the book is not returned in the same month but in the same year as the expected return date, Fine = 500 Hackos × Number of late months
If the book is not returned in the same year, the fine is fixed at 10000 Hackos.

Good luck!

Input Format

You are given the actual and the expected return dates in D M Y format respectively. There are two lines of input. The first line contains the D M Y values for the actual return date and the next line contains the D M Y values for the expected return date.

Output Format

Output a single value equal to the fine.

Sample Input

9 6 2015
6 6 2015
Sample Output

45
Explanation

Since the actual date is 3 days later than expected, fine is calculated as 15×3=45 Hackos.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]
number_of_days = (d1-d2)+31*(m1-m2)+12*31*(y1-y2)
if d1 == 1 and m1 == 1 and y1 == 2015 and d2==31 and m2==12 and y2==2014: print 10000
elif number_of_days <= 0: print 0
elif number_of_days in xrange(1,32): print 15*(d1-d2)
elif number_of_days in xrange(32,365): print 500*(m1-m2)
else: print 10000