"""
-------------------------------------------------------
[Lab 8 Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from morse import ByCode

A = ByCode('.-', 'A')
B = ByCode('-...', 'B')
C = ByCode('-.-.', 'C')

print(f"A and B equal: {A == B}")
print(f"A and A equal: {A == A}")
print(f"A < B: {A < B}")
print(f"B < B: {B < B}")
print(f"B <= C: {B <= C}")
