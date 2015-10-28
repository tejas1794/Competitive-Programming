'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done. 

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''
#Now this was a problem which is pretty tricky as there is an edge case not clearly visible unless some examples are compared
def make_chocolate(small, big, goal):
  if not make_bricks(small,big,goal): return -1
  else: 
    if((goal-(big*5))<0): return ((goal-(big*5))%5) #when number of big chocolates > desired goal requirements (5*big > goal), our substraction yields negative results. Simply modulo 5 of that number gives us the positive variant of small chocolates required. This can also be attained by absoluting the number and adding small to it, but that yields another edge case for very large number of big chocolates.
    else: return goal - (big*5)

#Reusing the check from make_bricks  
def make_bricks(small, big, goal):
  return not((goal > (big*5) + small) or goal%5>small)