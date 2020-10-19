class Rectangle:
	#Not Important to define
	def __new__(_cls, width, height):
		'''This is 1st step.
			Creates the instance of the class.
			Mark the 2 class paramenters.
			'''

	def __init__(self, width, height):
		'''This is 2nd Step.
			Initialize the clsss parameters'''
		self._width = width
		self._height = height

	#Not Important to define
	def __repr__(self):
		'''returns a nicely formated representation of class in string format.'''
		return self.__class__.__name__

	# This property will allow us to use object.width instead of object._width
	# basically, self.width will call this width property method
	@property
	def width(self):
		return self._width

	# property 'width' allow to make a setter method to add logic to the object parameter
	@width.setter
	def width(self, width):
		if width <=0:
			raise ValueError("Width cannot be 0 or negative")
		else:
			self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		if height <=0:
			raise ValueError("Height cannot be 0 or negative")
		else:
			self._height = height

	def area(self):
		return self.width*self.height

	# this will override the str() method to return what we want
	def __str__(self):
		return "Rectangle with {0} width and {1} height"\
				.format(self.width, self.height)

	''' 
	this help compare 2 objects of the same class.
	do the same for:
		1. __lt__ (less than)
		2. __gt__ (greater than)
		3. __lte__ (less than equal)
		4. __gte__ (greater than equal)
	'''
	def __eq__(self, other):
		# this will make sure that the 2nd object is of the same class
		if isinstance(other, Rectangle):
			return (self.width, self.height) == (other.width, other.height)
		else:
			return False

w = input("Enter width:")
h = input("Enter Height:")
r1 = Rectangle(int(w),int(h))
print(r1.area())
print(str(r1))

r2 = Rectangle(w,h)
print(r2.area())
print(str(r2))

print(r1 is r2)
print(r1==r2)
print(r1==100)