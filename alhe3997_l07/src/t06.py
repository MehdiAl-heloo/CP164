"""
-------------------------------------------------------
[Lab 7, Test 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

l = List()
l.append(1)
l.append(2)
l.append(3)

print("Original:")
for i in l:
    print(i)
l.reverse_r()

print("Reversed:")
for j in l:
    print(j)
