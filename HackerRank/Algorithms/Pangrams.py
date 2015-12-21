'''
Problem Statement

Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.

Input Format

Input consists of a string s.

Constraints 
Length of s can be at most 103 (1=|s|=103) and it may contain spaces, lower case and upper case letters. Lower-case and upper-case instances of a letter are considered the same.

Output Format

Output a line containing pangram if s is a pangram, otherwise output not pangram.

Sample Input

Input #1

We promptly judged antique ivory buckles for the next prize    
Input #2

We promptly judged antique ivory buckles for the prize    
Sample Output

Output #1

pangram
Output #2

not pangram
Explanation

In the first test case, the answer is pangram because the sentence contains all the letters of the English alphabet.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
alphabets = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,' ':0}
k = raw_input().lower()
for i in xrange(len(k)):
    alphabets[k[i]] = 1
if(alphabets['a']>0 and alphabets['b']>0 and alphabets['c']>0 and alphabets['d']>0 and alphabets['e']>0 and alphabets['f']>0 and alphabets['g']> 0 and alphabets['h']>0 and alphabets['i']>0 and alphabets['j']>0 and alphabets['k']>0 and alphabets['l']>0 and alphabets['m']>0 and alphabets['n']>0 and alphabets['o']>0 and alphabets['p']>0 and alphabets['q']>0 and alphabets['r']>0 and alphabets['s']>0 and alphabets['t']>0 and alphabets['u']>0 and alphabets['v']>0 and alphabets['w']>0 and alphabets['x']>0 and alphabets['y']>0 and alphabets['z']>0): print 'pangram'
else: print 'not pangram'