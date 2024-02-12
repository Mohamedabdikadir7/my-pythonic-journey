# Python’s range() function makes it easy to generate a series of numbers

# To generate a sequence of numbers from 0 to 4:

# for num in  range (1,5):
#     print(num)

# for value in range(1,1000):
#    print(value)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])

x = range(3, 6)
for n in x:
  print(n)

  #Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:

x = range(3, 20, 2)
for n in x:
  print(n)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Example 1: Creating a range
my_range = range(5)
print("Range:", my_range)  # Output: range(0, 5)

# Example 2: Iterating through a range
for num in my_range:
    print(num, end=" ")  # Output: 0 1 2 3 4
print()  # Print a newline

# Example 3: Creating a range with start and stop values
my_range_2 = range(2, 10)
print("Range with start and stop values:", my_range_2)  # Output: range(2, 10)

# Example 4: Creating a range with step value
my_range_3 = range(1, 10, 2)
print("Range with step value:", my_range_3)  # Output: range(1, 10, 2)

# Example 5: Checking if a value is in a range
value = 6
if value in my_range_2:
    print(f"{value} is in the range.")
else:
    print(f"{value} is not in the range.")
