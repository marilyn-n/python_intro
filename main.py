# imports in Python

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