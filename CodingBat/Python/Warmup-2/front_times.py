'''
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front; 

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''

def front_times(str, n):
  str = list(str)
  str1 = []
  
  for i in xrange(0,n):
    if len(str)<3: str1 += str[0:len(str)]
    else: str1 += str[0:3]
  
  str1 = "".join(str1)
  return str1