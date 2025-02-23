"""
-------------------------------------------------------
[Lab 1 Task 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-15"
-------------------------------------------------------
"""
# Imports
from Food_utilities import write_foods
# Constants

file_variable = open("new_foods.txt", "w", encoding="utf-8")

foods = []
new_food = str(input("enter a new food object: "))
while new_food != "":
    foods.append(new_food)
    new_food = str(input("enter a new food object: "))

test6 = write_foods(file_variable, foods)

file_variable.close()

print()
print(test6)
