'''
Day 15: Linked List!

You are given a class Node in the editor which has one instance pointer next pointing to next node and an integer data to store the data in Node.

You are also given a pointer head pointing to the head node of a linked list and an integer data to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node. The given head pointer may be null, meaning that the initial list is empty.

Code for input/output is already handled in the editor. You have to complete the function insert given in the editor. It takes two arguments: the head node of the linked list and an integer data to be inserted.

Good Luck!

Input Format

First line contains T, the number of testcases. Each test case contains an integer to be inserted at tail of linked list.

Output Format

Output the data in each node separated by space.

Sample Input

4
2
3
4
1
Sample Output

2 3 4 1
Explanation

T=4 
Initially head is null and 2 is inserted. 3,4,1 are inserted at the tail of linked list hence the linked list becomes 2 3 4 1
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

#I used Python 3 for this one instead of Python 2, as the print function in Python 3 can help finish the method in a single line.
    def insert(self,head,data): 
    #Complete this method
        print (data, end=" ") 

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head)