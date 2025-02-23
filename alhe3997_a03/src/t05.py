"""
-------------------------------------------------------
[Assignment 3 Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import is_palindrome_stack

palindromes = ["racecar", "Otto", "Able was I ere I saw Elba",
               "A man, a plan, a canal, Panama!", "This is not a palindrome"]

for i in palindromes:
    result = is_palindrome_stack(i)
    print(f"'{i}' is a palindrome: {result}")
