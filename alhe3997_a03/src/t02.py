"""
-------------------------------------------------------
[Assignment 3 Task 2]
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
source2 = Stack()
s1 = [8, 12, 8, 5]
for i in s1:
    source1.push(i)
s2 = [14, 9, 7, 1, 6, 3]
for i in s2:
    source2.push(i)
target = Stack()
target.combine(source1, source2)
for i in target:
    print(i)
