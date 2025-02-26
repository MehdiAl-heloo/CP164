"""
-------------------------------------------------------
[Assignment 8, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-17"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

tree = BST()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

print(tree.is_valid())
tree._root._right._value = 4
print(tree.is_valid())

tree2 = BST()
for i in range(1, 7):
    tree2.insert(i)

print(tree.levelorder())
tree.remove(1)
print(tree.levelorder())
