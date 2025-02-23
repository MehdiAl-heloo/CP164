"""
-------------------------------------------------------
[Assignment 4 Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

queue1 = Queue()
queue2 = Queue()
queue3 = Queue()

for i in [1, 2, 3, 4, 5]:
    queue1.insert(i)
    queue2.insert(i)

for i in [1, 2]:
    queue3.insert(i)

if queue1.__eq__(queue2):
    print("queue1 and queue2 are equal.")
else:
    print("queue1 and queue2 are not equal.")


if queue1.__eq__(queue3):
    print("queue1 and queue3 are equal.")
else:
    print("queue1 and queue3 are not equal.")
