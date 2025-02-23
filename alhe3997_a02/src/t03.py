"""
-------------------------------------------------------
[Assignment 2 Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import calories_by_origin

food1 = Food("Orange Chicken", 1, False, 800)
food2 = Food("Spring Rolls", 1, True, 200)
food3 = Food("Teppanyaki", 6, False, 200)

foods = [food1, food2, food3]

by_origin = calories_by_origin(foods, 1)

print(by_origin)
