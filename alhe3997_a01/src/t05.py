"""
-------------------------------------------------------
[Assignment 1 Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year
# Constants

year = int(input("Enter a year: "))

leap_year = is_leap_year(year)

print()
print(f"Leap Year: {leap_year}")
