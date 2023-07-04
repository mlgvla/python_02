# Creating a tuple using parentheses
my_tuple = (1, 2, 'three', 4.5)
print(my_tuple) 

# Creating a tuple without parentheses (tuple packing)
my_tuple = 1, 2, 'three', 4.5
print(my_tuple) 

# Accessing Tuple Elements
my_tuple = (1, 2, 'three', 4.5)
print(my_tuple[0])  
print(my_tuple[2]) 

# Tuple unpacking 
# (yes, you can unpack other data structures, as well)
my_tuple = (1, 2, 'three')
a, b, c = my_tuple
print(a)
print(b)
print(c) 

# Concatenating Tuples

# count()
my_tuple = (1, 2, 2, 3, 4, 2)
count = my_tuple.count(2)
print(count)

# len()
my_tuple = (1, 2, 2, 3, 4, 2)
print(len(my_tuple))


# index()
my_tuple = (1, 2, 3, 4, 5)
index = my_tuple.index(3)
print(index)


# Tuples DO'S and DON'TS

# You can slice:
my_tuple = (1, 2, 3, 4, 5)
slice = my_tuple[1:4]
print(slice)
print(my_tuple)

# But you can't change or append

my_tuple = (1, 2, 3)

# Trying to modify a tuple
my_tuple[0] = 4  # Raises a TypeError

# Trying to append to a tuple
my_tuple.append(4)  # Raises an AttributeError





