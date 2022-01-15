
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.

def split_half(s):
    length = len(s)
    half = length // 2
    add = 0
    if length % 2:
        add = 1
    left = s[:half + add]
    right = s[half + add:]
    return right + left
str_test_odd = 'aaaaubbbb'
str_test_even = 'aaaabbbb'

print(split_half(str_test_odd))

print(split_half(str_test_even))








