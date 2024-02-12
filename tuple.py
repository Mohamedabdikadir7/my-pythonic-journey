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
