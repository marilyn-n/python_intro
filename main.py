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
 