# VARIABLES

# Variables are easy to understand. They simply point to values
a = 1
b = 2

print(a)	# Out: 1
print(b)	# Out: 2
print()

# We can also change the value of an existing variable
a = 4

# Setting a variable to another variable gets the value of the other variable 
# and sets the first variable to point to that value.
value_a = 8
value_b = value_a	# This makes value_b point to 8, not value_a
value_a = 5
print(value_b)	# Out: 8 (Note that value_b didn't change when value_a changed)
print()

# Like many other things in Python, variable are case-sensitve
thing = 9
THING = 10
print(thing)	# Out: 9
print(THING)	# Out: 10

# It is best practice for variables to be lowercase with underscores
# separating each word
college_town = "Bloomington"
print()
