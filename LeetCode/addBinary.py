'''
'''
#My approach here is pretty self-explanatory. I'm using built-in int converter function with argument mentioning the string is binary.
#I continue by adding the two integers and converting the result to binary. I finally return the spliced string to make sure the final
#solution does not show 0b (binary flag from Python).
#Runtime is pretty clearly whatever time it takes for Python to convert strings to int. Thus the complexity is O(1) + O(complexity of int())
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b,2)
        c = a+b
        c = bin(c)
        return str(c)[2:]