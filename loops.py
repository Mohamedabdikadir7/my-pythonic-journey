# in python we have 2 loops for and while loop
#loops mean Python loops are control structures that allow you to execute a block of code repeatedly based on a condition.

# for loop
#For loops in Python are used to iterate over a sequence (like a list, tuple, string, etc.) and execute a block of code once for each element in the sequence.

# syntax
#Sfor item in sequence:
    # code block to be executed for each item

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

fruits = ["apple" , "banana" , "cherry"]
for k in fruits:
    print(k)

for i in range(5):
    print(i)

#The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 5:
  print(i)
  i += 1

  i = 0
i += 1  # Increment i by 1
print(i)  # Output will be 1

count = 1
while count <= 5:
    print(count)
    count += 1

# Example 1: Basic while loop
count = 0
while count < 5:
    print(count, end=" ")  # Output: 0 1 2 3 4
    count += 1
print()  # Print a newline

# Example 2: Using a while loop with a condition
number = 10
while number > 0:
    print(number, end=" ")
    number -= 2  # Decrement by 2
print()  # Print a newline

# Example 3: Using a while loop with a break statement
num = 1
while True:
    print(num, end=" ")
    num += 1
    if num > 5:
        break  # Break the loop when num is greater than 5

# Example: Using loops
# Looping through a list of numbers
numbers = [1, 2, 3, 4, 5]
print("Numbers:")
for num in numbers:
    print(num)



# Nested loops
print("Nested Loop:")
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
