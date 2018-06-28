import sys

def three_vowels(string):
    vowel_count = 0

    for char in string:
        if char in 'aeiou':
            vowel_count += 1

    return vowel_count >= 3

def double_letter(string):
    for index, char in enumerate(string[:-1]):
        if char == string[index + 1]:
            return True

    return False

def not_excluded(string):
    exclusions = ['ab', 'cd', 'pq', 'xy']

    for excluded_word in exclusions:
        if excluded_word in string:
            return False

    return True

def is_nice(string):
    return three_vowels(string) and double_letter(string) and not_excluded(string)

nice_list_length = 0

for test_string in sys.stdin:
    if is_nice(test_string):
        nice_list_length += 1

print(nice_list_length)