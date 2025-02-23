"""
-------------------------------------------------------
[Assignment 3 Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

source1 = Stack()
s1 = [1, 2, 3, 4]
for i in s1:
    source1.push(i)

print(f"Stack before: ")
for i in source1:
    print(i)

source1.reverse()

print(f"Stack after: ")
for i in source1:
    print(i)
