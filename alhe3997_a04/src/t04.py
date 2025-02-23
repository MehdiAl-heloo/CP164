"""
-------------------------------------------------------
[Assignment 4 Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

source = Queue()

for i in range(10):
    source.insert(i)

target1, target2 = source.split_alt()

print("Target 1 Queue:")
for value in target1:
    print(value)

print("Target 2 Queue:")
for value in target2:
    print(value)
