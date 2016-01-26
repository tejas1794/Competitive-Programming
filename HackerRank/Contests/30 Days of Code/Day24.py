'''
Day 24: More Review + More Linked Lists!

You're given the pointer head pointing to the head node of a linked list, where the data in the nodes is in non decreasing order. Delete as few nodes as possible so that the list does not contain any value more than once. The given head pointer may be null indicating that the list is empty. Adjust the next pointers to ensure that the remaining nodes form a single sorted linked list

The code for handling input/output is already given in the editor. You have to complete the function removeDuplicates given in the editor which takes one argument - the head of the linked list .

Good luck!

Input Format

First line contains T, the number of testcases. Each test case contains an integer data to be inserted at tail of linked list. 
Note: The input data for each test case is always given in non-decreasing order.

Output Format

Print the data in each node of linked list separated by a space after the deletion of duplicates as given in problem statement.

Sample Input

6
1
2
2
3
3
4
Sample Output

1 2 3 4 
Explanation

T = 6 
2 and 3 are repeated so after deleting the nodes with repeated values the linked list becomes

1 2 3 4
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head 
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next	
	def removeDuplicates(self, head):
        if not head: return head
        tmp = head
        while tmp:
            nextnode = tmp.next
            while (nextnode and nextnode.data == tmp.data):
                nextnode = nextnode.next
            tmp.next = nextnode
            tmp = nextnode
        return head
	
	
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)   
head=mylist.removeDuplicates(head)
mylist.display(head);