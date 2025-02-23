"""
-------------------------------------------------------
[Lab 7, Test 5]
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
list3 = List()

list2.append(0)
list2.append(1)
list2.append(2)
list2.append(3)

list3.append(2)
list3.append(3)
list3.append(4)
list3.append(5)

list1.union(list2, list3)

print("List2:")
for i in list2:
    print(i)

print("List3:")
for i in list3:
    print(i)

print("Union List of List2 and List3:")
for i in list1:
    print(i)
