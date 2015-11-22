'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

#My approach here is to take both version strings, convert them to integer filled arrays so that we may compare them and 
#handle edge cases by going through the extra version pointers.
#Runtime for my algorithm is clearly O(n) as we need to traverse the array multiple times in different loops.

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        #split strings to get the number arrays
        a1 = version1.split(".")
        a2 = version2.split(".")
        #if any element in array 1 or array 2 is different, stop and return accordingly
        for i in xrange(min(len(a1),len(a2))):
            if int(a1[i])>int(a2[i]): return 1
            elif int(a1[i])<int(a2[i]): return -1
        #if no elements are different, calculate if any of the string has higher length and does not have same number count as other (essentially the only edge case in the idea was 1, 1.00.0 which should give 0)
        count1 = 0
        count2 = 0
        for i in xrange(len(a1)):
            count1 += int(a1[i])
        for i in xrange(len(a2)):
            count2 += int(a2[i])
        if len(a1)>len(a2): 
            if count1 != count2 :return 1
            else: return 0
        elif len(a1)<len(a2): 
            if count1 != count2: return -1
            else: return 0
        return 0
        