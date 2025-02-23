"""
-------------------------------------------------------
[Lab 6 Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
# Imports
from List_linked import List

list = List()
list.append(1)
list.append(2)
list.append(3)
list.append(4)

previous, current, index = list._linear_search(3)

print("Previous Node from Key value:", previous._value if previous else None)
print("Current Node with Key value:", current._value if current else None)
print("Index of Node with Value key:", index)
