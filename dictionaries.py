# Empty dictionary
my_dict = {}

# Dictionary with initial values

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values using keys
print(my_dict['name'])
print(my_dict['age'])


# Modifying values using keys
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['age'] = 31
print(my_dict)


# Adding a new key-value pair
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['country'] = 'USA'
print(my_dict)

# Removing a key-value pair
del my_dict['age']
print(my_dict)


# Dictionary Methods

# keys() - Returns a view object that contains all the keys in the dictionary.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
print(keys)

# values() - Returns a view object that contains all the values in the dictionary.
values = my_dict.values()
print(values)

# items() - Returns a view object that contains tuples of key-value pairs in the dictionary.
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# get(key, default) - Returns the value associated with the given key. 
# If the key is not found, it returns the specified default value.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
age = my_dict.get('age', 0)
print(age)  # Output: 30
occupation = my_dict.get('occupation', 'N/A')
print(occupation)  # Output: N/A

# pop(key, default) - Removes the key-value pair associated with the given key and returns its value.
# If the key is not found, it returns the specified default value.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
age = my_dict.pop('age', 0)
print(age)  # Output: 30
occupation = my_dict.pop('occupation', 'N/A')
print(occupation)  # Output: N/A

# update(other_dict) - Updates the dictionary with the key-value pairs from another dictionary.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
other_dict = {'occupation': 'Engineer', 'country': 'USA'}
my_dict.update(other_dict)
print(my_dict) 

# zip() - combine elements from multiple iterables into tuples.
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
result = zip(numbers, letters)
print(list(result))


# Difference between accessing values with key vs. get()
my_dict = {'name': 'John', 'age': 30}
occupation = my_dict['occupation']  # Raises KeyError: 'occupation'

my_dict = {'name': 'John', 'age': 30}
occupation = my_dict.get('occupation', 'N/A')
print(occupation)  # Output: N/A

# Checking if a key exists
print('name' in my_dict)

# Getting the number of key-value pairs
size = len(my_dict)
print(size)

# Looping through a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Looping through the dictionary using items()
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# There is even such a thing as a dictionary comprehension!
squares = {x: x**2 for x in range(1, 6)}
print(squares)



