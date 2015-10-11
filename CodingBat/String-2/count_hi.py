'''Return the number of times that the string "hi" appears anywhere in the given string. 

count_hi('abc hi ho') ? 1
count_hi('ABChi hi') ? 2
count_hi('hihi') ? 2
'''

def count_hi(str):
  count = 0
  for i in xrange(len(str)):
    if 'h' in str[i-1] and 'i' in str[i]:
     count += 1
  return count