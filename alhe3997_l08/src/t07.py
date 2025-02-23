"""
-------------------------------------------------------
[Lab 8 Task 7]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports

"""
DATA1 Tree:

A
 \
  B
   \
    C
     \
      ...
       \
        Z


DATA2 Tree:
       M
      / \
    C     T
   / \   / \
  B   F J   W
 / \ / \ / \ / \
A  D E G I K O Q
               / \
              N   S
                 / \
                P   R
                   / \
                  L   U
                       \
                        V
                         \
                          X
                           \
                            Y
                             \
                              Z

DATA3 Tree:
 E
  \
   T
    \
     A
      \
       O
        \
         I
          \
           N
            \
             S
              \
               ...
                 \
                  Z
"""

# DATA1 is the most inefficient BST, since its height is the total amount of elements. It is pretty much a linked list

# Although not perfectly balanced, Data2 distributes its elements and spreads them more evenly apart from below 'Q' making it the most efficient whereas the other two are like a linear branch or linked list

# To figure out which is most efficient, calculate the height of each datasets BST and the BST with the lowest height, closest to the theoretical minimum height, which is log2(n) where n is the number of nodes, would be the most efficient

#
