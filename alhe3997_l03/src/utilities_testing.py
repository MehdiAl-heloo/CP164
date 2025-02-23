"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports

from utilities import priority_queue_test
from Food_utilities import read_foods

fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
priority_queue_test(foods)
