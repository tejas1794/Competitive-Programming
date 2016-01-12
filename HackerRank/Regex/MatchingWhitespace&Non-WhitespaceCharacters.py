'''
Problem Statement

\s

\s matches any whitespace character [ \r\n\t\f ].

In the above image, the Regex Pattern is matched with the Test String.

\S

\S matches any non-white space character.

In above image Regex Pattern is matched with the Test String.

Task

You have a test string S. Your task is to match the pattern XXxXXxXX 
Here, x denotes whitespace characters, and X denotes non-white space characters.

Note

This is a regex only challenge. You are not required to write code. 
You have to fill the regex pattern in the blank (_________).
'''

Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())