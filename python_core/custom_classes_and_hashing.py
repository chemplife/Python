'''
If there is no __eq__() method available, equality of class objects are based on 'is' operator, which checks the id of the objects.
Hash of the class object are based on the 'id' of the object.
So, even if obj1 == obj2 		-> AFTER implementing __eq__()
	but id(obj1) != id(obj2)
	so, hash(obj1) != hash(obj2)

But after implementing __eq__(), the hash() function looks for obj.__hash__() implementation
	and if it doesn't find it, it will return 'OBJ NOT HASHABLE'

This is becasue, condition of hash() function is violated.
Hash Conditions: if 	val1 == val2
				MUST	hash(val1) == hash(val2)
				Return value must be integer.

		This is to produce identical probe sequence

So, if obj1 == obj2			Because of __eq__()
we need to implement 		__hash__() for hash(obj)
'''

class Person:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'Person class with name= {self.name}'

	def __eq__(self, other):
		if isinstance(other, Person):
			return self.name == other.name
		else:
			return False

	def __hash__(self):
		return hash(self.name)

p1 = Person('john')
p2 = Person('john')

print('Is p1 and p2 same: ', p1 is p2)
print('Are p1 and p2 equal: ', p1 == p2)
print('Are hash(p1) and hash(p2) equal: ', hash(p1) == hash(p2))

#Since the hash() for p1 and p2 are equal, for dictionary 'd', they are in essence, the same 'key'
d = {p1: 78}
print('\nAccessing d[p1] with d[p2]: ', d[p2])

# If we want our class to be NONE HASHABLE
class Persons:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'Person class with name= {self.name}'

	# This will override the default Hash() for the class.
	# Now, the objects this class cannot be used as Dictionary Keys.
	__hash__ = None


print('\n\n--------------- Have Mutable Keys ---------------')

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f'({self.x},{self.y})'

	def __eq__(self, other):
		if isinstance(other, tuple) and len(other)==2:
			other = Point(*other)
		if isinstance(other, Point):
			return self.x == other.x and self.y == other.y
		else:
			return False

	def __hash__(self):
		return hash((self.x, self.y))

pt1 = Point(0,0)
pt2 = Point(1,1)
points = {Point(0,0): 'Origin', Point(1,1): 'point at (1,1)'}
print('Point Dictionary: ', points)
print('Different ways to get the value from dictionary:')
print('Way 1: points[Point(0,0)] ->', points[Point(0,0)])
print('Way 2: points[(0,0)] ->', points[(0,0)])
print('Way 3: points[pt1] ->', points[pt1])

#Now, pt1 is mutable. So, after mutation, points[pt1] won't work
pt1.x = 10
print('\nNew Point 1 after Mutation: ', pt1)
# print('Way 3: points[pt1] ->', points[pt1])
print('Point Dictionary: ', {k:v for k,v in points.items()})