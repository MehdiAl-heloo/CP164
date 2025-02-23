"""
-------------------------------------------------------
[Assignment 9, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-23"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

bst = BST()
bst.insert(10)
bst.insert(7)
bst.insert(15)
bst.insert(6)
bst.insert(9)
bst.insert(12)
bst.insert(18)
bst.insert(8)

yes = 7
no = 67

print(bst.node_counts())
print(yes in bst)
print(no in bst)
print(bst.parent(yes))
print(bst.parent_r(yes))
