'''
LAZY EVALUTION: Don't evaluate something until it is requested.
'''

# How to get area of a circle as property when only radius is passed.

import math

# Currently, area is calculated each time radius change
class Circle:
	def __init__(self, r):
		self.radius = r

	@property
	def radius(self):
		return self._radius

	@radius.setter
	def radius(self, r):
		self._radius = r
		print('Calculating Area')
		self.area = math.pi*(self._radius**2)

obj1 = Circle(5)
print('Area 1:', obj1.area)

# This will calculate the area as well.
obj2 = Circle(2)

print('-----------------------------------------------------------')

# Calculate area only when it is asked. LAZY EVALUATION
class Circle:
	def __init__(self, r):
		self.radius = r

	@property
	def radius(self):
		return self._radius

	@radius.setter
	def radius(self, r):
		self._radius = r
	
	@property
	def area(self):
		print('Calculating Area')
		return math.pi*(self.radius**2)

obj1 = Circle(5)
print('Area 1:', obj1.area)

# This will not calculate the area is it is not asked to.
obj2 = Circle(2)

print('Area 1:', obj1.area)
####
# The area is still getting calculated each time 'area' is asked for.
# Good idea: If Radius did not change, area only should get calculated once. Not everytime.
# Still calculating it in LAZY EVALUTAION fashion.
####

print('-----------------------------------------------------------')

class Circle:
	def __init__(self, r):
		self.radius = r
		self._area = None

	@property
	def radius(self):
		return self._radius

	@radius.setter
	def radius(self, r):
		self._radius = r
		self._area = None
	
	@property
	def area(self):
		if not self._area:
			print('Calculating Area')
			self._area = math.pi*(self.radius**2)
		return self._area

obj1 = Circle(5)
print('Area 1:', obj1.area)
print('Area 1 reprint:', obj1.area)

obj2 = Circle(2)
print('Area 2:', obj2.area)
print('Area 2 reprint:', obj2.area)

print('-----------------------------------------------------------')
####
# Factorial Calculation only when the value for a number is requested.
# Using custom Iterator
####

class Factorial:
	def __init__(self, length):
		self.length = length

	def __iter__(self):
		return self.FactIter(self.length)

	class FactIter:
		def __init__(self, length):
			self.length = length
			self.i = 0

		def __iter__(self):
			return self

		def __next__(self):
			if self.i >= self.length:
				raise StopIteration
			else:
				result = math.factorial(self.i)
				self.i += 1
				return result

fact = Factorial(3)
print('fact:', list(fact))