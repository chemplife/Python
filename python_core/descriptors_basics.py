'''
****************************** Go over 'properties_in_class.py' script first.. This concept will make more sense then.. *******************************


Descriptor Protocol: 4 methods to implement the protocol
	-> __get__: 					used to 'get' attribute value
	-> __set__: 					used to 'set' attribute value
	-> __delete__:					used to 'delete' attribute
	-> __set_name__	(python 3.6+):	called once when the Descriptor is Instantiated
									used to recover the name of the property to which the Descriptor Instance is assigned to in our class

@property: used the descriptor protocol.
	-> It is a convinience class that creates these 'Descriptor Classes' for us.

Why Custom Descriptors and not just use @property?
	-> @property will lead to a lot of repeated code if more than 1 similar attributes are involved.
		(It won't be a DRY code - "Don't Repeat Yourself" code)
		-> Eg: 2D-points: x and y both have to follow certain rules and if we use @property for x.setter()..
								we need to implement the same for y.setter()

2 Categories:
	-> Non-Data Descriptors:	Descriptors that only implement __get__		(Read-Only Property)
	-> Data-Descriptors:		Descriptors that implement __get__, __set__ / and-or / __delete__


#################################################################################################
# @property is a Data-Descriptors with
#	fget() -> __get__()
#	fset() -> __set__()
#
# If fset() is not defined.. It does not make the @property a Non-Data-Descriptor.
# @property still has __set__() implemented and absence of fset() will raise an 'AttributeError'
#################################################################################################
(You'll get it by the end of this script..)


1. __get__(self, instance, owner_class):
		-> self: instance of the descriptor class.
		-> instance: which instance is the __get__() method called from.
					-> If the __get__() method was called directly by a class and not any instance, instance = None
		-> owner_class: class which itself called __get__() method or whose 'instance' called __get__() method.

	Desired Flow:
		-> return the 'Descriptor Instance' when called from the class itself. (This provides the class, handle to the Descriptor instance.)
		-> then, return the 'attribute' value when called from an instance of the class.
		Eg:
			class TimeUTC:
				def __get__(self, instance, owner_class):

					# Called from the owner-class: Return the instance of the TimeUTC..
					if not instance:
						return self

					# Called from the instance of owner-class: Return the attribute value
					return datetime.utcnow().isoformat()


2. __set__(self, instance, value):
		-> self: instance of the descriptor class.
		-> instance: which instance is the __set__() method called from.
		-> value: value we want to assign to the attribute

	** Unlike, __get__(), __set__() is meant to be used as 'Instance Property'. So, we can only call it from the instance of the owner-class
		and the owner-class cannot call it directly.. That is why, there is no such thing as owner-class for __set__().


3. __set_name__(self, owner_class, property_name):
		-> self: instance of the descriptor class.
		-> owner_class: class which itself called __set_name__() method or whose 'instance' called __set_name__() method.
		-> property_name: owner_class property to which the Desciptor class instance is assigned to.


Problem:
	class Logger:
		current_time = TimeUTC()

	l1 = Logger()
	l2 = Logger()

	-> current_time is a class-attribute that holds the instance of TimeUTC() descriptor.
	-> l1 and l2 are instances that shares class-attributes, and in this case, they will share the same instance of TimeUTC().
		-> It is not an issue when we are just returning data (Non-Data Descriptors.)
		-> But can become a problem when dealing with Data-Descriptors, when we start storing data directly in the Descriptors..

Solution:
	__get__(), __set__(), and __delete__()
		-> They have 'instance' parameter. This instance parameter keeps track of which instance is accessing the data.
		-> Even though the descriptor-instance ('self') is shared, 'instance' parameter is different for the owner-class instances.

	(So, if we are storing the data directly in the descriptors, we need to use the 'instance' to make the stored-data instance specific..)
'''

# To check Reference Count
import ctypes
def ref_count(address):
	return ctypes.c_long.from_address(address).value


print('--------------------------- Non-Data Descriptors Example ---------------------------\n')

from datetime import datetime

# This is the Descriptor Class
class TimeUTC:
	def __get__(self, instance, owner_class):
		return f'Data: {datetime.utcnow().isoformat()}\nInstance: {instance}\nOwner-Class: {owner_class.__name__}'

class Logger:
	# Here, current_time is the instance of TimeUTC() class.
	# It was suppose to be bound to the Class Logger and not accessible to its Instances (like 'l' below)
	# But Implementation of Descriptor protocol make 'current_time' accessible to the 'instances' of Logger Class
	current_time = TimeUTC()

print('Logger Class Dict:', Logger.__dict__)
#This should always work..
print('\nLogger Class using TimeUTC Class instance:\n', Logger.current_time)

# This works only because of 'Descriptor Protocol'
l = Logger()
print('\nLogger Instance using TimeUTC class instance:\n', l.current_time)

#This works exactly like @property
class TimeUTC1:
	def __get__(self, instance, owner_class):

		# Called from the owner-class: Return the instance of the TimeUTC..
		if not instance:
			return self

		# Called from the instance of owner-class: Return the attribute value
		return datetime.utcnow().isoformat()

class Logger1:
	current_time = TimeUTC1()

class Logger2:
	@property
	def current_time(self):
		return datetime.utcnow().isoformat()


print('\nLogger1 Class using TimeUTC Class instance:\n', Logger1.current_time)

l = Logger1()
print('\nLogger1 Instance using TimeUTC class instance:\n', l.current_time)

print('\nLogger2 Class using @property:\n', Logger2.current_time)

l = Logger2()
print('\nLogger2 Instance using @property:\n', l.current_time)
	

print('\n\n--------------------------- Property and Descriptors ---------------------------\n')

print('----------------- Property -----------------\n')

from random import choice, seed

class Deck:
	@property
	def suit(self):
		return choice(('Spade', 'Heart', 'Diamond', 'Club'))

	@property
	def card(self):
		return choice(tuple('123456789JQKA') + ('10',))

# The probem above is the repeated code..
# both 'suit()' and 'card()' does the same thing: make random choice from a given Iterable.

d = Deck()
seed(0)
for _ in range(10):
	print(d.card, d.suit)


# Descriptors can be used to have 1 function and we can pass in the iterable we want to make the random choice from..
print('----------------- Descriptors -----------------\n')

# This is the Descriptor Class
class Choice:
	def __init__(self, *choices):
		self.choices = choices

	def __get__(self, instance, owner_class):
		return choice(self.choices)

class Deck:
	suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
	card = Choice(*'123456789JQKA', '10')


d = Deck()
seed(0)
for _ in range(10):
	print(d.card, d.suit)


'''
Data-Descriptors as Instance Properties:
Where to store Attribute Value?
	-> We could store them in the instance.__dict__.
		-> but while using __slots__, we might get into trouble because while using 'slots', __dict__ is not available for the instance.
''' 
print('\n\n--------------------------- Data-Descriptors as Instance Properties ---------------------------\n')

# Storing attribute Values on instance.__dict__:

# This will work but have drawbacks.
# 1. 2 times mentioning the attribute name.
# 2. If there is another place where the instance is using the same variable-name (_x), it will replace the value in the instance.__dict__
# 3. If Point2D is using slots, we can't have instance.__dict__.

class IntegerValue:
	def __init__(self, name):
		self.storage_name = '_'+name

	def __set__(self, instance, value):
		setattr(instance, self.storage_name, value)

	def __get__(self, instance, owner_class):
		if instance is None:
			return self
		return getattr(instance, self.storage_name, None)


class Point2D:
	# We have to pass the attribute name 2 times..
	x = IntegerValue('x')
	y = IntegerValue('y')

p1, p2 = Point2D(), Point2D()

p1.x = 10.1
p1.y = 20.2

p2.x = 100.2
p2.y = 200.2

print('Instance Dict: ', p1.__dict__)
print('Instance Dict: ', p2.__dict__)

print('\n')

# Storing instace attributes in the Descriptor.__dict__
# CAUTION:	The attribute_names need to be unique as per the Discripton.__dict__

# Assuming that we have 'slots' storage in Point2D and the class-objects are 'hashable' (otherwise they cannot be used as 'Keys')
# And in case we end up implementing '__eq__()' in the class, we need to implement '__hash__()' as well..

# Storing values in a dictionary {instance as Key: attribute Value as Value}
class IntegerValue:
	def __init__(self):
		self.values = {}

	def __set__(self, instance, value):
		self.values[instance] = int(value)

	def __get__(self, instance, owner_class):
		if instance is None:
			return self
		return self.values.get(instance, None)


class Point2D:
	x = IntegerValue()
	y = IntegerValue()

p1, p2 = Point2D(), Point2D()

p1.x = 10.1
p1.y = 20.2

p2.x = 100.2
p2.y = 200.2

# Get handle of Discriptor Class: Point2D.x or Point2D.y
print('Instance Dict: ', Point2D.x.values)
print('Instance Dict: ', Point2D.y.values)

# But there is a memory leak..
# The same Keys are present in both 'x.values' and 'y.values'
# So, even if the Class-Object goes out of scope, the Garbage-Collector cannot clear that memory
#	because the reference is still present in the 'values dictionary'

# This happens because we have been using 'STRONG REFERENCES' till this point.
# This problem can be solved using 'WEAK REFERENCES'


#####################################################################################
#
# Check-out 'strong_and_weak_reference.py' first before proceeding.
#
#####################################################################################


print('\n\n------------- Data-Descriptors as Instance Properties: Weak References -------------\n')

import weakref

class IntegerValue:
	def __init__(self):
		self.values = weakref.WeakKeyDictionary()

	def __set__(self, instance, value):
		self.values[instance] = int(value)

	def __get__(self, instance, owner_class):
		if instance is None:
			return self
		return self.values.get(instance, None)


class Point2D:
	x = IntegerValue()
	y = IntegerValue()

p1, p2 = Point2D(), Point2D()

p1.x = 10.1
p1.y = 20.2

p2.x = 100.2
p2.y = 200.2

# Get handle of Discriptor Class: Point2D.x or Point2D.y
print('Instance Dict: ', Point2D.x.values.keyrefs())
print('Instance Dict: ', Point2D.y.values.keyrefs())

# Everything is fine here, except that the class-objects need to be hashable.


'''
Instead of using Weak-References in Data-Descriptors, we can use 'id(instance)'
	-> id() is always hashable.
	-> No Strong References used as we are using the 'id' of the object.
	-> Drawback:	If an instance is Garbage-Collected, we will still have its 'id' in our data-dictionary.
				1. We might have data that is no longer usable.
				2. The 'id'-adress might have reused by the memory for something else, and we will have wrong assignment.


'''
print('\n\n------------- Data-Descriptors as Instance Properties: Final Approach -------------\n')
'''
We will use:

-> weakref.ref: It provides callback functionality (when an object is Garbage Collected, it runs a custom function to remove the weak references)
-> use regular Data Dictionary with
	-> Keys: 'id(instance)'
	-> Value: (weak_ref, value)
		-> each 'weak_ref' register a callback function, which removes the dead entries from the Data Dictionary.

Advantage:
	-> Using Instance Specific Storage in Descriptor Class (instance itself as storage won't work when using 'slots'.)
	-> Now, can handle non-hashable objects as well.
	-> Keep the data-storage mechanism clean.
'''

class IntegerValue:
	def __init__(self):
		self.values = {}

	def __set__(self, instance, value):
		self.values[id(instance)] = int(value)

	def __get__(self, instance, owner_class):
		if instance is None:
			return self
		return self.values.get(id(instance), None)


class Point2D:
	x = IntegerValue()
	y = IntegerValue()

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return isinstance(other, Point2D) and self.x == other.x and self.y == other.y


p1, p2 = Point2D(10.1, 20.2), Point2D(100.2, 200.4)

# But when p1 or p2 are deleted, we will still have these entries.
print('Instance Dict: ', Point2D.x.values)
print('Instance Dict: ', Point2D.y.values)
del p1

# Entries for p1 are still there even though p1 object is deleted.
print('Instance Dict: ', Point2D.x.values)
print('Instance Dict: ', Point2D.y.values)

print('\n')

# Syntax of a 'Live' weak_ref:	<weakref at 0x105f0e2c0; to 'Point2D' at 0x105efe1f0>
# Syntax of a 'Dead' weak_ref:	<weakref at {Memory Address}; dead>

class IntegerValue:
	def __init__(self):
		self.values = {}

	def __set__(self, instance, value):
		# self._remove_object: Callback function that will get called as soon as the 'weak_ref' goes 'Dead'..
		# Whatever we want to do when that happens, we can put it here. (Eg, delete entry from the 'values' dict.)
		self.values[id(instance)] = (weakref.ref(instance, self._remove_object), int(value))

	def __get__(self, instance, owner_class):
		if instance is None:
			return self
		else:
			# Now, this is safe to do. Since any strong reference to the instance is garbage collected
			# and the week reference will be dead, so we won't have any handle to the instance and will be able to call the __get__()
			# with that instance.
			value_tuple = self.values[id(instance)]
		return value_tuple[1]

	def _remove_object(self, weak_ref):
		# Problem is, when a weak_ref is dead, we don't have the handle to the address of the Strong-referenced object.
		# Because weak-ref goes dead when strong-ref is Garbage-Collected.
		# So, we have iterate over the dictionary to find the tuple with 'element 0' being 'dead'

		dead_ref_lookup = [key for key, value in self.values.items()
							if value[0] is weak_ref]

		if dead_ref_lookup:
			key = dead_ref_lookup[0]
			del self.values[key]

		# or this will work too
		# for key, value in self.values.items():
		# 	if value[0] is weak_ref:
		# 		del self.values[key]
		# 		break


class Point:
	x = IntegerValue()

p7 = Point()
p7.x = 10.1
id_p7 = id(p7)
print('Object-p value: ', p7.x)
print('Instance Dict: ', Point.x.values)
print('Reference count for p7: ', ref_count(id_p7))
del p7

print('Instance Dict: ', Point.x.values)
print('Reference count for p7: ', ref_count(id_p7))


print('\n\n------------- Weak Reference and Slots -------------\n')
# There is a problem though..
# When using 'slots'.. the '__weakref__' attribute is also gone for the Class and its object, the same way __dict__ goes away.

class Person:
	pass

p = Person()
print('__weakref__ for class:\t\t  ', Person.__weakref__)
print('__weakref__ for class-Object: ', p.__weakref__)


print('\n')

class Person:
	__slots__ = 'name',
	pass

p = Person()
print('__weakref__ for class:\t\t  ', hasattr(Person, '__weakref__'))
print('__weakref__ for class-Object: ', hasattr(Person, '__weakref__'))


print('\n')

class Person:
	# The same thing we did with '__dict__'
	__slots__ = 'name', '__weakref__'
	pass

p = Person()
print('__weakref__ for class:\t\t  ', Person.__weakref__)
print('__weakref__ for class-Object: ', p.__weakref__)

# Checking if the __weakref__ still a Descriptor itself.
print('__weakref__ has __get__?: ', hasattr(Person.__weakref__, '__get__'))
print('__weakref__ has __set__?: ', hasattr(Person.__weakref__, '__set__'))


print('\n\n------------------------------------------ __set_name__ ------------------------------------------\n')
'''
Going back to using the 'instance __dict__' to store the data instead of having a Data Dictionary in the Descriptor.

** called once when the Descriptor is Instantiated
** used to recover the name of the property to which the Descriptor Instance is assigned to in our class

3. __set_name__(self, owner_class, property_name):
		-> self: instance of the descriptor class.
		-> owner_class: class which itself called __set_name__() method or whose 'instance' called __set_name__() method.
		-> property_name: owner_class property to which the Desciptor class instance is assigned to.
'''

class ValidString:
	def __set_name__(self, owner_class, property_name):
		print(f'__set_name__ was called: owner_class = {owner_class} and property_name = {property_name}')

class Person:
	name_for_property_name = ValidString()


print('\n------- Taking this further-------\n')

class ValidString:
	def __set_name__(self, owner_class, property_name):
		print(f'__set_name__ was called: owner_class = {owner_class} and property_name = {property_name}')
		# It is ok to store the property_name in the Descriptor __dict__, because each instance of owner_class will be using it.
		self.property_name = property_name

	def __get__(self, instance, owner_class):
		if isinstance is None:
			return self
		print(f'__get__ called for property: {self.property_name}.. for instance: {instance}')


class Person:
	first_name = ValidString()
	last_name = ValidString()

# Now, the problem we had about storing attributes in Instance __dict__, where the same name for attribute will override the older value
# That problem is can be resolved because we can get the property_name from the Descriptor Instance for reference.
# And we don't have to pass the property_name as the parameter for Descriptor Instantiation.
# (Refer Code in line 190-210 of this script.)
# (Assuming that we are not using 'Slots')

print('\n------- Taking this even further-------\n')

# Here we will reference the class attribute in the Descriptor-Class to give out 'descriptive messages custom for each attribute'
class ValidString:
	def __init__(self, min_length=None):
		self.min_length = min_length

	def __set_name__(self, owner_class, property_name):
		self.property_name = property_name

	def __set__(self, instance, value):
		if not isinstance(value, str):
			raise ValueError(f'{self.property_name} must be a String.')
		if self.min_length is not None and len(value) < self.min_length:
			raise ValueError(
				f'{self.property_name} must be at least {self.min_length} characters.'
				)
		key = '_' + self.property_name
		setattr(instance, key, value)

	def __get__(self, instance, owner_class):
		if isinstance is None:
			return self
		key = '_' + self.property_name
		return getattr(instance, key, None)

# The override of attributes in instance __dict__ issue is still there..
class Person:
	first_name = ValidString(2)
	last_name = ValidString(2)

p = Person()

try:
	p.first_name = 'Alex'
	p.last_name = 'M'
except Exception as ex:
	print(ex)
print('Insance Dictionary:\t\t\t\t\t   ', p.__dict__)

p._first_name = 'I did not know this attribute_name was taken.. too bad.. for you..'
print('Insance Dictionary overriding Issue..: ', p.__dict__)

'''
Now, we can store 'self.property' directly in the 'Key' instead of " '_' + self.property_name".
	-> setattr(instance, self.property, value)
		will call __set__() again and make the function go infinite recursion.
	-> So we use the instance.__dict__ directly..
'''
print('\n')

class ValidString:
	def __init__(self, min_length=None):
		self.min_length = min_length

	def __set_name__(self, owner_class, property_name):
		self.property_name = property_name

	def __set__(self, instance, value):
		if not isinstance(value, str):
			raise ValueError(f'{self.property_name} must be a String.')
		if self.min_length is not None and len(value) < self.min_length:
			raise ValueError(
				f'{self.property_name} must be at least {self.min_length} characters.'
				)
		#Bypassing Descriptor completely and storing data directly in instance.__dict__
		instance.__dict__[self.property_name] = value

	def __get__(self, instance, owner_class):
		if isinstance is None:
			return self
		print('__get__ called..')
		return instance.__dict__.get(self.property_name, None)

class Person:
	first_name = ValidString(2)
	last_name = ValidString(2)

p = Person()

p.first_name = 'Alex'

print('Insance Dictionary:\t\t\t\t\t   ', p.__dict__)
print('is the __get__ called for getting the value of p.first_name or it will take directly from instance.__dict__?:')
print(p.first_name)
# Why did it go to the Descriptor when the value of 'first_name' was there in the in instance __dict__.. That is where Python looks first..
# And that is why anything in instance __dict__ shadows the same attribute_name present in class __dict__ (Definition of Overriding attributes..)


print('\n\n------------------------------------------ Property Value Lookup Resolution ------------------------------------------')
print('-------------------------------------------- Data Vs Non-Data Descriptors --------------------------------------------\n')
'''
class Descriptor:
	pass

class Owner:
	x = Descriptor()

owner = Owner()
owner.x = None

Now,
	class.__dict__	-> {x = something..}
	owner.__dict__		-> {x = None}

If we want to fetch -> owner.x 		where will it get from?
	-> from owner.__dict__
	-> from Descriptor's __get__() method.

It depends on:
	-> Descriptor is Non-Data or Data Descriptor.

		-> For Data-Descriptor:	(with both __get__ and (__set__ or __delete__))
			Descriptor __dict__ will ALWAYS OVERRIDE instance __dict__ (BY DEFAULT).. This can be changed but it is tricky..
			owner.x -> will go to __get__() method of descriptor.
			(To set any value):
				-> owner.y = 100					(will go to the __set__() method of the descriptor)
				-> owner.__dict__['y'] = 500		(will put the value directly in __dict__ of the instance.)
					-> But doing 'owner.y' -> 100	(because it calls __get__() method of descriptor)
					-> owner.__dict__['y'] -> 500

		-> For Non-Data-Descriptor: (with only __get__)
			Python will look in instance __dict__ first.. if the entry is not there, then it will it will look in Descriptor __dict__.
			owner.x -> will go to the instance.__dict__ (1st)..
					-> if instance.__dict__ is empty, __get__() method is called.
			(To set any value):
				-> owner.y = 100		(since __set__() is not implemented [Non-Data-Descriptor], it will update __dict__.)
'''

# Data Descriptor
class IntergerValue:
	def __get__(self, instance, owner_class):
		print('__get__ was called..')

	def __set__(self, instance, value):
		print('__set__ was called..')

class Point:
	x = IntergerValue()

p = Point()
print('Setting Value of x:')
p.x = 100
print('\nGetting Value of x:')
p.x
print('\nInstance dict: ', p.__dict__)
print('Manually entring x in p.__dict__')
p.__dict__['x'] = 'Hello'
print('Instance dict: ', p.__dict__)
print('\nGetting Value of x:')
p.x

print('\n')
# Non-Data Descriptor
class IntergerValue:
	def __get__(self, instance, owner_class):
		print('__get__ was called..')

class Point:
	x = IntergerValue()

p = Point()
print('Instance dict: ', p.__dict__)
print('Getting value of x:')
p.x
print('Setting Value of x:')
p.x = 100
print('Getting Value of x:', p.x)
print('Instance dict: ', p.__dict__)
print('Deleting entry from __dict__')
del p.x
print('Getting value of x:')
p.x

# So, in case of Data-Descriptors, where we need instance-based-storage, we can use the property_name itself to store the value in the instance
# under the same name.	(self.property_name used by instance to store data in __dict__)
# It will not shadow (override) the class attribute (the descriptor-instance)
# So, we have no risk of overriding any instance attribute our class may already have.
#
# Assuming, No 'Slots' being used.. or have '__dict__' in the 'Slots' if they are used.

print('\n------- Overriding instance __dict__ issue: RESOLVED -------\n')

# Original Code from Line 573
class ValidString:
	def __init__(self, min_length=None):
		self.min_length = min_length

	def __set_name__(self, owner_class, property_name):
		self.property_name = property_name

	def __set__(self, instance, value):
		if not isinstance(value, str):
			raise ValueError(f'{self.property_name} must be a String.')
		if self.min_length is not None and len(value) < self.min_length:
			raise ValueError(
				f'{self.property_name} must be at least {self.min_length} characters.'
				)
		#Bypassing Descriptor completely and storing data directly in instance.__dict__
		instance.__dict__[self.property_name] = value

	def __get__(self, instance, owner_class):
		if isinstance is None:
			return self
		print(f'__get__ called for {self.property_name}..')
		return instance.__dict__.get(self.property_name, None)

class Person:
	first_name = ValidString(2)

p = Person()
p.first_name = 'Alex'
print('Instance Dict:', p.__dict__)
# __get__ was called even thought the value is in instance.__dict__
print('Getting First_name:', p.first_name)


# Overriding instance __dict__ issue: RESOLVED..
# Add Code..


print('\n\n--------------------------- Property and Descriptors (More Detailed) ---------------------------\n')
######################################################################################
# @property is a Data-Descriptors with
#	fget() -> __get__()
#	fset() -> __set__()
#
# If fset() is not defined.. It does not make the @property a Non-Data-Descriptor.
# @property still has __set__() implemented and absence of fset() will raise an 'AttributeError'
######################################################################################

from numbers import Integral

class Person:

	# 'fget()' receives instance of 'age'					<- goes to __get__
	@property
	def age(self):
		return getattr(self, '_age', None)

	# 'fset()' received instance of 'age' and a 'value'		<- goes to __set__
	@age.setter
	def age(self, value):
		if not isinstance(value, Integral):
			raise ValueError('Age: must be an Integer number..')
		if value < 0:
			raise ValueError('Age: must be an Non-Zero number..')
		self._age = value

p = Person()

try:
	p.age = -10
except Exception as ex:
	print(ex)

print('Instance Dict:\t\t', p.__dict__)
p.age = 30
print('Instance Dict now:  ', p.__dict__)
# p.__dict__ has '_age' not 'age'


print('\n\n--------------------------- Functions and Descriptors ---------------------------\n')
'''
Functions are objects that implement the Non-Data Descriptor Protocol..
** That is how they become Methods that are bound to an class-instance when used inside a class.

** Method -> Function bound to an Instance 			(MethodType is in 'types' Module)
	-> m = types.MethodType(func_name, instance)
'''

import sys

me = sys.modules['__main__']

def add(a, b):
	return a + b

print('Does add() has __get__()?: ', hasattr(add, '__get__'))

f = add.__get__(None, me)
print('Is f() same as add()?: ', f is add)

print('\n')
class Person:
	def __init__(self, name):
		self.name = name

	def say_hello(self):
		return f'Say Hello to {self.name}'

# Since the say_hello() is called from Class Person
# the __get__ of say_hello() got
#	-> instance = None 		(Because there is no Instance.. we called directly from class)
#	-> owner_class = Person
print('Call function from class: ', Person.say_hello)

p = Person('Alex')
# This time, the instance = 'p' and not None
print('Call function from class-object: ', p.say_hello)

#It is same as
bound_method = Person.say_hello.__get__(p, Person)
print('Bound Method: ', bound_method)
print('Is Bound_Method same as p.say_hello?: ', bound_method == p.say_hello)

# say_hello() is a function in class Person, but when used with an Instance, it returns a 'Method' Object.
# How does the 'Method' know which function to call when the Method is actually called?
# Ans: There is an attribute in Method-Objects called '__func__'
# and it reference the exact function to be called by the Method.
print('Bound_Method Function tracking: ', bound_method.__func__,'\nwhich is same as p.say_hello:\t', p.say_hello.__func__)