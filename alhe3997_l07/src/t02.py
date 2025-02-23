"""
-------------------------------------------------------
[Lab 7, Test 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

list1 = List()
list2 = List()
list1.append(1)
list2.append(1)

print("Are list1 and list2 identical:", list1.is_identical_r(list2))
