"""
-------------------------------------------------------
[Assignment 3 Task 7]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_maze

maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': ['D'], 'C': [
    'D', 'E'], 'D': [], 'E': ['F', 'X'], 'F': ['G'], 'G': ['C']}

print("Maze:")
print(maze)
print()
print("Maze Solution:")
print(stack_maze(maze))
