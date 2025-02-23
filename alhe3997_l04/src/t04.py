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
from List_array import List

list = List()

list.append(1)
list.append(2)
list.append(3)
list.append(1)
list.append(2)

print("List:")
for i in list:
    print(i)

index_of_2 = list.index(2)
print(f"The index of the first occurrence of '2': {index_of_2}")

found_value = list.find(3)
print(f"The value found for '3': {found_value}")

contains_2 = 2 in list
print(f"Is '2' in the list? {contains_2}")

count_of_1 = list.count(1)
print(f"The count of '1' in the list: {count_of_1}")

max_value = list.max()
print(f"Max value in the list: {max_value}")

min_value = list.min()
print(f"Min value in the list: {min_value}")
