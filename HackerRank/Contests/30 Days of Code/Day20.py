'''
Day 20: Review + More String Methods!

Given a string S, find number of words in that string. For this problem a word is defined by a string of one or more English letters.

Note: Space or any of the special characters like ![,?.\_'@+] will act as a delimiter.

Input Format
The string will only contain lower case english alphabets, upper case english alphabets, blank spaces and this special characters: ![,?.\_'@+].

Constraints 
1=|S|=400000

Output Format
In the first line, print number of words in the string. The words don't need to be unique. Also print each word in a separate line.

Sample Input

He is a very very good boy, isn't he?
Sample Output

10
He
is
a
very
very
good
boy
isn
t
he
'''


import re
result = re.split("[ !\[,?.\\\\_'@+\]]", raw_input())
result = filter(None, result)
print len(result)
print "\n".join(result)