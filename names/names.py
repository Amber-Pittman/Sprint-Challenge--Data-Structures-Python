import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
bst = BSTNode(10000)

# Replace the nested for loops below with your improvements
#runtime: 4.167854309082031 seconds on my machine
# Current runtime = O(n) + O(n) + O(1) + O(1) = O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#runtime: 0.12916326522827148 seconds
# Current runtime = O(n)
for name_1 in names_1:
    name = int("".join(str(ord(char)) for char in name_1))
    bst.insert(name)

for name_2 in names_2:
    name = int("".join(str(ord(char)) for char in name_2))
    if bst.contains(name):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.