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