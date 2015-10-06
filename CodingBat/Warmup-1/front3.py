'''
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front. 

front3('Java') ? 'JavJavJav'
front3('Chocolate') ? 'ChoChoCho'
front3('abc') ? 'abcabcabc'
'''

def front3(str):
  str = list(str)
  if len(str)>2: 
    str1 = str[0:3]
    str1 += str1
    str1 += str1[0:3]
  if len(str)<3:
    temp = str[0:len(str)]
    str1 = str
    str1+=str1
    str1+=temp
  str1 = "".join(str1)
  return str1