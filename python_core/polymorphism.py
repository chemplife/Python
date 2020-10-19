'''
Polymorphism:
	-> ability to define a generic type of behavior that will (potentially) behave differently when applied to different object types

-> Duck Typing: If it walks like a duck and quacks like a duck, it is a duck.
	-> If an object has certain behavior, than we can use that object without caring what that object really is.
		Eg: methods that take iterable as parameter: They don't care whether it is a dict, list, or custom class object.
			As long as the iterable protocol is followed, the object is an iterable.

__init__: 		to initialize the instance of class

__enter__:		|-> ised by Context Managers [ with ctx() as obj: ]
__exit__:		|

__getitem__:	|
__setitem__:	|-> used by sequence types ; a[i], a[i:j], del a[i]
__delitem__:	|

__iter__:		|-> iterables and iterators
__next__:		|	iter(), next()

__len__:		|-> implement len()
__contains__:	|-> implement 'in'


Concept 1:
__str__ and __repr__
	-> Both are used to create a string representation of an Instance, and does essentially the same work.
	-> __repr__: used by developer and is useful for debugging. Called by repr(obj)
		-> if __repr__ is not there, Python calls the __repr__ of the base-class (Inheritance.. every class has a common base-class.)
	-> __str__: Called by str(obj) or print(obj).. used to display information for end user
		-> if __str__ is not implemented, Python looks for __repr__.


Concept 2:
Arithmetic Operations:-
	-> __add__:			+
	-> __sub__:			-
	-> __mul__:			*
	-> __trudiv__:		/
	-> __floordiv__:	//
	-> __mod__:			%
	-> __pow__:			**
	-> __matmul__:		@	(Only for Python 3.5+.. Added for better numpy support.)

	To indicate the operation is not supported: implement the method and 'return NotImplemented'. 


	Reflected Operators:-
		a + b 		-> a.__add__(b)		[Python look for __add__ operation for 'a']
		if __add__ NotImplemented for 'a' 		AND 		operands are NOT of same type
			Python swap the operands and try: b.__radd(a)

		-> __radd__
		-> __rsub__
		-> __rmul__
		-> __rtruediv__
		-> __rfloordiv__
		-> __rmod__
		-> __rpow__


	In-Place Operators:-
		They do in-place change in the object. If address is mutable type, the address of the object does not change..

		-> __iadd__:		+=
		-> __isub__:		-=
		-> __imul__:		*=
		-> __itruediv:		/=
		-> __ifloordiv__:	//=
		-> __imod__:		%=
		-> __ipow__:		**=


	Unary Operators:-
		They operators on 1 operand.

		-> __neg__:		-a
		-> __pos__:		+a
		-> __abs__:		abs(a)
'''

from numbers import Real
from math import sqrt


class Vector:
	def __init__(self, *components):
		if len(components)<1:
			raise ValueError('Cannot create an empty Vector.')
		for component in components:
			if not isinstance(component, Real):
				raise ValueError(f'Vector components all must be real numbers. {component} is invalid entry.')
		# args in *args are already tuple.. This is just to reemphisize that its a tuple..
		# This will not create a new tuple.. it will use the originally created one.
		self._components = tuple(components)

	def __len__(self):
		return len(self._components)

	@property
	def components(self):
		return self._components

	def __repr__(self):
		return f'Vector: {self.components}'

	# Since we would need to Validate 'Type' and 'Dimensions' of vectors for add, subt, mul, etc.
	# 1 function for that and reusing it make sense.
	def validate_type_and_dimension(self, v):
		return isinstance(v, Vector) and len(v) == len(self)

	def __add__(self, other):
		if not self.validate_type_and_dimension(other):
			return NotImplemented
		components = (x + y for x,y in zip(self.components, other.components))
		return Vector(*components)

	def __sub__(self, other):
		if not self.validate_type_and_dimension(other):
			return NotImplemented
		components = (x - y for x,y in zip(self.components, other.components))
		return Vector(*components)

	def __mul__(self, other):
		print('__mul__ called..')
		if isinstance(other, Real):
			# scalar product
			components = (other * x for x in self.components)
			return Vector(*components)

		if self.validate_type_and_dimension(other):
			#dot-product
			components = (x * y for x,y in zip(self.components, other.components))
			return sum(components)
		# If other is neither Real nor vector of same dimension.
		return NotImplemented

	# usign existing __mul__() method
	def __rmul__(self, other):
		print('__rmul__ called..')
		return self * other

	# Cross-product
	def __matmul__(self, other):
		print('__matmul__ called..')

	def __iadd__(self, other):
		print('__iadd__ called..')
		if self.validate_type_and_dimension(other):
			components = (x + y for x,y in zip(self.components, other.components))
			# This time, we HAVE TO do tuple() because components at this moment is a 'generator' object.
			self._components = tuple(components)
			return self
		return NotImplemented

	def __neg__(self):
		print('__neg__ called..')
		components = (-x for x in self.components)
		return Vector(*components)

	def __abs__(self):
		return sqrt(sum(x **2 for x in self.components))

# Now we can create objects and test these..



'''
Rich Comparison:
	-> Less Than 			: 	__lt__ 	: < 
	-> Greater Than 		:	__gt__ 	: >
	-> Less Then Equal		: 	__le__  : <=
	-> Greater Than Equal	:	__ge__  : >=
	-> Equal				:	__eq__	: ==
	-> Not Equal			:	__ne__ 	: !=

If NotImplemented is returned: Python does the reflection. Eg: a.__lt__(b) returns NotImplemented, it will do b.__gt__(a)

Mostly, All the Rich Comparisions can be derived from 2 operations:
	if '==' and '<' is defined
		-> a <= b 	is 		a == b 	or 	a < b
		-> a > b 	is 		b < a
		-> a >= b 	is 		a == b 	or 	b < a
		-> a != b 	is 		not(a == b)

	if '==' and '<=' is defined
		-> a < b 	is 		a <= b 	and not(a == b)
		-> a > b 	is 		b <= a 	and not(a == b)
		-> a >= b 	is 		b <= a
		-> a != b 	is 		not(a == b)

functools.total_ordering
	-> This decorator adds all the rich-comparisons to the class if 2 of them are present in the class.
	
	** Documentation says that we don't have to.. But implementing '==' is good idea otherwise we can have unexpected behavior
		Eg:
			class Numbers has only '__lt__()'

			a = Number(1)
			b = Number(1)
			a == b   -> False (It is checking the address by default.)	
'''
from functools import total_ordering

@total_ordering
class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f'Vector(x={self.x}, y={self.y})'

	# until we implement '__eq__' method, Python will compare Addresses of operands instead of values.
	# So, v1==v2 for (v1=0,0 and v2=0,0) will be False
	# This will work for '__ne__'.. Because Python reflects if a certain operation is not implemented
	def __eq__(self, other):
		# Adding support for Tuple type objects
		if isinstance(other, tuple):
			other = Vector(*other)
		if isinstance(other, Vector):
			return self.x==other.x and self.y==other.y
		return NotImplemented

	# After using '@total_ordering' decorator, this is optional
	def __abs__(self):
		return sqrt(self.x **2 + self.y **2)

	# This will work for '__gt__' as well.. Because Python reflects if a certain operation is not implemented.
	def __lt__(self, other):
		# Adding support for Tuple type objects
		if isinstance(other, tuple):
			other = Vector(*other)
		if isinstance(other, Vector):
			return abs(self) < abs(other)
		return NotImplemented

	# This will work for '__ge__' as well.. Because Python reflects if a certain operation is not implemented.
	# After using '@total_ordering' decorator, this is optional
	def __le__(self, other):
		return self == other or self < other





