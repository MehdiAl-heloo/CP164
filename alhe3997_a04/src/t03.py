"""
-------------------------------------------------------
[Assignment 4 Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
from functions import queue_split_alt

source = Queue()
source_contain = Queue()

for i in range(10):
    source.insert(i)

target1, target2 = queue_split_alt(source)

assert source.is_empty(), "Source queue should be empty after split."

print("Target1 contains:")
while not target1.is_empty():
    print(target1.remove())

print("Target2 contains:")
while not target2.is_empty():
    print(target2.remove())
