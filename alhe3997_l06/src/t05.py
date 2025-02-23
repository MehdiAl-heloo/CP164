"""
-------------------------------------------------------
[Lab 6 Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from List_linked import List

list = List()
list.append(1)
list.append(2)
list.append(3)
list.append(4)

first = list.peek()
print("Peek:", first)

removed = list.remove(2)
print("Removed item:", removed)
