round_table = ["Arthur", "Lancelot", "Galahad", "Bedevere", "Robin"]

# Create a new list with uppercase names
uppercase_names = []
for name in round_table:
    uppercase_names.append(name.upper())
print(uppercase_names)
print("\n")


# Create a new list with uppercase names
# using a list comprehension
uppercase_names = [name.upper() for name in round_table]

print(uppercase_names)
print("\n")


# Create a new list with names containing more than 6 letters
round_table = ["Arthur", "Lancelot", "Galahad", "Bedevere", "Robin"]

selected_names = []
for name in round_table:
    if len(name) > 6:
        selected_names.append(name)

print(selected_names)
print("\n")


# Create a new list with names containing more than 6 letters
# using a list comprehension
selected_names = [name for name in round_table if len(name) > 6]

print(selected_names)

# Generator Comprehension

round_table = ["Arthur", "Lancelot", "Galahad", "Bedevere", "Robin"]

# Create a generator of reversed names
reversed_names = (name[::-1] for name in round_table)

print(reversed_names)  # what's in reversed names?
print(type(reversed_names))

for name in reversed_names:
    print(name)

# So why use a generator??

import sys

limit = 1000000

# List comprehension
squares_list = [x**2 for x in range(limit)]
list_size = sys.getsizeof(squares_list)

# Generator comprehension
squares_generator = (x**2 for x in range(limit))
generator_size = sys.getsizeof(squares_generator)

print(f"Memory used by list comprehension: {list_size} bytes")
print(f"Memory used by generator comprehension: {generator_size} bytes")

"""
In most cases, you will observe that the memory used by the generator 
comprehension is significantly smaller than the memory used by the list comprehension. 
This difference becomes more noticeable as the limit increases.
"""
