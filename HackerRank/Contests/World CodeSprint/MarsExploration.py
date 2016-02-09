'''
Sami's spaceship crashed on Mars! She sends n sequential SOS messages to Earth for help.

Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, SS, determine how many letters of Sami's SOS have been changed by radiation.

Input Format

There is one line of input: a single string, SS.

Note: As the original message is just SOS repeated nn times, SS's length will be a multiple of 33.

Constraints 
1=|S|=991=|S|=99
|S| % 3=0|S| % 3=0
SS will contain only uppercase English letters.

Output Format

Print the number of letters in Sami's message that were altered by cosmic radiation.

Sample Input 1

SOSSPSSQSSOR
Sample Output 1

3
Sample Input 2

SOSSOT
Sample Output 2

1
Explanation

Sample 1

SS = SOSSPSSQSSOR, and signal length |S|=12|S|=12. Sami sent 44 SOS messages (i.e.: 12/3=412/3=4).

Expected signal: SOSSOSSOSSOS
Recieved signal: SOSSPSSQSSOR

We print the number of changed letters, which is 33.

Sample 2

SS = SOSSOT, and signal length |S|=6|S|=6. Sami sent 22 SOS messages (i.e.: 6/3=26/3=2).

Expected Signal: SOSSOS 
Received Signal: SOSSOT

We print the number of changed letters, which is 11.

'''


#!/bin/python

import sys

count = 0
S = raw_input().strip()
k = len(S)
c = k/3
if len(S)>3:
    string = "SOS"*(c)
    for i in xrange(len(string)):
        if S[i]!=string[i]: count+=1
    print count
else:
    string = "SOS"
    for i in xrange(len(string)):
        if S[i]!=string[i]: count+=1
    print count 