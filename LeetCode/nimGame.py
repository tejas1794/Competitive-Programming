'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
'''
#Approach: This isn't much of a programming problem. The main idea is to understand the logic behind the problem. 
#Clearly, if number of stones is upto 3, I will win as I can take all the stone in our first turn. 
#I can't win the game if the number of stones is 4 as the opponent can pick the rest up in a single go regardless of what I pick.
#Following this pattern, we can determine the general idea which is written below in code.
#Runtime is clearly O(1).

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<3: return True
        else: return (not (n%4 == 0))