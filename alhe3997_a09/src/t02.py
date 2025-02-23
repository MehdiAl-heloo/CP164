"""
-------------------------------------------------------
[Assignment 9, Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-23"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_sorted import Hash_Set

fv = open('otoos610.txt', 'r')
hash_set = Hash_Set(20)

insert_words(fv, hash_set)
total, max_word = comparison_total(hash_set)

print("Using sorted-based list Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(
    max_word.word, max_word.comparisons))
