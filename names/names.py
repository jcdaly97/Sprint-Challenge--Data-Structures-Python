import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
tree = BSTNode(names_2[498])
for name in names_2:
    tree.insert(name)

#for name_1 in names_1:
#_______________original_________________(10 seconds)
    #for name_2 in names_2:
    #    if name_1 == name_2:
    #        duplicates.append(name_1)
#______________first_try_________________ (2 seconds)
    #if name_1 in names_2:
    #   duplicates.append(name_1)
#______________BST_______________________(.3 seconds)
    #if tree.contains(name_1):
    #    duplicates.append(name_1)
#______________Stretch____________________
x = set(names_1)
y = set(names_2)
duplicates = x.intersection(y)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
