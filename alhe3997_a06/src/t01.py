"""
-------------------------------------------------------
[Assignment 6, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue
# Constants

queue = Queue()

empty = queue.is_empty()
print(f"Queue should be empty:  {empty}")

print("Inserting into Queue:")

for i in range(5):
    queue.insert(i)
    print(f"Inserting {i} into queue")

empty = queue.is_empty()
print(f"Is_empty should be false now: {empty}")

len = len(queue)
print(f"Length of queue now: {len}")

peek = queue.peek()
print(f"Peeking queue, front value: {peek}")

remove = queue.remove()
print(f"Removing front value, value removed: {remove}")

q1 = Queue()
empty = q1.is_empty()
print(f"New queue, q1 should be empty: {empty}")

q1._move_front_to_rear(queue)
print(f"Moved front node from queue to rear of q1, q1 rear value: ")
print(q1._rear._value)

q1._append_queue(queue)
print(f"Appending the rest of queue to q1")
print(f"q1 now: ")
while not q1.is_empty():
    print(q1.remove(), end=" ")
print()

q2 = Queue()

for i in range(5):
    if i % 2 == 0:
        q1.insert(i)
    else:
        q2.insert(i)
print("Combining two queues (q1 and q2) into 'queue'.")
queue.combine(q1, q2)
print("Final combined queue (should alternate between q1 and q2 elements):")
while not queue.is_empty():
    print(queue.remove(), end=" ")
print()


print("Splitting the combined queue back into two queues:")
queue.insert(0)
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
q1, q2 = queue.split_alt()
print("Contents of q1:")
while not q1.is_empty():
    print(q1.remove(), end=" ")
print("\nContents of q2:")
while not q2.is_empty():
    print(q2.remove(), end=" ")
print()

print("Checking equality of two queues:")
for i in range(3):
    q1.insert(i)
    q2.insert(i)
print(f"Are q1 and q2 equal? {q1 == q2}")
q2.insert(4)
print(f"Are q1 and q2 equal after modifying q2? {q1 == q2}")
