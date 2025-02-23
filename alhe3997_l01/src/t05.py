"""
-------------------------------------------------------
[Lab 1 Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-15"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
# Constants

file_variable = open("foods.txt", "r", encoding="utf-8")

test5 = read_foods(file_variable)

file_variable.close()

for test in test5:
    print()
    print(test5)
