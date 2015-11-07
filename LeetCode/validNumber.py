'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
'''
#Approach: I'm trying not to reinvent the wheel here. Python already has a built-in function which does this for us! I'm assuming its very fast too :)
#This does work, and grabbed me best runtime amongst all other submissions.

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        
        try:
            float(s)
        except ValueError:
            return False
        else: 
            return True