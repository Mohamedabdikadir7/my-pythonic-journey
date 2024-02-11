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