# FOR LOOPS

kendrick_albums = ['Section.80', 'Good Kid, M.A.A.D City', 
				   'To Pimp a Butterfly', 'DAMN', 'Kids on Butterflies']

# Let's go back to this updated Kendrick Lamar album list above. Let's say
# we want to print each of these out. A super quick way to perform the same
# command on each item is to use a for loop
for album in kendrick_albums:
	print(album)
print()

# ^ Notice that I never declared the variable 'album'. In a for loop, this 
# variable is created in the first line and dynamically changes its value
# each time the for loop 'iterates' through the list.

# You can also loop through lists of numbers. Here's a popular way to find the
# sum of a list of numbers
sum = 0		# Declare the sum to be zero at the beginning
for number in [1,2,3,4,5,6]:
	sum = sum + number

print(sum)	# Out: 21
print()

# You can even loop through Strings!
for character in "pizza":
	print(character.upper())	# upper() is a popular method for a String
print()

# Any class that we can loop through is 'iterable'. Lists and Strings are both
# iterable

# Challenge: Print out all the albums in kendrick_albums that contain a space
for album in kendrick_albums:
	if " " in album:
		print(album)

