"""
-------------------------------------------------------
[Assignment 1 Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants

file = "task4.txt"
fv = open(file, "r", encoding="utf-8")
upp, low, dig, whi, rem = file_analyze(fv)
print("uppers: ", upp)
print("lowers: ", low)
print("digits: ", dig)
print("whitespace: ", whi)
print("other: ", rem)
fv.close()
