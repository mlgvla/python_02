#range(start, stop, step)

# Using range with stop value
numbers = range(5)
print(numbers)
print(type(numbers)) # range object
print(list(numbers)) # must type cast to see the range object as a list

# Using range in a for loop
for i in range(5):
    print(i)

# Counting backwards with range()
for i in range(10, 0, -1):
    print(i)

