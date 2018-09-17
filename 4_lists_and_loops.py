# LISTS AND LOOPS

# Instead of creating variables for each and every value, it might make more
# sense to store them all in one variable. Any easy way to do this is using
# a list. Let's make a List of Strings:
kendrick_albums = ["Section.80", "Good Kid, M.A.A.D City",
				   "To Pimp a Butterfly", "Untitled Unmasted", "DAMN"]
print(kendrick_albums)	# Out: ['Section.80', 'Good Kid, M.A.A.D City', 'To Pimp a Butterfly', 'DAMN']		
print(type(kendrick_albums))	# Out: <class 'list'> 
print()

# Just like finding the length of a String you use len() with Lists
print(len(kendrick_albums))		# Out: 5

# What if I want to extract the second album in the List? I use a concept
# called 'slicing'
second_album = kendrick_albums[1]
print(second_album)		# Out: Good Kid, M.A.A.D City

# Wait a second... why did we use '1' to get the second item in the list?
# Python using zero-based indexing, which means the first item starts at '0'.
# So if you want to get the first item in the list:
first_album = kendrick_albums[0]
print(first_album)		# Out: "Section.80"
print()

# Let's check if a Drake album is in this list
isTakeCare = "Take Care" in kendrick_albums
print(isTakeCare)	# Out: False
print()

# Lists have these useful things called methods. Methods allow you to mutate,
# or change, an object in a particular way. Two common List methods are 
# append() and remove(), 

# Let's say J Cole and Kendrick finally made that collab album! Let's add
# it to the list
kendrick_albums.append("Kids on Butterflies")
print(kendrick_albums)

# Actually, 'Untitled Unmasted' isn't an album- it's technically an EP. Let's
# remove it
kendrick_albums.remove("Untitled Unmasted")
print(kendrick_albums)

