"""
-------------------------------------------------------
[Lab 4 Task 7]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import list_test
from List_array import List

llist = []

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

for food in foods:
    llist.append(food)

list_test(llist)
