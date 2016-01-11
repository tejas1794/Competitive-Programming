'''
Problem Statement

\d

The expression \d matches any digit [0 - 9].

In the above image, a Regex Pattern is matched with the Test String.

\D

The expression \D matches any character that is not a digit.

In the above image, a Regex Pattern is matched with the Test String.

Task

You have a test string S. Your task is to match the pattern xxXxxXxxxx 
Here x denotes a digit character, and X denotes a non-digit character.

Note

This is a regex only challenge. You are not required to write any code. 
You only have to fill the regex pattern in the blank (_________).
'''

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())