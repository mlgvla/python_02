# Creating a set
# Creating a set using curly braces
my_set = {1, 2, 3, 4}
print(my_set) 

# Creating a set using the set() constructor
my_set = set([1, 2, 3, 4])
print(my_set)

# Constructor takes an any iterable
my_set = set("mississippi")
print(my_set)

my_set = {1, 2, 3}

# Checking membership
print(1 in my_set) 
print(4 in my_set) 

# Iterating over a set
my_set = {1, 2, 3}
for num in my_set:
    print(num)

# Set Operations
# Set methods examples

# add(): Add an element to the set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)

# remove(): Remove an element from the set 
# (throws an error if not found)
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)

# discard(): Remove an element from the set 
# (does not throw an error if not found)
my_set = {1, 2, 3, 4, 5}
my_set.discard(2)
print(my_set)

# union(): Perform the union of two sets 
# (combines unique elements from both sets)
my_set = {1, 2, 3, 4, 5}
other_set = {4, 5, 6, 7, 8}
union_set = my_set.union(other_set)
print(union_set)

# intersection(): Perform the intersection of two sets
# (elements common to both sets)
my_set = {1, 2, 3, 4, 5}
other_set = {4, 5, 6, 7, 8}
intersection_set = my_set.intersection(other_set)
print(intersection_set)

# difference(): Perform the difference of two sets 
# (elements in the first set but not in the second)
my_set = {1, 2, 3, 4, 5}
other_set = {4, 5, 6, 7, 8}
difference_set = my_set.difference(other_set)
print(difference_set) 

# issubset(): Check if the set is a subset of another set
my_set = {1, 2, 3, 4, 5}
subset = {4, 5, 6}
is_subset = subset.issubset(my_set)
print(is_subset) 

# issuperset(): Check if the set is a superset of another set
my_set = {1, 2, 3, 4, 5}
superset = {1, 4, 5, 6, 7, 8}
is_superset = superset.issuperset(my_set)
print(is_superset)

# Set Comprehension!

# Create a set from a list with duplicates using set comprehension
my_list = [1, 2, 3, 2, 4, 3, 5, 1, 4, 7, 9]
my_set = {x for x in my_list}
print(my_set) 

# Sets cannot be sliced or indexed

my_set = {1, 2, 3}

# Trying to access an element by index
element = my_set[0]  # Raises a TypeError





