# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

# def unique_char(s):
#     return len(set(s)) == len(s)
#
# test_str_positive = 'abcde'
# test_str_negative = 'aabcde'
#
# print(unique_char(test_str_positive))
#
# print(unique_char(test_str_negative))


def unique_char(s):
    if len(s) == 1:
        return True

    chars = set()
    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True

test_str_positive = 'abcde'
test_str_negative = 'aabcde'

print(unique_char(test_str_positive))

print(unique_char(test_str_negative))
