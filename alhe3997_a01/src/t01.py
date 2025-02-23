"""
-------------------------------------------------------
[Assignment 1 Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import clean_list
# Constants

values = [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4,
          3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]
print(f"Before: {values}")

clean_list(values)

print(f"After: {values}")
