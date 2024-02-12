#Tuples allow you to do just that. Python refers to values that cannot
#change as immutable, and an immutable list is called a tuple.

# syntax 

#my_tuple = (item1, item2, item3, ...)

# Access Tuple Items

mylit = ("apple" , "mango" , "juice" )
print(mylit[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-5:-1])

# Example 1: Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple elements:", my_tuple)

# Example 2: Accessing tuple elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Example 3: Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# Example 1: Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple elements:", my_tuple)

# Example 2: Accessing tuple elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Example: Tuples in Python

# Creating a tuple of coordinates
point = (3, 4)
print("Point coordinates:", point)

# Accessing elements in a tuple
x = point[0]
y = point[1]
print("X-coordinate:", x)
print("Y-coordinate:", y)

# Tuple packing and unpacking
person = ("John", "Doe", 30)
print("Person details:", person)

# Unpacking the person tuple
first_name, last_name, age = person
print("First name:", first_name)
print("Last name:", last_name)
print("Age:", age)

# Tuple as a return value from a function
def get_coordinates():
    return 5, 7

coordinates = get_coordinates()
print("Coordinates:", coordinates)


