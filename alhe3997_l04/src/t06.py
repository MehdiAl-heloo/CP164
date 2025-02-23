"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list, list_to_array
from List_array import List

llist = List()

source = [1, 2, 3, 4, 5]

array_to_list(llist, source)
print("List after array_to_list:")
for value in llist:
    print(value, end=' ')
print()

target = []
list_to_array(llist, target)
print("Python list after list_to_array:", target)
print("List is empty:", llist.is_empty())
