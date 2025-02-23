"""
-------------------------------------------------------
[Lab 6 Task 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from List_linked import List

my_list = List()
my_list.append(1)
my_list.append(2)
my_list.append(3)

index_1 = my_list[1]
print("Value at index 1:", index_1)

my_list[1] = 5
print("New item at index 1:", my_list[1])
