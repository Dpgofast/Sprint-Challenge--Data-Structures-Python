import time
from bin_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# ANSWER 🔻
# This Solution would be O(n^2) I believe.
# Nested for loops are inefficient

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Plant some trees and glue the leaves on!
# place holder for any duplicates we find
duplicates = []

# seed a tree with first name in list 1
tr = BinarySearchTree(names_1[0])
# loop through rest of names and insert into tree
# skipping the first name since we used it to seed
for name in names_1[1:]:
    tr.insert(name)

# Now we can check through list 2 and compare to list one
# Since list one is now searchable as a tree it should be more efficient
for name in names_2:
    if tr.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach
# to this problem
# What's the best time you can accomplish with no restrictions on techniques
#  or data
# structures?
