#In Python, you define a function using the def keyword followed by the function name and parentheses containing any parameters the function takes.


#syntax
# def function_name(parameter1, parameter2, ):
#     # Function body
#     # Perform actions
   

def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    """
    result = a + b
    return result

# Calling a Function:

# To call a function, you simply use its name followed by parentheses and provide any required arguments:

# now lets call the above function 

#result = add_numbers(5, 3)
#print(result)  # Output: 8

def addnumers(a,b):
    result = a +b
    return result

#result = addnumers(6,8)
#print(result)


# example 2 
def great_user(name):
 print("Hello, " + name + "! Welcome to our platform.")

 # calling the function

 user_name = input("what is your name:")
 great_user(user_name)

def greet_user(name):
    """
    This function greets the user by name.
    """
    print("Hello, " + name + "! Welcome to our platform.")

# Calling the function
#user_name = input("Please enter your name: ")
#greet_user(user_name)


#  Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the
#function, and make sure the message displays correctly

def display_message():
   print("i am learning python")
display_message()

# def describe_pet(pet_name, animal_type):
#   print("I have " + animal_type + ".")

# print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('harry' , 'hamster')


def describe_pet(pet_name, animal_type):
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Call the function with arguments 'harry' and 'hamster'
describe_pet('harry', 'hamster')
