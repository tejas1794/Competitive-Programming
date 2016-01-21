'''
Day 18: Queues & Stacks!

To solve this challenge, we must first take each character in s, enqueue it in a queue, and also push it onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means s isn't a palindrome).

Write the following four functions/methods in class Palindrome:

void pushCharacter(char ch): Pushes a character onto a stack.
void enqueueCharacter(char ch): Enqueues a character in a queue.
char popCharacter(): Pops and returns the top character.
char dequeueCharacter(): Dequeues and returns the first character.
Code handling Input/Output and determining if s is palindrome is provided in the editor.

Input Format

A single line containing string s.

Note: s will always be lowercase.

Output Format

If s is a palindrome, print "The word, s, is a palindrome." 
Otherwise, print "The word, s, is not a palindrome." without quotes

Sample Input

racecar
Sample Output

The word, racecar, is a palindrome.
'''

import sys

class Palindrome:
    #Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []
    def pushCharacter(self,ch):
        self.stack.insert(0,ch)
    def enqueueCharacter(self,ch):
        self.queue.append(ch)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop()

# read the string s
s=raw_input()
#Create the Palindrome class object
p=Palindrome()   

l=len(s)
# push all the characters of string s to stack
for i in range(l):
    p.pushCharacter(s[i])
#enqueue all the characters of string s to queue
for i in range(l):
    p.enqueueCharacter(s[i])
f=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l):
    if p.popCharacter()!=p.dequeueCharacter():
        f=False
        break
#finally print whether string s is palindrome or not.
if f:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")   