"""
-------------------------------------------------------
[Lab 6 Task 4]
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

found_item = list.find(1)
print("Found item:", found_item)

index = list.index(2)
print("Index of '2':", index)

contains = 3 in list
print("Is '3' in the list:", contains)
