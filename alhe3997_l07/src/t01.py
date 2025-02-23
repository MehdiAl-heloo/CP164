"""
-------------------------------------------------------
[Lab 7, Test 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

list = List()
list.append(1)
list.append(3)

previous, current, index = list._linear_search_r(3)
print("Recursively in List there is a 3 found at index:", index)
