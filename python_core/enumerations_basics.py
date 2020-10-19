'''
PEP 435 and Python 3.4+
enum Module
	-> Enum Type is the most important one.

class Color(enum):
	RED = 1
	GREEN = 2
	BLUE = 3

	-> Class 'Color' is called as an 'enumeration'
	-> Color.RED is called as 'Enumeration Member'
	-> Members have associated values, like 1,2,3 here.
	-> 'type' of a member is the 'enumeration' it belongs to
		-> RED (being an attribute of class 'Color') here points to the instance of class-Color
			-> type(Color.RED) 				==> Color
			-> isinstance(Color.RED, Color)	==> True

		New Things available:
			-> Color.RED.name 	==> 'RED'
			-> Color.RED.value 	==> 1

			-> Color.RED == 1	==> False 	(Color.RED is an instance of class-Color and '1' is an instance of int())

	-> Enumeration Members should be 'UNIQUE'	(Even the Values..)
		-> But when the values are not 'Unique' among Enumeration Members, 'Alias' is at play.. [Check Alias_basic.py script.]

	-> Enumeration Members are always HASHABLE.
		-> unless we override __eq__() method.

	-> Enumerations are callable
		-> Color(2)		==> Color.GREEN
			-> We can use the 'value' to find out which Enumeration Member holds it.

	-> Enumeration implements __getitem__ method.
		-> Color['GREEN']				==> Color.GREEN
		-> Color(2) == Color['GREEN']	==> True

	-> Enumerations are 'Iterables'
		-> list(Color)	==> [Color.RED, Color.GREEN, Color.BLUE]

	-> 'Definition order is preserved'.

	-> Enumeration has a '__members__' property
		-> returns a 'Mapping Proxy', which is an Immutable Dict.
			-> Keys		= Member Names
			-> Values 	= Value

** Once the Enumeration is declared:
	-> Members list is immutable:						Cannot add more Members
	-> Values are immutable:							Cannot assign a different value to the members.
		-> If the Value is a mutable type, then the value can be mutated.. but some other value cannot be assigned
	-> Cannot be subclassed (extended via inheritance):	Cannot make this class a parent class.. unless there is No Member inside it.
'''

import enum
from collections.abc import Iterable

class Status(enum.Enum):
	PENDING = 'pending'
	RUNNING = 'running'
	COMPLETED = 'completed'

print('Type of class attribute:\t\t\t\t\t\t\t\t\t', type(Status.PENDING))
print('Is class attribute an instance of class here?:\t\t\t\t', isinstance(Status.PENDING, Status))
print('Are Enumerations Callable:\t\t\t\t\t\t\t\t\t', callable(Status))
print('Is Enumeration class <Status> an Iterable?:\t\t\t\t\t', isinstance(Status, Iterable))
# hasattr(Status, '__iter__')		-> will also work
print('Is COMPLETED in Status?:\t\t\t\t\t\t\t\t\t', Status.COMPLETED in Status)
print('Call Enumeration Member by value:\t\t\t\t\t\t\t', Status('running').name)
print('Other Properties of Enumeration Members: name = ', Status.PENDING.name,", value = ",Status.PENDING.value)
print('Print Status Class Enumeration Members as list:\t\t\t\t', list(Status))
print('__members__: ', Status.__members__)
print('Is __members__ values same as Enumeration Members:\t\t\t', Status.__members__['PENDING'] is Status.PENDING)

print('\n')

# __getitem__ Revisit
# obj[key]	-> calls the __getitem__()
class Person:
	def __getitem__(self, val):
		return f'__getitem__({val}) is called..'

p = Person()
print('GetItem call: ', p['Test'])

print('Get value by __getitem__: ', Status['PENDING'])

# Enumerations are immutable.. and the values cannot be changed either.
# Enumerations are immutable..
print('\n')
try:
	Status['New'] = 'new status'
except Exception as ex:
	print('Exception while mutating Enumeration: ', ex)

# Enumeration Member's values cannot be changed..
try:
	Status.PENDING.value = 'In Progress'
except Exception as ex:
	print('Exception while change value of Enumeration Member: ', ex)

print('\n')
# Cannot Subclass (extend or inheritance) if there is a member
class Test1(enum.Enum):
	pass

class Test2(enum.Enum):
	X = 1

try:
	class Test1_1(Test1):
		Y = 2
except Exception as ex:
	print('Got Exception while subclassing TEST1 Enumeration: ', ex)

try:
	class Test2_1(Test2):
		Y = 2
except Exception as ex:
	print('Got Exception while subclassing TEST2 Enumeration: ', ex)


print('\n\n---------------------------------------- Customizing / Extending Enums ----------------------------------------\n')
'''
Enumerations are classes with its attributes being its instances.
We can implement methods in Enumerations as they are still classes.
'''
print('------------------- Customizing Enums -------------------\n')
# By Default, every member of Enum is Truthy
class State(enum.Enum):
	Ready = 1
	Busy = 0

print('Truthy Value of Ready: ', bool(State.Ready))
print('Truthy Value of Busy: ', bool(State.Busy))

# To make use of the Truthy value of Busy = 0, we need to implement a Method in Enumeration
class State(enum.Enum):
	Ready = 1
	Busy = 0

	def __bool__(self):
		# self.value -> Attributes are instances in Enum..
		return bool(self.value)

print('\nTruthy Value of Ready: ', bool(State.Ready))
print('Truthy Value of Busy: ', bool(State.Busy))

class Color(enum.Enum):
	red = 1
	green = 2
	blue = 3

	def purecolor(self, value):
		return {self: value}

	def __repr__(self):
		return f'{self}->{self.value}'

Color.red.purecolor(255)
Color.green.purecolor(255)
Color.blue.purecolor(255)

print('\nEnumeration Members: ', list(Color))

from functools import total_ordering

@total_ordering
class Phase(enum.Enum):
	READY = 'Ready'
	RUNNING = 'Running'
	FINISHED = 'Finished'

	def __str__(self):
		return self.value

	def __eq__(self, other):
		if isinstance(other, Phase):
			return self is other
		elif isinstance(other, str):
			return self.value == other
		return False

	def __lt__(self, other):
		ordered_items = list(Phase)
		self_order_index = ordered_items.index(self)

		if isinstance(other, Phase):
			other_order_index = ordered_items.index(other)
			return self_order_index < other_order_index

		if isinstance(other, str):
			try:
				other_member = Phase(other)
				other_order_index = ordered_items.index(other_member)
				return self_order_index < other_order_index
			except ValueError:
				return False

print('\nEnum Members: ', Phase.READY)
print('Ordering based on Members: ', Phase.READY < Phase.RUNNING)
print('Ordering based on String: ', Phase.READY < 'Running')


print('\n------------------- Extending Enums -------------------\n')
'''
Any Child class of Enum class is going to be Enum class as well.. Obviously..

Enum class with Members cannot be extended.. But we can have methods in Enum class and extend that with Child class bringing in Members..
** We can use the Enum class as Base Class to implement various functionalities which is used by many Child Classes.
'''
class ColorBase(enum.Enum):
	
	def hello(self):
		return f'({self.name}) says Hello!'

class Color(ColorBase):
	RED = 'red'
	GREEN = 'green'
	BLUE = 'blue'

# hello() here is a bound Method..
print('Extended Enum class with bound method:', Color.RED.hello)
print('Extended Enum class bound method call:', Color.RED.hello())

print('\n------------------- Extending Enums with HTTP -------------------\n')

from http import HTTPStatus

print('Type of HTTPStatus: ', type(HTTPStatus))
print('List of HTTPStatus Instances: ', list(HTTPStatus))
print('\nSome of the Names from Values:')
print(HTTPStatus(400))
print(HTTPStatus(205))
print(HTTPStatus(300))
print(HTTPStatus(500))
print(f'\nFor Not_Found-\nName= {HTTPStatus.NOT_FOUND.name},\nValue= {HTTPStatus.NOT_FOUND.value},\nPhrase= {HTTPStatus.NOT_FOUND.phrase}')

print('\n')
# Implementing similar Behavior
class AppStatus(enum.Enum):
	OK = (0, 'No Problem!')
	FAILED = (1, 'Oh, Crap!')

print('Value of Members: ', AppStatus.OK.value)
# it is a tuple
print('Getting each value from the value-tuple: ', AppStatus.OK.value[0], '\t', AppStatus.OK.value[1])

#To make it more user-friendly.
class AppStatus(enum.Enum):
	OK = (0, 'No Problem!')
	FAILED = (1, 'Oh, Crap!')

	@property
	def code(self):
		return self.value[0]

	@property
	def phrase(self):
		return self.value[1]

print(f'Getting each value-\t\tname: {AppStatus.OK.name},\tcode: {AppStatus.OK.code},\tphrase: {AppStatus.OK.phrase}')
# But the call-by-value will not work
# print('Getting Member by value: ', AppStatus(0))

class AppStatus(enum.Enum):
	OK = (0, 'No Problem!')
	FAILED = (1, 'Oh, Crap!')

	# Overriding the Instance creation step (__new__())
	# This will create the Instance with distinctions between the 'value' and 'Phrase' at the time of
	# intance creation.
	def __new__(cls, member_value, member_phrase):
		# Now, we need an instance of the class for which we need to put together the value and phrase for..
		member = object.__new__(cls)

		member._value_ = member_value
		member.phrase = member_phrase

		# __new__ creates and return the instance.. Here instance is 'member'
		return member

print(f'\nGetting each value-\t\tname: {AppStatus.OK.name},\tvalue: {AppStatus.OK.value},\tphrase: {AppStatus.OK.phrase}')
print('Getting Member by value: ', AppStatus(0))

# Making the Overriden as General Enum..
class TwoValueEnums(enum.Enum):
	def __new__(cls, member_value, member_phrase):
		member = object.__new__(cls)
		member._value_ = member_value
		member.phrase = member_phrase
		return member

class AppStatus(TwoValueEnums):
	OK = (0, 'No Problem!')
	FAILED = (1, 'Oh, Crap!')

print(f'\nGetting each value-\t\tname: {AppStatus.FAILED.name},\tvalue: {AppStatus.FAILED.value},\tphrase: {AppStatus.FAILED.phrase}')
print('Getting Member by value: ', AppStatus(1))


print('\n\n---------------------------------------- Automatic Values ----------------------------------------\n')
'''
Python 3.6+

Python assign values automatically to our Enumerations
uses: enum.auto()
	-> enum.auto() uses '_generate_next_value_()' method of Enum class
	-> generated auto-values are of 'int()' type.

_generate_next_value_(name, start, count, last_values)
	-> Static Method (so, class or instance is not the first argument..)
	-> called by enum.auto()
	
	Arguments:
	-> name: 		name of the Enumeration Member.
	-> start: 		used in functional creation.. (Not used often)
					-> Enumerations can be created using 'functions' as well (not only Class)..
						-> Pass values for the 'member names', 'member value' to _generate_next_value_() function and it will create an Enumeration
	-> count:		Number of members that are already been created (including Aliases)..
	-> last_values:	List of all the previous values of the Enumeration Members.
	** This list keeps on growing each time 'auto()' is called.
	
	Returns:		value to be assigned to the Member.

** We can override the _generate_next_value_() function..
'''

class State(enum.Enum):
	WAITING = enum.auto()
	STARTED = enum.auto()
	FINISHED = enum.auto()

for member in State:
	print(f'Member Name: {member.name}\tMember Value: {member.value}')

print('\n')
# Now, this might/might-not work the same way.. so don't rely on this behavior
class State(enum.Enum):
	WAITING = 100
	STARTED = enum.auto()
	FINISHED = enum.auto()

for member in State:
	print(f'Member Name: {member.name}\tMember Value: {member.value}')

print('\n')
# Example where it can cause problem..
class State(enum.Enum):
	WAITING = enum.auto()
	STARTED = 1
	FINISHED = enum.auto()

for member in State:
	print(f'Member Name: {member.name}\tMember Value: {member.value}')

#State.STARTED is an Alias now.. @enum.unique will catch the problem, but will not fix it..
print('Members: ', State.__members__)

print('\n------------------- Custom _generate_next_value_() -------------------\n')

import random

random.seed(0)

class State(enum.Enum):
	def _generate_next_value_(name, start, count, last_values):
		while True:
			new_value = random.randint(1, 100)
			if new_value not in last_values:
				return new_value

	a = enum.auto()
	b = enum.auto()
	c = enum.auto()
	d = enum.auto()

for member in State:
	print(f'Member Name: {member.name}\tMember Value: {member.value}')


print('\n------------ Usecase 1: Excase Repeating ------------\n')

class State(enum.Enum):
	def _generate_next_value_(name, start, count, last_values):
		return name.title()

	WAITING = enum.auto()
	STARTED = enum.auto()
	RUNNING = enum.auto()
	FINISHED = enum.auto()

for member in State:
	print(f'Member Name: {member.name}\tMember Value: {member.value}')

print('\nOR\n')

class NameAsValue(enum.Enum):
	def _generate_next_value_(name, start, count, last_values):
		return name.title()

class State(NameAsValue):
	WAITING = enum.auto()
	STARTED = enum.auto()
	RUNNING = enum.auto()
	FINISHED = enum.auto()

class Status(NameAsValue):
	READY = enum.auto()
	SET = enum.auto()
	GO = enum.auto()
		

for member in State:
	print(f'Member Name: {member.name}\tMember Value: {member.value}')
for member in Status:
	print(f'Member Name: {member.name}\tMember Value: {member.value}')

print('\n')
# If the member.values are meaningless and we don't want others to use them as replacement of using member name..
class State(enum.Enum):
	'''Member Values are meaningless and subject to change in future..'''
	WAITING = 1
	STARTED = 2
	RUNNING = 3
	FINISHED = 4
#imagine a system that uses these states as input and people are doing this..
print('State name: ', State(1))

# Make the values go away..
class State(enum.Enum):
	'''Member Values are meaningless and subject to change in future..'''
	WAITING = object()
	STARTED = object()
	RUNNING = object()
	FINISHED = object()
#imagine a system that uses these states as input and people are doing this..
print('State Waiting: ', State.WAITING)

print('\n------------ Usecase 1: Creating Aliases ------------\n')

class Aliased(enum.Enum):
	def _generate_next_value_(name, start, count, last_values):
		return last_values[-1]

class Color(Aliased):
	RED = object()
	CRIMSON = enum.auto()
	CARMINE = enum.auto()

	BLUE = object()
	VIOLET = enum.auto()
	AZURE = enum.auto()

print('All Members: ', Color.__members__)
print('Master Members: ', list(Color))
