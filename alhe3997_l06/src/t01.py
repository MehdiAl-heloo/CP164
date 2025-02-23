"""
-------------------------------------------------------
[Lab 6 Task 1]
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

list.prepend("Front")
list.append("Rear")
list.insert(1, "Middle")

for i in list:
    print(i)
