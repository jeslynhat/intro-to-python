# Assignment 5 - Create a Class Rectangle

# First, I add the Point class. This class represents a point on a 2D grid (like the corner of a rectangle).
class Point:
	def __init__(self, x, y):
		self.x = x	# This is my x-coordinate
		self.y = y	# This is my y-coordinate
	
# Next, I add the Rectangle class. This class represents the rectangle using a corner point, width, and height
class Rectangle:
	"""A class to manufacture rectangle objects"""
	
	def __init__(self, posn, width, height):
		"""Initialize rectangle at posn, with width and height"""
		self.corner = posn	# This is the bottom-left corner of the rectangle (a Point).
		self.width = width	# This is how wide the rectangle is
		self.height = height #Thisis how tall the rectangle is
	
	def __str__(self):
		return f"({self.corner.x}, {self.corner.y}, {self.width}, {self.height})"
# The return will make it easy to print the rectangle in a returnable format.


# Next, I add the four required functions
# This function creates a new rectangle using x, y, width, and height
def create_rectangle(x, y, width, height):
	return Rectangle(Point(x, y), width, height)


# This function turns the rectangle into a string so we can print it nicely
def str_rectangle(rect):
	return str(rect)


# This function moves the rectangle by changing its corners x and y
def shift_rectangle(rect, dx, dy):
	rect.corner.x += dx 	# This moves it horizontally
	rect.corner.y += dy		# This moves it vertically
	

# This function creates a new rectangle that is offset from the original
def offset_rectangle(rect, dx, dy):
	new_x = rect.corner.x + dx
	new_y = rect.corner.y + dy
	return Rectangle(Point(new_x, new_y), rect.width, rect.height)


# Next I use the test code to check if everything works correctly
if __name__ == "__main__":
	# This creates a rectangle at (10, 20) with width 30 and height 40
	r1 = create_rectangle(10, 20, 30, 40)
	print(str_rectangle(r1))	# This should print (10, 20, 30, 40)
	
	# This moves the rectangle by -10 in x and -20 in y
	shift_rectangle(r1, -10, -20)
	print(str_rectangle(r1))	# This should print: (0, 0, 30, 40)
	
	# This creates a new rectangle offset from r1 by (100, 100)
	r2 = offset_rectangle(r1, 100, 100)
	print(str_rectangle(r1))	# This should still be (0, 0, 30, 40)
	print(str_rectangle(r2))	# This should be (100, 100, 30, 40)
	
	
	
	








