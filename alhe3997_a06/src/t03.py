"""
-------------------------------------------------------
[Assignment 6, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque

deque = Deque()

for i in [1, 2, 3, 4, 5]:
    deque.insert_rear(i)
print("Inserting values at rear of deque:")
for i in deque:
    print(i, end=' ')
print()

for i in [0, -1, -2, -3, -4]:
    deque.insert_front(i)
print("Inserting values at front of deque:")
for i in deque:
    print(i, end=' ')
print()

front_value = deque.remove_front()
rear_value = deque.remove_rear()
print(f"Removed from front: {front_value}")
print(f"Removed from rear: {rear_value}")

front_peek = deque.peek_front()
rear_peek = deque.peek_rear()
print(f"Peek front: {front_peek}, Peek rear: {rear_peek}")

print("Deque is_empty should be False:", deque.is_empty())
print("Length of the deque:", len(deque))

deque2 = Deque()
for value in [-2, -1, 0, 1, 2, 3, 4]:
    deque2.insert_rear(value)

print("Deques equal:", deque == deque2)
