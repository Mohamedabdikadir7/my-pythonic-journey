# are used to store multiple item on single variable exampe

mylist = ['apple' , 'mango' , 'guava']
print(mylist)

#Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# we can acces element in lists 

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist[0])


# list metod 
# 1 append this adds new item on the back
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist.append('mango')
print(thislist)

# reverse list we use .reverse()

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist.reverse()
print(thislist)

# pop removes the last part or element 

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist.pop()
print(thislist)

#finding values we use .index

thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist.index("apple"))

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

