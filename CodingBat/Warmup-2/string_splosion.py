'''
Given a non-empty string like "Code" return a string like "CCoCodCode". 

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def string_splosion(str):
  str = list(str)
  str1 = []
  for i in xrange(0,len(str)+1):
    str1+=str[0:i]
  str1 = "".join(str1)
  return str1


