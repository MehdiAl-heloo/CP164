"""
-------------------------------------------------------
[Assignment 4 Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq.insert(1)
pq.insert(2)
pq.insert(4)
pq.insert(5)

key = 3

higher_priority, lower_or_equal_priority = pq_split_key(pq, key)

print("Key:", key)

print("Target 1 Queue:")
for i in higher_priority:
    print(i)

print("Target 2 Queue:")
for i in lower_or_equal_priority:
    print(i)
