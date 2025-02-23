"""
-------------------------------------------------------
[Lab 1 Task 7]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-15"
-------------------------------------------------------
"""
# Imports
from Food_utilities import get_vegetarian, read_foods
# Constants

file_variable = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file_variable)

test7 = get_vegetarian(foods)

for test in test7:
    print()
    print(test7)
