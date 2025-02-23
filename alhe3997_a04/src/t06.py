"""
-------------------------------------------------------
[Assignment 4 Task 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
for value in [1, 2, 4, 5]:
    pq.insert(value)

key = 3

print("key", key)

higher_than_key, lower_or_equal_to_key = pq.split_key(key)

print("Priority Queue with values higher than key:")
for value in higher_than_key:
    print(value)

print("Priority Queue with values lower than or equal to key:")
for value in lower_or_equal_to_key:
    print(value)
