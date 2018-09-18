# FUNCTIONS

# If you find yourself righting the same exact code over and over again, it
# might be time to define a function. Creating custom fucntions allow you 
# to run the same algorithm no matter where you are in your code

# If you looked at the past tutorials, you are already familiar with a couple
# functions:
print("Print is a function!")
len("King Arthur")
print()

# ^ Yep, print() and len() are both functions! We didn't have to right them
# because they came pre-coded when we installed python. But if you look deep
# into your python download folder, you will be able to see them defined.

# Let's create our own simple function. 
def see_meatballs():
	print("meatballs")

see_meatballs()	# Out: meatballs
see_meatballs() # Out: meatballs

# ^ see_meatballs() is defiitely a function, but it's not too helpful than
# just coding 'print("meatballs")'. So, what if we want to type 'meatballs'
# an x amount of times? That's where function parameters come in.
def see_meatballs_repeat(times_repeated):
	print("meatballs" * times_repeated)

see_meatballs_repeat(5)	# Out: meatballsmeatballsmeatballsmeatballsmeatballs
print()

# ^ Pretty cool, huh? We can insert 100 as a parameter and let the function do
# the hard work.

# This next function is tough, but it applies all the same concepts. Let's
# create a function to calculate Present Value. 
# PV = FV * (1 / (1 + i) ^ n)
def get_present_value(future_value, interest_rate, years):
	
	pv_factor = (1 / (1 + interest_rate) ** years)	# ** raises an exponent
	present_value = future_value * pv_factor

	present_value = round(present_value, 2)

	return present_value

pv_1 = get_present_value(1000, .10, 20)
print(pv_1)	# Out: 148.64

# ^ Okay- a lot of things to unpack here. Let's walk through it:
# 	- When a function has many parameters, they are separated by commas
# 	- variables can be declared inside a function
#	- I called round(), another pre-installed function, to round my answer to 2
#	  decimal places
# 	- A function usually will 'return' a value. A return statement is better
#	  than printing something out because you can store it as a variable as I 
#	  did on line 48. You can always print it out. 'return' can only be used
#	  once in a function! Once it's called, the function stops

# There are 2 types of variables in Python: global and local. Global variables
# are outside all functions and loops and can be used anywhere. Conversly, 
# local variables are inside functions and loops deleted when the function
# exits
global_variable = "I'm global"
def print_values():
	
	print(global_variable)

	local_variable = "I'm local. I can only be acccessed inside this function"
	print(local_variable)
