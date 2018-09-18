# OBJECT ORIENTED PROGRAMMING

# So far, we've dealt with a few different things in Python; we've mostly
# been interacting with Strings and Integers. As we've already shown, 'str'
# and 'int' are known as classes.
print(str)	# Out: <class 'str'>
print(int)	# Out: <class 'str'>
print()

# But what if we want to make our own class? A class that has its own methods
# and attributes. With Python and many other languages, we can use object-
# oriented programming to build our own classes that go beyond simple Strings
# and Integers

# Let's say we're building the football video game, FIFA. A match in FIFA will
# consist of several football players. Instead of indivually coding each 
# player, we can simply create a Player class. 

# Wait, why are we talking about classes? Isn't this OBJECT oriented
# programming? An object is an instance of a class. In our past code, we can
# have many String objects, but they all fall with one String class. You only
# have to write one class in order to create an inifinite amount of objects of
# that class.

# To create a class in Python, simply write 'class <class name>:'
class Player:

	# These 3 variables are the same for every player in the game, no matter
	# what!
	sport = "football"
	num_of_arms = 2
	retired = False

	# The __init__ function is defined in every custom class. When you create
	# a Player object, Python will inuitively call this function. The 
	# parameters (in parenthesis) will be all the variabes that make a
	# particular Player unique. 

	# 'self' is another feature to Python OOP. It is used to reference all the
	# variables and method in the Player class. Think about this: we'll be
	# making a lot of Player instances for this game right? So think of 'self'
	# as one individual instance of this class. Every function must have 'self'
	# as a parameter.  
	def __init__(self, name, country, team, position, height_meters, 
		init_x, init_y):
		
		self.name = name
		self.country = country
		self.team = team
		self.position = position
		self.height_meters = height_meters
		self.pos_x = init_x
		self.pos_y = init_y

	# This is how you make a method for a class. Remember the .append('')
	# method that we used for Lists? This is the same thing but for a Player!
	# You can see how to call this method below. Again, 'self' must be a 
	# parameter.
	def get_info(self):
		print("PLAYER PROFILE: " + self.name)
		print("Country: " + self.country)
		print("Team: " + self.team)
		print("Position: " + self.position)
		print("Height (m): " + str(self.height_meters))

	# Methods typically have a 'return' statement, just like functions.
	# Here, I'm returning the location of a particular player with their
	# x and y positions in a List object.
	def get_location(self):
		return [self.pos_x, self.pos_y]

	# Methods typically change the state of an object. In the next 2 methods,
	# let's develop a way to change the location of the Player
	def move_up(self):
		self.pos_y += 1
		return self.get_location()

	def move_left(self):
		self.pos_x -= 1
		return self.get_location()

	# Methods can accept other parameters. If a particular player is switching
	# teams, we can pass his/her new team as a paramter and change the value
	# of 'self.team'
	def switch_teams(self, new_team):
		self.team = new_team
		print(self.name + " now plays for " + self.team)

# To make a Player instance, you need to call the class with all the paramters
# populated. 'self' does not have a value in this way.
player_1 = Player("Lionel Messi", 
					"Argentina", 
					"Barcelona", 
					"Forward", 
					1.70, 
				   	50, 25)
# ^ You could call 'player_1' a 'a Player instance', 'a Player object', or 
# simply 'a Player'

# Let's call the move_up() method on player_1. Notice I didn't have to assign
# it to a variable
player_1.move_up()

# Now, let's use the get_location() method to see where player_1 is. Since
# the method only returns the value, we have to print is out to see it
print(player_1.get_location())	# Out: [50, 26]
print()

# Look's like Messi got transferred over to Arsenal! Maybe the Gunners can
# finally go further than 4th place :). Let's change Messi's team.
player_1.switch_teams("Arsenal") # Out: Lionel Messi now plays for Arsenal
print()

# Now call the get_info() method to see all of Messi's info.
print(player_1.get_info())


# In my opinion, learning object-oriented programming is when the fun begins.
# If you ever heard something like, "With coding, you can build your own
# worlds," now think about it in the context of OOP. Now, you can build your
# own Player objects, Stadium objects, Warlock objects, Accounts Receivable
# objects, and anything else you can imagine! Then, you can make them interact
# with each other. Then, you can build an app and create mouse, keyboard, and 
# button events for your human users to interact with those objects.  

