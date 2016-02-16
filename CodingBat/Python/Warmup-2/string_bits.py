'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo". 

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''

def string_bits(str):
  str = list(str)
  str1 = []
  for i in xrange(0,len(str),2):
    str1 += str[i]
  str1 = "".join(str1)
  return str1 

