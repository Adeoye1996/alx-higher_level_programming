#!/usr/bin/python3
# Iterate through ASCII values for lowercase letters and print them without newlines
for char_code in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(char_code), end='')
