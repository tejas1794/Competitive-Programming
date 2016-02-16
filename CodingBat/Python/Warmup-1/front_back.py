'''Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') ? 'eodc'
front_back('a') ? 'a'
front_back('ab') ? 'ba'
'''

def front_back(str):
  str = list(str)
  if len(str) > 0:
    char = str[0]
    str[0] = str[-1]
    str[-1] = char
  str = "".join(str)
  return str