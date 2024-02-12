# In Python, conditions are used to make decisions based on whether certain conditions are true or false.


#Comparison operators are used to compare values.

# ==: Equal to
# !=: Not equal to
# <: Less than
# >: Greater than
# <=: Less than or equal to
# >=: Greater than or equal to

# If Statement
# The if statement is used to execute a block of code only if a condition is true.

x = 5 
if x > 7:
    print("x is greater")

# example 2 
age = 17 
if age >= 18:
    print("you can vote")
    print("Have you registered to vote yet?")

#If-else statements
#The if-else statement is used to execute one block of code if the condition is true and another block if it's false.
    
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


#Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# example 2 
x = 20
if x > 25:
    print("x is greater than 25")
elif x > 10:
    print("x is greater than 10 but less than or equal to 25")
else:
    print("x is less than or equal to 10")


#nested if
# You can also nest if statements within other if statements to handle more complex conditions.

x = 10
if x > 12:
    if x < 15:
        print("x is between 5 and 15")


# exercise 
# online store 
        
# Prompt the user to enter the total purchase amount
total_purchase_amount = float(input("Enter the total purchase amount: $"))

# Define discount rates
discount_rate_10 = 0.1  # 10% discount
discount_rate_5 = 0.05  # 5% discount

# Calculate the discount based on the total purchase amount
if total_purchase_amount >= 100:
    discount = total_purchase_amount * discount_rate_10
elif total_purchase_amount >= 50:
    discount = total_purchase_amount * discount_rate_5
else:
    discount = 0

# Calculate the discounted amount
discounted_amount = total_purchase_amount - discount

# Display the result
print("Total Purchase Amount: ${:.2f}".format(total_purchase_amount))
print("Discount Applied: ${:.2f}".format(discount))
print("Discounted Amount: ${:.2f}".format(discounted_amount))


# Example 1: Simple if-else statement
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

# Example 2: Nested if-else statement
num = -5
if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is zero")
else:
    print("Number is negative")

# Example: If-Else Inside Loop
numbers = (5, 10, 15, 20)
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
