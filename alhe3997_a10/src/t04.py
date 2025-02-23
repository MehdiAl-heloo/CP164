"""
-------------------------------------------------------
[Assignment 10, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-30"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
a.insert_rear(1)
a.insert_rear(25)
a.insert_rear(3)
a.insert_rear(100)
a.insert_rear(250)
a.insert_rear(88)
a.insert_rear(99)
a.insert_rear(20)
a.insert_rear(2)
a.insert_rear(5)
Sorts.gnome_sort(a)

for i in a:
    print(i)
