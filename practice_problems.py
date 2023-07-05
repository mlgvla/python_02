"""
Problem 1: Square Numbers
Write a program that takes a list of numbers as input 
and returns a new list containing the squares of those numbers.
"""
numbers = [1, 2, 3, 4, 5]

def square_numbers(numbers):
    return [int**2 for int in numbers]

result = square_numbers(numbers)
print(result)  # Output: [1, 4, 9, 16, 25]


"""
Problem 2: Remove Vowels
Write a program that takes a string as input and 
removes all the vowels from it, returning the modified string.
"""
string = "Hello, World!"

def remove_vowels(string):
    vowels = "aeiou"
    return "".join([char for char in string if char.lower() not in vowels])

result = remove_vowels(string)
print(result)  # Output: "Hll, Wrld!"


"""
Problem 3: Find Common Elements in Lists
Write a program that takes two lists as input and returns a new list 
containing only the common elements between the two lists.
"""
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

def find_common_elements(list1, list2):
    return [element for element in list1 if element in list2]


result = find_common_elements(list1, list2)
print(result)  # Output: [4, 5]


"""
Problem 4: Create a Dictionary from Two Lists
Write a program that takes two lists, one with keys and the other with values, 
and creates a dictionary using those lists.
"""
keys = ["a", "b", "c"]
values = [1, 2, 3]

def create_dictionary(keys, values):
    return {key: value for key, value in zip(keys, values)}

result = create_dictionary(keys, values)
print(result)  # Output: {'a': 1, 'b': 2, 'c': 3}


"""
Problem 5: Filter Even Numbers from a List
Write a program that takes a list of numbers as input and 
returns a new list containing only the even numbers from the original list.
"""
numbers = [1, 2, 3, 4, 5, 6]

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

result = filter_even_numbers(numbers)
print(result)  # Output: [2, 4, 6]


"""
Problem 6: Count Word Frequency in a Sentence
Write a program that takes a sentence as input and returns a dictionary
containing the frequency of each word in the sentence.
"""
sentence = "The cat chased the mouse and the mouse chased its tail."

def count_word_frequency(sentence):
    words = sentence.split()
    return {word: words.count(word) for word in set(words)}

result = count_word_frequency(sentence)
print(result)
# Output: {'The': 1, 'mouse': 2, 'and': 1, 'cat': 1, 'its': 1, 'tail.': 1, 'chased': 2, 'the': 2}


"""
Problem 7: Get the Maximum Value in a Dictionary
Write a program that takes a dictionary as input and 
returns the maximum value in the dictionary.
"""
dictionary = {"a": 10, "b": 5, "c": 15}

def get_maximum_value(dictionary):
    return max(dictionary.values())

result = get_maximum_value(dictionary)
print(result)