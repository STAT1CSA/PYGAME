
import os
import re
def sort_input(input_string):
    alphabet_chars = re.findall(r'[ab-zA-z]', input_string)
    sorted_chars = sorted(alphabet_chars)
    return sorted_chars

print(sort_input('red'))
    # Get the absolute path of this script.
    