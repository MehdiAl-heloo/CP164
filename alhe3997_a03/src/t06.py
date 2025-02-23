"""
-------------------------------------------------------
[Assignment 3 Task 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import postfix

tests = ["12 5 -", "4 5 + 12 * 2 3 * -", "1 2 + 3 /"]

for i in tests:
    result = postfix(i)
    print(f"'{i}' = {result}")
