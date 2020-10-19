'''
super().method()/attribute
	-> To deligate things back to the parent class.
	-> Use this only when you have the same named function in the child as well.. Because Python anyways will look uo the heirarchy
		if it does not find the method in Child-class.
		Eg:		class A:
					def b():

				class B(A):
					def c():
						return self.b()		<- is same as -> return super().b()		<- Because 'class B'' does not have 'def b()' of its own.

self: binds the instance of the object to the method anywhere in the herarchy.

** if the 'Parent-Class' has '__init__(seld, name)' method that takes in an argument and the 'Child-Class' does not have a '__init__(self)' defined:
	-> 'Child-Class' instance need that argument (name) because it is inheritied from the 'Parent Class'
'''

class Person:
	def hello(self):
		print('In Person Class: ', self)

class Student(Person):
	def hello(self):
		print('In Student Class: ', self)
		super().hello()

p = Person()
s = Student()

p.hello()
print('\n')
# Looks at the address of 'self'.. it is the same in 'Person Class' as it is for 'Student Class'
s.hello()

print('\n\n-------------------------------- Combined Example: Property/Inheritance/Deligate/Caching --------------------------------')

from math import pi
from numbers import Real

class Circle:
	def __init__(self, r):
		self.radius = r
		self._area = None
		self._perimeter = None

	@property
	def radius(self):
		return self._r

	@radius.setter
	def radius(self, r):
		if isinstance(r, Real) and r > 0:
			self._r = r
			self._area = None
			self._perimeter = None

		else:
			raise ValueError('Radius must be a Positive Real Number.')


	@property
	def area(self):
		if self._area is None:
			self._area = pi * self.radius **2
		return self._area

	@property
	def perimeter(self):
		if self._perimeter is None:
			self._perimeter = 2 * pi * self.radius
		return self._perimeter

class UnitCircle(Circle):
	def __init__(self):
		super().__init__(1)


u = UnitCircle()

print('UnitCircle Radius:', u.radius)
print('UnitCircle Area:', u.area)
print('UnitCircle Perimeter:', u.perimeter)

#But this will work..
u.radius = 10
print('\nProblem: UnitCircle Radius:', u.radius)

# To make the Radius for Unit-Circle read-only..

class UnitCircle_1(Circle):
	def __init__(self):
		super().__init__(1)

	@property
	def radius(self):
		return self.radius 		# return super().radius ;; will work the same.

# Now it will not work... even without setting u1.radius=10.. Because now, the 'self.radius' in 'circle.__init__()' does not take any argument.
# ** we cannot call the 'radius.setter' from outside of the class.
# u1 = UnitCircle_1()
# u1.radius = 10
# print('\nProblem: UnitCircle_1 Radius:', u1.radius)

# To fix, this, we need to make the 'self.radius' in 'circle.__init__()' call a method to set radius..

class Circle:
	def __init__(self, r):
		self._set_radius(r)
		self._area = None
		self._perimeter = None

	@property
	def radius(self):
		return self._r

	def _set_radius(self, r):
		if isinstance(r, Real) and r > 0:
			self._r = r
			self._area = None
			self._perimeter = None
		else:
			raise ValueError('Radius must be a Positive Real Number.')

	@radius.setter
	def radius(self, r):
		self._set_radius(r)


	@property
	def area(self):
		if self._area is None:
			self._area = pi * self.radius **2
		return self._area

	@property
	def perimeter(self):
		if self._perimeter is None:
			self._perimeter = 2 * pi * self.radius
		return self._perimeter

class UnitCircle_1(Circle):
	def __init__(self):
		super().__init__(1)

	@property
	def radius(self):
		return super().radius

u = UnitCircle_1()
print('\n')
print('UnitCircle Radius:', u.radius)
print('UnitCircle Area:', u.area)
print('UnitCircle Perimeter:', u.perimeter)

#Now this will not work..
# u.radius = 10
# print('\nProblem: UnitCircle Radius:', u.radius)

print('\n\n------------------------------------------- Slots -------------------------------------------\n')
'''
Class inherently use 'DICTIONARY' to store all the attributes.
But when we have a lot of instances of the class.. it will create a lot of memory-overhead..

To do it in a better 'memory-efficient-way'.. SLOTS are used

Slots- more compact datastructe that Python.

We need to tell slots what all attributes we will have in advance.
__slots__ = ('x', 'y')

('x', 'y')	-> Iterable..
__slots__	-> tells Python that don't use dictionary.. use slots..

Now, Both of these will give error
	-> obj.__dict__	:	Attribute Error
	-> vars(obj)	:	Tyoe Error

But ->	dir(obj)	: will tell us about 'x' and 'y'

Slots V/S Dict
	-> Slots are 'Memory-Effecient'	: Save 10 times the memory compared to Dict.
	-> Slots are 'Time-Effecient'	: Runs 30% faster then Dict.
	
	-> Slots: Cannot add attributes (Monkey-Patching) during the program.. Dict, we can add attributes on the fly..
'''

class Location:
	__slots__ = 'name', '_longitude', '_latitude'

	def __init__(self, name, *, longitude, latitude):
		self._longitude = longitude
		self._latitude = latitude
		self.name = name

	@property
	def longitude(self):
		return self._longitude
	
	@property
	def latitude(self):
		return self._latitude

print('Location Dict: ', Location.__dict__)
Location.map_service = 'Google Maps'
print('\nLocation Dict after Attribute Addition: ', Location.__dict__)

#But we don't have Instance-Dictionary
l = Location('Delhi', longitude=100, latitude=72)
# print('\nLocation Instance Dict: ', l.__dict__)

print('\n\n--------------------------- Slots with Single Inheritance ---------------------------\n')
'''
-> 'Child-Class' will use the 'slots' FROM 'Parent-Class' if present. But 'Child-Class' will have its own '__dict__' to store attributes.
-> 'Child-Class' can have 'slots' even if 'Parent-Class' DON'T have it. 'Child-Class' will still have a '__dict__' to store attributes.
-> If Child-Class also needs to have 'Slots', mention those in the 'Child-Class' which are not in 'Parent-Class'.. Don't re-mention attributes.
	-> If re-mentioned:
		-> In future updates from Python it will break (It is marked to have a 'check-on' in future.)
		-> It hides the Parent Attribute and can cause problems.
		-> Increase memeory overhead due to re-mentioning..

************************
How to use both 'Slots' and '__dict__'?
	-> __slots__ = 'attributes', .. , '__dict__'
		-> Now, we can add more attributes during run-time.. (__dict__ is not dropped..)
		-> Nowly added attributes will get stored in '__dict__' and not in 'slots' 
'''
class Person:
	__slots__ = 'name'

class Student(Person):
	pass

p = Person()
s = Student()
s.name = 'Alex'
print('Student Instance Dict: ', s.__dict__)
s.age = 18
print('\nStudent Instance Dict: ', s.__dict__)

# This will not work
#print('Person Instance Dict: ', p.__dict__)

