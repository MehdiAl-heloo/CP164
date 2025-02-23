"""
-------------------------------------------------------
[Assignment 8, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-17"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import fill_letter_bst
from functions import letter_table

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()

fill_letter_bst(bst, DATA1)

letter_table(bst)
