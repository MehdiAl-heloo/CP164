"""
-------------------------------------------------------
[Lab 8 Task 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_code_bst, decode_morse, DATA1

bst = BST()

fill_code_bst(bst, DATA1)

morse = "... --- ..."
decoded_text = decode_morse(bst, morse)

print(f"Morse Code: {morse}")
print(f"Decoded Text: {decoded_text}")
