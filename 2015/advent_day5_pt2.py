import sys
import re

def contains_pair(string):
    if re.findall(r'[a-z]*([a-z]{2})[a-z]*(\1)', string):
        return True
    else:
        return False

def contains_group(string):
    if re.findall(r'[a-z]*([a-z])[a-z]\1', string):
        return True
    else:
        return False

def is_nice(string):
    return contains_pair(string) and contains_group(string)

nice_list_length = 0

for test_string in sys.stdin:
    if is_nice(test_string):
        nice_list_length += 1

print(nice_list_length)

'''
Credit:
http://stackoverflow.com/questions/4700912/python-regex-not-working
http://stackoverflow.com/questions/17560658/python-how-to-find-consecutive-pairs-of-letters-by-regex
'''