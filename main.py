# imports

import random

# comments in python start with a hash 

'''
multiline 
comments
'''

# it prints data to the screen
print('My name is Marilyn')

greetings = 'Good afternoon'
name = 'Marilyn'
print(greetings + ' ' + name)
# or ,
print(greetings, name)

# Arithmetic operators

print(5**5)
print(3 + 5)
print(23 - 4)
print(9 / 2)
print(3 * 1)
print(7 % 43)

# A string is a string of characters surrounded by " or '
# If you must use a " or ' between the same quote escape it with \
quote = "\"Always remember you are unique,"
print(quote)

# A multi-line quote
multi_line_quote = ''' just
like everyone else" '''

print(multi_line_quote)

# LISTS -------------------------------------------------------------------------
# A list allows you to create a list of values and manipulate them
# Each value has an index with the first one starting at 0
 
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('The first item is', grocery_list[1])

# You can change the value stored in a list box
grocery_list[0] = "Green Juice"
print(grocery_list)

print(grocery_list[1:3])

# You can put any data type in a list including a list
other_events = ['Wash Car', 'Pick up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]
 
print(to_do_list)

# Get the second item in the second list (Boxes inside of boxes)
print(to_do_list[1][1])

# You add values using append
grocery_list.append('Onions')
print(to_do_list)

# Insert item at given index
grocery_list.insert(1, "Pickle")
print(grocery_list)

# Remove item from list
grocery_list.remove("Pickle")
print(grocery_list)

# Sorts items in list
grocery_list.sort()
print(grocery_list)

# Reverse sort items in list
grocery_list.reverse()
print(grocery_list)

# del deletes an item at specified index
del grocery_list[4]
print(to_do_list)

# We can combine lists with a +
to_do_list = other_events + grocery_list
print(to_do_list)

# Get length of list
print(len(to_do_list))

# Get the max item in list ???????????????????????????????????????????????????????????????
print(max(to_do_list))

# Get the minimum item in list
print(min(to_do_list))

# TUPLES ---------------------------------------------------------
# Values in a tuple can't change like lists
 
pi_tuple = (3, 1, 4, 1, 5, 9)
 
# Convert tuple into a list
new_tuple = list(pi_tuple)
print(new_tuple)

# Convert a list into a tuple
new_list = tuple(grocery_list)
print(new_list)
 
# tuples also have len(tuple), min(tuple) and max(tuple)
 
# DICTIONARY or MAP -------------------------------------------------
# Made up of values with a unique key for each value
# Similar to lists, but you can't join dicts with a +

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}
 
print(super_villains['Captain Cold'])
 
# Delete an entry
del super_villains['Fiddler']
print(super_villains)

# Replace a value
super_villains['Mirror Master'] = 'Hartley Rathaway'
print(super_villains)

# Print the number of items in the dictionary
print(len(super_villains))

# Get the value for the passed key
print(super_villains.get("Pied Piper"))

# Get a list of dictionary keys
print(super_villains.keys())

# Get a list of dictionary values
print(super_villains.values())

# CONDITIONALS -------------------------------------------------------------
# The if, else and elif statements are used to perform different
# actions based off of conditions
# Comparison Operators : ==, !=, >, <, >=, <=
 
# The if statement will execute code if a condition is met
# White space is used to group blocks of code in Python
# Use the same number of proceeding spaces for blocks of code
age = 30 

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive') 

# If you want to check for multiple conditions use elif
# If the first matches it won't check other conditions that follow
 
if age >= 21 :
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else :
    print('You are not old enough to drive')

# You can combine conditions with logical operators
# Logical Operators : and, or, not
 
if ((age >= 1) and (age <= 18)):
    print("You get a birthday party")
elif (age == 21) or (age >= 65):
    print("You get a birthday party")
elif not(age == 30):
    print("You don't get a birthday party")
else:
    print("You get a birthday party yeah")

# FOR LOOPS ----------------------------------------------------------
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9

for x in range(0, 10):
    print(x , ' ', end="")
 
print('\n')

# You can use for loops to cycle through a list
for i in grocery_list:
    print(i)

# You can also define a list of numbers to cycle through
for x in [2,4,6,8,10]:
    print(x)    

# You can double up for loops to cycle through lists
num_list =[[1,2,3],[10,20,30],[100,200,300]]
 
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

# WHILE LOOPS --------------------------------------------------
# While loops are used when you don't know ahead of time how many
# times you'll have to loop

random_num = random.randrange(0,100)
 
while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

# FUNCTIONS ------------------------------------------------------
# Functions allow you to reuse and write readable code
# Type def (define), function name and parameters it receives
# return is used to return something to the caller of the function

        