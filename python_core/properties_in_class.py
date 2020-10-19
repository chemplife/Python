'''
Property:
	-> Type = Class
	-> Its constructor has few parameters
		-> fget = function to use to 'get' instance property value
		-> fset = function to use to 'set' instance property value
		-> fdel = function to use to 'delete' instance property value
		-> doc = allw to specify docstring for that property/function of the instance

We can start with 'plain' attributes but in future, if we need to implement function to use those attributes,
we can use 'Property' inside the class.

** fdel will only delete the attribute for that instance. It won't delete the attribute from the Class Namespace

** This change will not effect the implementation of code outside of the class. Makes this backword-compatible

** Without Property,
	-> we need to call 'get_language' and 'set_language' functions manually,
	-> obj._attribute_names will give an error

NOTE: obj._attribute_name is still accessible to the outside code.
'''

# Class with 'plain' attributes and no Property
class Person_1:
	def __init__(self, language):
		self.language = language

# Class without 'plain' attributes and have Property
class Person_2:
	def __init__(self, language):
		self._language = language
	
	def get_language(self):
		print('Access Granted..')
		return self._language

	def set_language(self, value):
		print('Performing Checkes on provided Value.. like if it is a string or not..')
		self._language = value

	'''
	Now, 'language' is an attribute of instance, but for 'Person_2' class, it is a property object.
	The moment obj.langugae is executed, will come to this part of the code and Python will make the
		call the function (fget or fset) and execute that code.

	Since, Python does not have 'Private variables', this prevents external code to 'DIRECTLY' access
		the attributes.
	'''
	language = property(fget=get_language, fset=set_language)

p1 = Person_1('Python')
print('Direct access to attribute:', p1.language)
p1.language = 'Python3'
print('Direct access to change attribute:', p1.language)
print('p1 namespace:', p1.__dict__)

print('\n')

p2 = Person_2('Java')
print('Direct access to attribute?:', p2.language)
p2.language = 'Java 8'
print('Direct access to change attribute?:', p2.language)
# 'language' is not even in the 'Obj Namespace', unlike p1
# So, Python looks for 'language' in the 'Class Namespace',
# and finds 'language' which is a 'Property Object' and uses the 'fget' and 'fset' depending on the operation we want to do.
print('p2 namespace:', p2.__dict__)

# Obj.__dict__ , the namespace is 'dict' type and is mutable (unlike Class Namespace, which is not.)
p2.__dict__['language'] = 'My_own_Language'
print('p2 namespace:', p2.__dict__)

# Even though, 'language' is now in the Obj namespace, 'property object'-> language is still going to run
print('p2.langugae: ', p2.language)


print('\n\n---------------------------------- Ways to define Property ----------------------------------')
'''
There are Class-Defined-Methods: 'getter', 'setter', 'deleter'
	-> : takes a callable as argument and returns a 'Property Object' with the 'getter'
				defined to whatever we specified as argument to the getter method.

These allow to put 'fget', 'fset', 'fdel' methods on the Property itself.

Instead of:
	-> x = property(fget=get_x, fset=set_x)
we can do:
	-> x = property()
	# This 'x.getter' will return a property that will have the 'getter' set to 'get_x'
	-> x = x.getter(get_x)
	-> x = x.setter(set_x)

we can also do,
	x = property(get_x)			-> Python knows that get_x is 'getter'.
'''
class MyClass_1:
	def __init__(self, language):
		self._language = language

	# This is our 'getter' now.
	def language(self):
		return self._language

	# This is exactly how Decorators work. To refresh it: 'scopes_namespace_closure_decorators.py'
	# func_name = Function(func_name)
	# 	-> pass funntion 'func_name' to another 'Function' and returned function 'func_name' get reassigned to the same value 'func_name'
	language = property(language)

# So, it can written as
class MyClass_2:
	def __init__(self, language):
		self._language = language

	@property
	def language(self):
		return self._language

	# Now to define a 'setter'
	def set_language(self, value):
		self._language = value
	# But we need to assign it to the 'language' property.
	# so,
	language = language.setter(set_language)
	# But this looks like a decorator too.

# So, again, it can written as
class MyClass_3:
	def __init__(self, language):
		self._language = language

	@property
	def language(self):
		'''the doc string for 'language' property..'''
		return self._language

	# We need to use the same name 'langauge' for the function
	@language.setter
	def language(self, value):
		'''the doc string won't show..'''
		self._language = value

	# Now, we have our property-object 'language' to be used, like the way we did earlier.

# Property as decorator can have 'docstring' in the 'getter' method, but not in 'setter' method

# Creating a write-only object.. Only 'setter', no 'getter'...
class MyClass_4_1:
	def __init__(self, language):
		self._language = language

	language = property(doc='This is a write-only property')

	@language.setter
	def language(self, value):
		'''the doc string won't show..'''
		self._language = value

class MyClass_4_2:
	def __init__(self, language):
		self._language = language

	def set_language(self, value):
		self._language = value

	language = property(fset=set_language)


# Creating a read-only object.. Only 'getter', no 'setter'...
class MyClass_5_1:
	def __init__(self, language):
		self._language = language

	@property
	def language(self):
		'''the doc string for 'language' property..'''
		return self._language

class MyClass_5_2:
	def __init__(self, language):
		self._language = language

	def get_language(self):
		return self._language

	language = property(fget=get_language)


print('\n\n---------------------------------- Read-only and Computed Property ----------------------------------')

from math import pi

class Circle:
	def __init__(self, radius):
		self.radius = radius

	# Because of @property, c.area() -> c.area 		-> Area() becomes a property rather than being a method
	@property
	def area(self):
		print('Calculating area')
		return pi*(self.radius**2)

c = Circle(2)
print('Radius Of Circle and Area: ', c.radius, "\t", c.area)

# But now, each time area is going to get recalculated everytime.
# so we need to calculate the area only if radius changes.
class Circle:
	def __init__(self, radius):
		self._radius = radius

		# This will store cache of already calculated areas of different raduis
		self._area = None

	# Because of @property, c.area() -> c.area 		-> Area() becomes a property rather than being a method
	@property
	def radius(self):
		return self._radius

	@radius.setter
	def radius(self, value):
		# When the radius is set, we clear the cache
		self._area = None
		self._radius = value

	@property
	def area(self):
		if self._area == None:
			print('Calculating area')
			# Keep the self.radius instead of self._radius						************************************
			# This will take the value from our radius-property					************************************
			self._area = pi*(self.radius**2)
		return self._area

c = Circle(2)
print('Radius Of Circle and Area: ', c.radius, "\t", c.area)
# It will not recalculate Area
print('Again the same Circle and Area: ', c.radius, "\t", c.area)