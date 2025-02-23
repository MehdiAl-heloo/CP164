"""
-------------------------------------------------------
[Assignment 4 Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
from Food import Food

q = Queue(2)

f1 = Food("Food1", 1, True, 1)
f2 = Food("Food2", 2, True, 2)
f3 = Food("Food3", 3, False, 3)

print("Check empty should be true:", q.is_empty())
print("Is full should be false:", q.is_full())
q.insert(f1)
print("Inserted f1, peek it:", q.peek())
print("Length:", len(q))
q.insert(f2)
print("Inserted f2, queue should now be full:", q.is_full())
print("It should not be empty:", q.is_empty())
i = q.remove()
print("Removed the front value", i)
q.insert(f3)
for i in q:
    print(i)
