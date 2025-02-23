"""
-------------------------------------------------------
[Lab 8 Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_letter_bst, encode_morse, DATA1

bst = BST()

fill_letter_bst(bst, DATA1)

text = "Lab Eight Task Five"
morse = encode_morse(bst, text)

print(f"Original Text: {text}")
print(f"Encoded Morse Code: {morse}")
