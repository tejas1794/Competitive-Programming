'''
Given a number n, return True if n is in the range 1..10, inclusive. Unless "outsideMode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10. 

in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True
'''

def in1to10(n, outside_mode):
  return ((n in range(1,11) and not outside_mode) or (n not in range(2,10) and outside_mode))

