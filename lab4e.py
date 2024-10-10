#!/usr/bin/env python3
# Author ID: jsingh1101

def is_digits(sobj):
    for char in sobj:  # Loop through each character in the string
        if not char.isdigit():  # Check if the character is not a digit
            return False  # Return False if any character is not a digit
    return True  # Return True if all characters are digits

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
