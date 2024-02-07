#You can return a range of characters by using the slice syntax.
# examples

# Slice From the Start

b = "Hello, World!"
print(b[:5]) 

 # here the out put will be hello it started at the front using the :  symbole

# Slice From the end 

b = "Hello, World!"
print(b[5:]) 
# the output will be world since it sliced from the end 

 # Negative Indexing

b = "Hello, World!"
print(b[-2])
# here the indexing start from the back and the output will be d 

# making strings to uppercase  we use upper() functions example

a = "hello world "
print (a.upper())

# to lower we use  lower()  example

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# concantatanet strings 

a = "hello"
b = "world"
c = a+ " " +b

print(c)

# Format - Strings

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {1} pieces of item {1}."
print(myorder.format(quantity, itemno, price))