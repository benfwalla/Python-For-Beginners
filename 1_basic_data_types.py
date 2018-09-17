# PRINT() AND DATA TYPES

# print()
# Ah, the print function! This is the most simple function in all of 
# python and easiest to understand. Placing something inside the print
# statement will output it on the console
print("Hello World!")	# Out: Hello World!
print('This is a Python String')	# Out: This is a Python String
print()	# Creates a line break in the output

# What you just printed was a String data type. Strings are typically words.
# Other popular data types are Integers and Floats

# Try print() with numbers and math
print(42)	# Out: 42
print(-239)	# Out: -239
print(11 * 7)	# Out: 77
print(9 + 8)	# Out: 17
print(20 / 3)	# Out: 6.666666666666667
print(20 % 3)	# Out: 2
print()

# Strings and Integers behave differently. Experiment!
print("4" + "7")	# Out: 47
print("Repeat" * 4)	# Out: RepeatRepeatRepeatRepeat
print("Hello" + "World")	# Out: HelloWorld
print()

# Integers can be 'casted' in Strings and vice-versa
print("What's 2 + 2? " + str(2+2))	# Out: What's 2 + 2? 4
print(int("4") + int("7"))	# Out: 11
print()

# len() is a built-in function that counts the length of a String
print(len("Al Jumahiriyah al Arabiyah al Libiyah ash Shabiyah al\
	Ishtirakiyah al Uzma"))	# Out: 74
print()

# Strings and Integer are known as classes. There are many classes built into
# Python, and you can even create your own! You can view the class of each
# Python object using the type() function
print(type("This is a String"))	# Out: <class 'str'>
print(type(5))	# Out: <class 'int'>
print(type(20 / 3))	# Out: <class 'float'>
