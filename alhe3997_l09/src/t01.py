"""
-------------------------------------------------------
[Lab 9, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-15"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Hash_Set_array import Hash_Set
from Food import Food

food1 = Food("Lasagna", 7, False, 135)
food2 = Food("Butter Chicken", 2, False, 490)
food3 = Food("Moo Goo Guy Pan", 1, False, 272)
foods = []
foods.append(food1)
foods.append(food2)
foods.append(food3)
hash_table(1, foods)
