"""
-------------------------------------------------------
[Lab 6 Task 3]
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
list.append(1)

count = list.count(1)
print("The value '1' appears", count, "times in the list.")

max = list.max()
print("The maximum value in the list is:", max)

min = list.min()
print("The minimum value in the list is:", min)
