	#!/usr/bin/python3
	
	def islower(c):
	    if isinstance(c, str) and len(c) == 1:
	        return ord('a') <= ord(c) <= ord('z')
	    else:
	        return False
	
	# Test the function
	print(islower('a'))  # True
	print(islower('A'))  # False
	print(islower('z'))  # True
	print(islower('Z'))  # False
print(islower('1'))  # False
