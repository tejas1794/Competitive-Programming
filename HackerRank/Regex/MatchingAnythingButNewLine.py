'''Problem Statement

dot

The dot (.) matches anything (except for a newline).

ach02.png

In the above image, a Regex Pattern is matched with the Test String.

Note: If you want to match (.) in the test string, you need to escape the dot by using a slash \..
In JavaScript and Java, use \\. instead of \..

Task

You have a test string S. 
Your task is to match the pattern xxx.xxx.xxx.xxx where x denotes any character (other than the newline).

Note

This is a regex only challenge. You are not required to write any code. 
You only have to fill in the regex pattern in the blank (_________).
'''

Regex_Pattern = r"...\....\....\...."	# Do not delete 'r'.
import re
import sys
Test_String = sys.stdin.read()

match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)