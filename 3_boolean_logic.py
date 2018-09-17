# BOOLEAN LOGIC

# Sometimes you can't handle the truth. Luckily, Python can handle it just
# fine! In Python land, there are only two possible answers to a statement:
# True or False. These are known as Boolean values

# In Python, '=' is assigning and '==' is comparing. Comparing will return
# a Boolean value
favorite_fruit = "orange"
print(favorite_fruit == "orange")	# Out: True
print(favorite_fruit == "banananana")	#Out: False
print(type(True))	# OUt: <class 'bool'>
print()

# There are other operators beyond '=='. Most are self-explanatory
a = 1
b = 5000
print(a == b)	# Out: False
print(a < b)	# Out: True
print(a >= b)	# Out: False
print(a != b)	# Out: True		('!=' means not equal to)
print()

# We can also combine multiple comparison with 'and' and 'or'
and_case = (1 == 1 and 2 == 2)
print(and_case)	# Out: True

or_case = (1 == 4 or 2 == 2)
print(or_case)	# Out: True

# 'not' is also helpful in comparisons by negating the operation
and_case2 = not(1 == 1 and 2 == 2)
print(and_case2)	# Out: False
print()

# 'in' is a really easy to way to check if the contents are in an iterable
# class
singers = "Beyonce, Frank Ocean, 6lack, Usher, Ariana Grande"
print("Beyonce" in singers)	# Out: True
print("George Bush" not in singers)	# Out: True
print()

# Now, we know what True and False are. But what if we want to execute
# different code depending on something. That's where 'if' comes in!
its_raining = True
if its_raining == True:
	print("It's raining!")
else:
	print("Clear skies.")	# This won't run

# if statements might have more than one condition. That's where you can use
# elif, which is short for 'else if'
ohio_state = 3
indiana = 10
if (ohio_state == indiana):
	print("We got a tie game")
elif (ohio_state > indiana):
	print("Ohio State is winning")
else:
	print("Indiana is winning")

# The if statement simply checks to see if the condition is True. It could be
# as simple as this
if True:
	print("This will always print out til the end of time")
else:
	print("This will never print out")
