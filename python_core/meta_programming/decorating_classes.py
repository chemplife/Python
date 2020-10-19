'''
Decorating a function:

@my_dec								def my_func():
def my_func():			-->				pass
	pass
									my_func = my_dec(my_func)


Decorating a CLASS:

@my_dec								class MyClass():
class MyClass():		-->				pass
	pass
									MyClass = my_dec(MyClass)

Like Decorator returns the same function but a little tweaked (added functionality)
the same way, a Decorator can return a class by a little tweaked (added functionality)
	-> Kind of what we can do using Metaclass..

** A 'Decorator' can be used to do what we plan to use a 'Metaclass' for.. And when possible, we should use 'Decorators' instead of 'Metaclass'..
	-> It is easy to read
	-> Less complications

Eg:
def savings_account(cls):
	cls.account_type = 'Savings'
	return cls

@savings_account
class BankAccount:
	def __init__(self, account_number, balance):
		self.account_number = account_number
		self.balance = balance

--> This is same as
class BankAccount:
	def __init__(self, account_number, balance):
		self.account_number = account_number
		self.balance = balance

BankAccount = savings_account(BankAccount)

-> Class is created first and then Decorated.


We can parameterize the Decorator as well:
Eg:
def apr(rate):
	def inner(cls):
		cls.apr = rate
		cls.apy = ...
		return cls
	return inner

@apr(0.2)
class SavingsAccount:
	pass

@apr(0.0)
class CheckingsAccount:
	pass
'''

def savings(cls):
	cls.account_type = 'savings'
	return cls

def checkings(cls):
	cls.account_type = 'checkings'
	return cls

class Account:
	pass

@savings
class SavingsAccount(Account):
	pass

@checkings
class CheckingsAccount(Account):
	pass

print('Namespace of SavingsAccount: ', SavingsAccount.__dict__)
print('Namespace of CheckingsAccount: ', CheckingsAccount.__dict__)

print('\n')
# now, we don't want multiple decorators for each account-type
# So, we can use Parameterized decorator
def account_type(type_):
	def type_decor(cls):
		cls.account_type = type_
		return cls
	return type_decor

@account_type('savings')
class SavingsAccount(Account):
	pass

@account_type('checkings')
class CheckingsAccount(Account):
	pass

print('Namespace of SavingsAccount: ', SavingsAccount.__dict__)
print('Namespace of CheckingsAccount: ', CheckingsAccount.__dict__)

print('\n')
#Injecting functions in the class using Decorators

def hello(cls):
	cls.hello = lambda self: f'{self} says hello!'
	return cls

@hello
class Person:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

print('Namespace of Person Class: ', vars(Person))

print('\n\n------------------------ Example 1: Logging every call made to a callable ------------------------\n')
# Old style
from functools import wraps

def func_logger(fn):
	@wraps(fn)
	def inner(*args, **kwargs):
		result = fn(*args, **kwargs)
		print(f'Log: {fn.__qualname__}({args}, {kwargs}) = {result}')
		return result
	return inner

class Person:
	@func_logger
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@func_logger
	def greet(self):
		return f'Hello, my name is {self.name}, and my age is {self.age}'

p = Person('John', 78)
p.greet()

print('\n')
# But if we have a lot of methods, we have to write the 'func_logger' on top of each of them
# We can have a class decorator that will do the same for each method it has, without us having to mention it on top of each method..
def class_decorator(cls):
	for name, obj in vars(cls).items():
		if callable(obj):
			print('Decorating: ', cls, name)
			setattr(cls, name, func_logger(obj))
	return cls

@class_decorator
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def greet(self):
		return f'Hello, my name is {self.name}, and my age is {self.age}'

# by this time, the __init__() and greet() methods are already replaced with the Decorated versions of them..
# Decorating Class happens right after class creation.. and, class instances comes after this is done..
p = Person('John', 78)
p.greet()

print('\n\n------------------------ Class Decorators only work for instance methods ------------------------\n')

@class_decorator
class Person:
	@staticmethod
	def static_method():
		pass

	@classmethod
	def cls_method():
		pass

	def instance_method():
		pass

# Decorator only called by instance_method.
# Because static and class methods are of 'Descriptor' type.. They fail the 'if callable(obj):' check..
print('Is staticmethod callable: ', callable(Person.__dict__['static_method']))
print('Is classmethod callable: ', callable(Person.__dict__['cls_method']))

# To decorate the Static and Class methods, we need to do so before they become 'Descriptor' Objects
# Way-1
@class_decorator
class Person:
	@staticmethod
	@func_logger
	def static_method():
		pass

	@classmethod
	@func_logger
	def cls_method():
		pass

	def instance_method():
		pass

print('\n')
# Way-2
print('Type of Static Methods:', type(Person.__dict__['static_method']))
print('Type of Class Methods:', type(Person.__dict__['cls_method']))
print('Reaching the underlying function for Static and Class Methods: ', Person.__dict__['cls_method'].__func__)

# So, we can decorate the underlying function and put it back..
print('\n')
def class_decorator(cls):
	for name, obj in vars(cls).items():
		if callable(obj):
			print('Decorating Instance methods: ', cls, name)
			original_func = obj
			decorated_func = func_logger(original_func)
			setattr(cls, name, decorated_func)

		elif isinstance(obj, staticmethod):
			print('Decorating Static methods: ', cls, name)
			original_func = obj.__func__
			decorated_func = func_logger(original_func)
			method = staticmethod(decorated_func)
			setattr(cls, name, method)

		elif isinstance(obj, classmethod):
			print('Decorating Class methods: ', cls, name)
			original_func = obj.__func__
			decorated_func = func_logger(original_func)
			method = classmethod(decorated_func)
			setattr(cls, name, method)

	return cls

@class_decorator
class Person:
	@staticmethod
	def static_method():
		print('Static Method Called..')

	@classmethod
	def cls_method():
		print('Class Method Called..')

	def instance_method():
		print('Instance Method Called..')

# Now, each of these will get decorated..
print('Calling Static Method: ', Person.static_method)
print('Calling Class Method: ', Person.cls_method)
print('Calling Instance Method: ', Person.instance_method)

# property-> This will not get decorated at this point
# isinstance(obj, property) -> true
# to get to underlying function we use fget, fset, fdel..
print('\n')
def class_decorator(cls):
	for name, obj in vars(cls).items():
		if callable(obj):
			print('Decorating Instance methods: ', cls, name)
			original_func = obj
			decorated_func = func_logger(original_func)
			setattr(cls, name, decorated_func)

		elif isinstance(obj, staticmethod):
			print('Decorating Static methods: ', cls, name)
			original_func = obj.__func__
			decorated_func = func_logger(original_func)
			method = staticmethod(decorated_func)
			setattr(cls, name, method)

		elif isinstance(obj, classmethod):
			print('Decorating Class methods: ', cls, name)
			original_func = obj.__func__
			decorated_func = func_logger(original_func)
			method = classmethod(decorated_func)
			setattr(cls, name, method)

		elif isinstance(obj, property):
			print('Decorating property: ', cls, name)
			if obj.fget:
				obj = obj.getter(func_logger(obj.fget))
			if obj.fset:
				obj = obj.setter(func_logger(obj.fset))
			if obj.fdel:
				obj = obj.deleter(func_logger(obj.fdel))
			setattr(cls, name, obj)
			# at each 'if' statement, the 'obj' is the decorated 'obj' from the previous step.

	return cls

@class_decorator
class Person:
	def __init__(self, name):
		self._name = name

	@property
	def name(self):
		return self._name

p = Person('Alex')
# This will print the log
print('What is the name function now: ', p.name)

# But since Classes and its callable-objects are also callable, this can cause a problem
print('\n')
@class_decorator
class Person:
	class Other:
		def __call__(self):
			print('Called instance of Other..')
	other = Other()

print('Type of Class Other:  ', type(Person.Other))
print('Type of object other: ', type(Person.other))
# This happened because the callables got replaced by what was returned by the decorator.
# So, we need to restrict our decorator from using all 'callables'.. as 'callable' is very broad..
print('\n\n')


import inspect

class MyClass:
	@staticmethod
	def static_method():
		pass

	@classmethod
	def cls_method():
		pass

	def instance_method():
		pass

	@property
	def name(self):
		return self._name

	def __add__(self, other):
		pass

	class Other:
		def __call__(self):
			print('Called instance of Other..')
	other = Other()


# We want to decorate every callable except: class Other and its object 'other'
keys = ('static_method', 'cls_method', 'instance_method', 'name', '__add__', 'Other', 'other')
inspect_funcs = ('isroutine', 'ismethod', 'isfunction', 'isbuiltin', 'ismethoddescriptor')

max_header_length = max(len(key) for key in keys)
max_fname_length = max(len(func) for func in inspect_funcs)
print(format('', f'{max_fname_length}s'), '\t'.join(format(key, f'{max_header_length}s') for key in keys))
for inspect_func in inspect_funcs:
	fn = getattr(inspect, inspect_func)
	inspect_results = (format(str(fn(MyClass.__dict__[key])), f'{max_header_length}s') for key in keys)
	print(format(inspect_func, f'{max_fname_length}s'), '\t'.join(inspect_results))

def class_decorator(cls):
	for name, obj in vars(cls).items():
		if isinstance(obj, staticmethod):
			print('Decorating Static methods: ', cls, name)
			original_func = obj.__func__
			decorated_func = func_logger(original_func)
			method = staticmethod(decorated_func)
			setattr(cls, name, method)

		elif isinstance(obj, classmethod):
			print('Decorating Class methods: ', cls, name)
			original_func = obj.__func__
			decorated_func = func_logger(original_func)
			method = classmethod(decorated_func)
			setattr(cls, name, method)

		elif isinstance(obj, property):
			print('Decorating property: ', cls, name)
			if obj.fget:
				obj = obj.getter(func_logger(obj.fget))
			if obj.fset:
				obj = obj.setter(func_logger(obj.fset))
			if obj.fdel:
				obj = obj.deleter(func_logger(obj.fdel))
			setattr(cls, name, obj)
			# at each 'if' statement, the 'obj' is the decorated 'obj' from the previous step.

		elif inspect.isroutine(obj):
			print('Decorating all routine types: ', cls, name)
			original_func = obj
			decorated_func = func_logger(original_func)
			setattr(cls, name, decorated_func)

	return cls

print('\n')

@class_decorator
class MyClass:
	@staticmethod
	def static_method():
		pass

	@classmethod
	def cls_method():
		pass

	def instance_method():
		pass

	@property
	def name(self):
		return self._name

	def __add__(self, other):
		pass

	# This will decorate any callables that fits our criteria inside this class.
	@class_decorator
	class Other:
		def __call__(self):
			print('Called instance of Other..')
	other = Other()

# Refactoring Class_decorator()
def class_decorator(cls):
	for name, obj in vars(cls).items():
		if isinstance(obj, staticmethod) or isinstance(obj, classmethod):
			type_ = type(obj)
			print(f'Decorating {type_} methods: ', cls, name)
			original_func = obj.__func__
			decorated_func = func_logger(original_func)
			method = type_(decorated_func)
			setattr(cls, name, method)

		elif isinstance(obj, property):
			print('Decorating property: ', cls, name)
			methods = (('fget', 'getter'), ('fset', 'setter'), ('fdel', 'deleter'))
			for prop, method in methods:
				if getattr(obj, prop):
					obj = getattr(obj, method)(func_logger(getattr(obj, prop)))
			setattr(cls, name, obj)
			# at each 'if' statement, the 'obj' is the decorated 'obj' from the previous step.

		elif inspect.isroutine(obj):
			print('Decorating all routine types: ', cls, name)
			original_func = obj
			decorated_func = func_logger(original_func)
			setattr(cls, name, decorated_func)

	return cls