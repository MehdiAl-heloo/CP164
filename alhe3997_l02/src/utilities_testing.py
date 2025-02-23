"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_foods
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array, stack_test


fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
stack_test(foods)
fv.close()
