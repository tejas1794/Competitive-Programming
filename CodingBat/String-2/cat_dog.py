'''Return True if the string "cat" and "dog" appear the same number of times in the given string. 

cat_dog('catdog') ? True
cat_dog('catcat') ? False
cat_dog('1cat1cadodog') ? True
'''

def cat_dog(str):
  countd = 0
  countc=0
  for i in xrange(len(str)-2):
    if str[i] == 'c' and str[i+1]=='a' and str[i+2]=='t': countc+=1
    elif str[i] == 'd' and str[i+1]=='o' and str[i+2]=='g': countd+=1
  return (countc==countd)