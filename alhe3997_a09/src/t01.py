"""
-------------------------------------------------------
[Assignment 9, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-23"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from functions import insert_words, comparison_total

fn = "otoos610.txt"
fv = open(fn, "r", encoding="utf-8")
hs = Hash_Set(20)

insert_words(fv, hs)
total, max_word = comparison_total(hs)

print("Using array-based list Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(
    max_word.word, max_word.comparisons))
