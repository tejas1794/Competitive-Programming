'''
Given a string and a non-negative int n, return a larger string that is n copies of the original string. 

string_times('Hi', 2) ? 'HiHi'
string_times('Hi', 3) ? 'HiHiHi'
string_times('Hi', 1) ? 'Hi'
'''

def string_times(str, n):
  str = list(str)
  str1 = []
  for i in xrange(0,n):
    str1+=str[0:len(str)]
  str1 =   "".join(str1)
  return str1
