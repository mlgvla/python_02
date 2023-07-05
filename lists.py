# List methods examples with strings
my_list = ["rabbit", "swallow", "møøse", "parrot"]
print(my_list)

# append(): Add an element to the end of the list
my_list.append("python")
print(my_list)

# extend(): Add elements from another list to the end
my_list.extend(["camel", "koala"])
print(my_list)

# insert(): Insert an element at a specific index
my_list.insert(2, "penguin")
print(my_list)

# remove(): Remove the first occurrence of an element
my_list.remove("møøse")
print(my_list)

# pop(): Remove and return an element at a specific index
popped_element = my_list.pop(4)
print(popped_element)
print(my_list)


my_list = ["rabbit", "swallow", "penguin", "parrot", "camel", "koala"]

# len(): Get the length of the list
length = len(my_list)
print(length)

# index(): Find the index of the first occurrence of an element
index = my_list.index("parrot")
print(index)

# count(): Count the occurrences of an element in the list
count = my_list.count("swallow")
print(count)

my_list = ["rabbit", "swallow", "penguin", "parrot", "camel", "koala"]

# sort(): Sort the list in ascending order
my_list.sort()
print(my_list)

# Using sorted() function to sort the list in ascending order
my_list = ["rabbit", "swallow", "penguin", "parrot", "camel", "koala"]

sorted_list = sorted(my_list)
print(sorted_list)
print(my_list)

my_list = ["rabbit", "swallow", "penguin", "parrot", "camel", "koala"]

# reverse(): Reverse the elements in the list
my_list.reverse()
print(my_list)


# Using reversed() function to reverse the list
my_list = ["rabbit", "swallow", "penguin", "parrot", "camel", "koala"]

reversed_list = list(reversed(my_list))
print(reversed_list)
print(my_list)

# Reversing the list with slicing
my_list = ["rabbit", "swallow", "penguin", "parrot", "camel", "koala"]

print(my_list)
reversed_list_slice = my_list[::-1]
print(reversed_list_slice)

# copy(): Returns a shallow copy of the list.
copy_list = my_list.copy()
print(copy_list)

# copy a list using slicing
copy_list = my_list[:]
print(copy_list)

# clear(): Remove all elements from the list
my_list.clear()
print(my_list)

numbers = [1, 3, 2, 7, 9, 8, -2]

# max(): Returns the maximum element in the list.
max_element = max(numbers)
print(max_element)

# min(): Returns the minimum element in the list.
min_element = min(numbers)
print(min_element)

# Slicing lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic slicing
sliced_list = numbers[2:7]
print(sliced_list)

# Slicing with a step of 2 to extract alternate element
alternate_elements = numbers[::2]
print(alternate_elements)

# Reverse a list using slicing with a step of -1:
reversed_list = numbers[::-1]
print(reversed_list)


# Differences between append and extend lists:
a1 = [1, 2]
a2 = [1, 2]
# b = (3, 4)  # tuple
b = "cat"

# a1 = [1, 2, 3, 4]
a1.extend(b)
print(a1)

# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)
