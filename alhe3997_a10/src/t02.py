"""
-------------------------------------------------------
[Assignment 10, Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-30"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts
from List_linked import List

list = List()
list.append(1)
list.append(25)
list.append(3)
list.append(100)
list.append(250)
list.append(88)
list.append(99)
list.append(20)
list.append(2)
list.append(50)

Sorts.radix_sort(list)

for i in list:
    print(i)
