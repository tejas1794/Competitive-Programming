'''
Day 29: Look at Everything We've Learned!

Suppose you have some string S having length N that is indexed from 0 to N-1. You also have some string R that is the reverse of string S. S is funny if the condition |Si-Si-1|=|Ri-Ri-1| is true for every i from 1 to N-1.

Note: For some string str, stri denotes the ASCII value of the ith 0-indexed character in str. The absolute value of some integer, x, is written as |x|.

Input Format

The first line contains an integer, T (the number of test cases). 
The T subsequent lines each contain one string S.

Constraints 
1=T=10 
2=length of S=10000
Output Format

For each string S, print whether it is Funny or Not Funny on a new line (i.e.: the ith line of output should be the answer for input string Si).

Sample Input

2
acxz
bcxz
Sample Output

Funny
Not Funny
Explanation

Test Case 0: S= "acxz" 
|c-a|=2=|x-z| 
|x-c|=21=|c-x| 
|z-x|=2=|a-c| 
We print Funny.

Test Case 1: S= "bcxz" 
|c-b|=1, but |x-z|=2 
We stop evaluating the string (as |c-b|?|x-z|), and print Not Funny.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in xrange(int(raw_input())):
    alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    arr = list(raw_input().strip())
    rev = arr[::-1]
    count = 0
    for j in xrange(len(arr)-1,-1,-1):
        if abs(alpha[arr[j]]-alpha[arr[j-1]])==abs(alpha[rev[j]]-alpha[rev[j-1]]): count +=1
    if (count==len(arr)): print "Funny"    
    else: print "Not Funny"
