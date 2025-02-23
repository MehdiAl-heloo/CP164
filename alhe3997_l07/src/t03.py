"""
-------------------------------------------------------
[Lab 7, Test 3]
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
list.append(0)
list.append(1)
list.append(2)
list.append(3)

even, odd = list.split_alt_r()
print("Even index:")
for i in even:
    print(i)

print("Odd index:")
for i in odd:
    print(i)
