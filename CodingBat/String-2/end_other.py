'''Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string. 

end_other('Hiabc', 'abc') ? True
end_other('AbC', 'HiaBc') ? True
end_other('abc', 'abXabc') ? True
'''

#My Solution:
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if(len(a)<len(b)):
    c = a
    d = b
  else: 
    c = b
    d = a
  return d.endswith(c)
  
#Much Easier Solution
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))