#  discuss string slicing and provide example
''' ans:

String slicing in Python is a powerful feature that allows you to extract a substring from a string by specifying a start index, an end index, and an optional step. It provides a way to get a portion of the string or manipulate it in various ways.


#  syntax of string slicing :   substring = string[start:end:step]'''
#   example :
text = "Hello, World!"
substring = text[0:5]
print(substring)


#  explain the key feature of list in python
'''
ans:
Lists are one of the most versatile and commonly used data structures in Python. 
They are ordered collections that can hold items of any type, including other lists.
 Here are some key features of lists in Python:
 1. Ordered
 Lists maintain the order of elements. The order in which elements are added to the list is preserved.
2 Mutable: Lists are mutable, meaning you can change their content after they are created. You can add, remove, or modify elements in a list.

3.Dynamic Size: Lists can grow and shrink in size as needed. You can add new items using methods like append() and remove items using methods like remove() or pop().

4.Heterogeneous: Lists can hold items of different data types. For example, a list can contain integers, strings, other lists, or any other type of object.

5.Nested: Lists can contain other lists as their elements, allowing for the creation of complex, multi-dimensional data structures.

6.Indexing and Slicing: You can access individual items or a range of items in a list using indexing and slicing. For instance, my_list[0] accesses the first item, and my_list[1:3] accesses a sub-list from index 1 up to (but not including) index 3.
 
 
 
 
 
 
 
 
 '''



#  describe how to access , modify and delete the element from a list with example



'''1. Accessing Elements
To access elements in a list, you use indexing. Python lists are zero-indexed, meaning the first element has an index of 0.'''
my_list = [10, 20, 30, 40, 50]


print(my_list[0])


print(my_list[2])


print(my_list[-1])

"""2. Modifying Elements
You can modify elements in a list by assigning a new value to a specific index.
"""
my_list = [10, 20, 30, 40, 50]


my_list[1] = 99
print(my_list)
my_list[-1] = 100
print(my_list)
'''
3. Deleting Elements
You can delete elements from a list using several methods:

del keyword: Deletes an element at a specified index.
remove() method: Removes the first occurrence of a specific value.
pop() method: Removes and returns an element at a specified index (or the last element if no index is specified)'''
my_list = [10, 20, 30, 40, 50]

del my_list[2]
print(my_list)

my_list.remove(40)
print(my_list)
last_element = my_list.pop()
print(last_element)
print(my_list)
first_element = my_list.pop(0)
print(first_element)
print(my_list)










#  compare and contrast tuple and list with example

'''ans:
Tuples and lists are both fundamental data structures in Python that can hold collections of items, but they have distinct characteristics. 
Here's a detailed comparison of the two:
 Mutability
List: Mutable, meaning you can change its content (add, remove, or modify elements) after the list has been created.
Tuple: Immutable, meaning once it’s created, its content cannot be changed. You can’t add, remove, or modify elements.
'''
#  list example
my_list = [1, 2, 3]
my_list[1] = 20
my_list.append(4)
print(my_list)

# Tuple example
my_tuple = (1, 2, 3)
#  my_tuple[1]=10 this will give us an error in our code
print(my_tuple)








#  describe key features of sets and provide examples of their use
'''
ans:

Sets are  fundamental data structure in Python, distinct from lists and tuples. 
They are highly useful for various scenarios where you need to work with unique collections of items
Here are the key features of sets
Unordered:

Sets do not maintain any order of elements.
 The items are not indexed, so you cannot access elements by position.'''
my_set = {3, 1, 2}
print(my_set) # if we will execute this code we will get our data in unordered way
'''
Unique Elements:

Sets automatically remove duplicate items. Each element in a set must be unique.'''
my_set = {1, 2, 2, 3, 4, 4, 5}
print(my_set)  # when we will run this code we will get the set where no value will be repeted one value occurs only one time

'''Sets are mutable, which means you can add or remove elements after the set has been created. However, the elements themselves must be immutable'''

my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)

'''No Indexing:

Since sets are unordered, you cannot access elements by index. However, you can check for membership using the in keyword'''


#  discribe the use   case of   tuples and sets in python programing
'''Definition
A tuple is an immutable, ordered collection of elements. Once a tuple is created, its contents cannot be changed. Tuples are defined using parentheses ().

Use Cases
Immutable Data: When you need a collection of elements that should not be modified, tuples are ideal. They provide a guarantee that the data will remain unchanged, which can be important for certain applications.

Return Multiple Values: Functions often return multiple values packed in a tuple. This is a common pattern for returning complex data from functions.


def get_coordinates():
    return (10.0, 20.0)

x, y = get_coordinates()
Dictionary Keys: Tuples can be used as keys in dictionaries because they are immutable. Lists, on the other hand, cannot be used as dictionary keys due to their mutability.


locations = {("New York", "NY"): 100, ("Los Angeles", "CA"): 200}
Fixed Size Collections: When you have a fixed-size collection of elements, a tuple can be used instead of a list. This is useful when the number of elements is known and fixed.

person = ("mayank singh", 21, "Engineer")
Data Integrity: Since tuples are immutable, they can be used to ensure that the data cannot be altered accidentally, providing data integrity.'''

'''Sets
Definition
A set is an unordered collection of unique elements. Sets are defined using curly braces {} or the set() constructor.

Use Cases
Unique Elements: Sets automatically handle uniqueness, so they are perfect for situations where you need to ensure that all elements are distinct.

python
Copy code
unique_numbers = {1, 2, 3, 4}
Membership Testing: Sets provide fast membership testing. Checking if an item is in a set is generally faster than checking if an item is in a list.

numbers = {1, 2, 3, 4}
if 3 in numbers:
    print("3 is in the set")
Set Operations: Sets support mathematical operations such as union, intersection, and difference, which can be useful for various algorithms and data processing tasks.


a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # Intersection: {3}
print(a | b)  # Union: {1, 2, 3, 4, 5}
Removing Duplicates: Sets can be used to remove duplicates from a collection. Converting a list to a set automatically removes duplicate values.


numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)
Efficient Data Processing: Sets are often used in scenarios where fast lookups, additions, and deletions are required, especially when the order of elements is not important.





'''


# discuss how to add , modify and delete item in a dictionary  with example
'''Adding Items
You can add items to a dictionary by assigning a value to a new key.'''
#  example:

person = {
    'name': 'mayank',
    'age':21
}


person['city'] = 'delhi'

print(person)

''' Modifying Items
To modify an existing item in a dictionary, you simply assign a new value to an existing key.'''

person = {
    'name': 'mayank',
    'age': 21,
    'city': 'delhi'
}


person['age'] = 31

print(person)


'''Deleting Items
You can delete items from a dictionary using the del statement or the pop() method.'''
# Creating an initial dictionary
person = {
    'name': 'mayank',
    'age': 21,
    'city': 'delhi'
}


del person['city']

print(person)


#  discuss the importance of dictonery keys being immutable and provide example
'''In Python, dictionary keys must be immutable, which means they cannot be changed after they are created.
 This immutability is crucial for maintaining the integrity and consistency of dictionary data. 
Here’s why it’s important and how it affects the use of dictionaries:'''


''' Hashing Consistency: Dictionaries in Python use hash tables for fast lookups. Each key is hashed to a unique value that determines its position in the table. For this hashing to work correctly, the key must be immutable so that its hash value remains consistent throughout its lifetime. If keys were mutable and could change, their hash values would change, potentially leading to inconsistencies and errors in dictionary operations.

Data Integrity: Immutable keys ensure that once a key is added to the dictionary, it cannot be altered. This provides data integrity because the key-value relationship is preserved, and the dictionary structure remains stable.

Efficient Lookups: The efficiency of dictionary operations, such as lookups, insertions, and deletions, relies on the ability to quickly compute and retrieve hash values. Immutable keys guarantee that the hash computation does not need to be recalculated, which keeps these operations efficient.  '''






