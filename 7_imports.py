# IMPORTS

# Let's say we want to generate a random number between 1 and 3. How
# would be do it? The 'random' module is a really easy way to do this:
import random

print(random.randint(1,3))
print()

# Woah, where did that comes from?
# When you 'import' a module, such as 'random', you are accepting all the
# code from that particular module. What's a module, exactly? It could be a
# another .py file or a file of .py files. Let's see what random is:
print(random)	# Out: <module 'random' from 'C:\\Python36\\lib\\random.py'>

# Looks like it gives us a file path in our computer. It points to a .py file.py
# called random.py! Random.py is just another python file that consists of a
# class, functions, methods, and variables that we can use.

# 'math' is a nother popular import that contains many popular math functions
# and numbers
import math
print(math.pi)	# Out: 3.141592653589793
print(math.radians(360))	# Out: 6.283185307179586

# Bonus: If you only need one or two things from the module, you can
# specifically say so:
from math import sin, pi
print(sin(pi / 2))	# Out: 1.0	

# ^ Now, you don't have to place 'math.' in front of it

