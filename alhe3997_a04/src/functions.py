"""
-------------------------------------------------------
[Assignment 4 Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
from copy import deepcopy
from Priority_Queue_array import Priority_Queue


def queue_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source queue into separate target queues with values
    alternating into the targets. At finish source queue is empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target1, target2 = queue_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a queue (Queue)
    Returns:
        target1 - contains alternating values from source (Queue)
        target2 - contains other alternating values from source (Queue)
    -------------------------------------------------------
    """
    i = 0
    target1 = Queue(source._capacity)
    target2 = Queue(source._capacity)

    while not source.is_empty():
        if i % 2 == 0:
            target1.insert(deepcopy(source.remove()))
        else:
            target2.insert(deepcopy(source.remove()))
        i += 1

    return target1, target2


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()

    while not source.is_empty():
        i = source.remove()
        if i < key:
            target1.insert(deepcopy(i))
        else:
            target2.insert(deepcopy(i))

    return target1, target2
