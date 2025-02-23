"""
-------------------------------------------------------
[Lab 5 Task 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-09"
-------------------------------------------------------
"""
# Imports
from functions import bag_to_set
# Constants

bag = [4, 5, 3, 4, 5, 2, 2, 4]

print(f"Old list: {bag}")

new_set = bag_to_set(bag)

print(f"New list: {new_set}")
