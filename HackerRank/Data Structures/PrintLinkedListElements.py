'''
Problem Statement

If you are new to working with linked lists, then this is a great exercise to get familiar with them. You are given the pointer to the head node of a linked list. You need to print all its elements in order, one element per line. The head pointer may be null, i.e. it may be an empty list. In that case, don’t print anything!

Input Format 
You have to complete the void Print(Node* head) method which takes one argument: the head of the linked list. You should not read any input from stdin/console. The struct Node has a data part which stores the data and a next pointer which points to the next element of the linked list. There are multiple test cases. For each test case, this method will be called individually.

Output Format 
Print the elements of the linked list to stdout/console (using printf or cout). Print one per line.

Sample Input

NULL  
1->2->3->NULL
Sample Output

1
2
3
Explanation

For the first case, an empty list is passed to the method. So, nothing is printed. For the second case, all the elements of the linked list (1, 2 and 3) are printed on separate lines.
'''

"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 
"""
def print_list(head):
    while head!=None:
        print head.data
        head = head.next
  