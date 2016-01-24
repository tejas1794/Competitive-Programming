import sys
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
	def levelOrder(self,root):
        queue = [root]
        self.bfs(queue) 
    def bfs(self, queue):
        while len(queue) > 0:
            node = queue.pop(0)
            print node.data,
            if (node.left): queue.append(node.left)
            if (node.right): queue.append(node.right)
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)