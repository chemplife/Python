'''
'__call__()': method makes the instances of the class 'callables' themselves.

Can be used for creating Decorator Classes (classes that can be used as Decorators)
'''

from functools import partial

class Person:
	def __call__(self, name):
		print('__call__ is called..')
		return f'Hello {name}!'

p = Person()
print('Callable Object: ', p('Eric'))
# object 'p' is now a callable.. It is not a 'Method' or 'Function'..
print("Type of p: ", type(p))

print('\n\n-------------------- Recap of Partial --------------------')

# so what is partial then..
print("\nPartial's type: ", type(partial))
# 'Partial' is a callable class.

def my_func(a,b,c):
	return a,b,c

# 10 and 20 are ppsitional arguments of 'my_func'
partial_func = partial(my_func, 10,20)
print('Type of partial_func: ', type(partial_func))

print('Calling partial_func: ', partial_func(30))

'''
Till this point,
All the callables-
	1. p() : 			Instance of Class Person
	2. partial: 		class of type 'type'
	3. my_func:			Function
	4. partial_func:	Instance of 'partial' class
'''

print('\n\n-------------------- Recreating Partial Class --------------------')

class Partial:
	def __init__(self, func, *args):
		self._func = func
		self._args = args

	def __call__(self, *args):
		return self._func(*self._args, *args)

def my_func(a,b,c):
	return a,b,c

# using our custom Partial class.. And the object will be callable like it was for 'functools.partial' class.
partial_func = Partial(my_func, 10,20)
print('Type of partial_func: ', type(partial_func))

print('Calling partial_func: ', partial_func(30))

print('\n\n-------------------- Check if something is callable or not --------------------')
# using callable() to check if something is callable or not.

print('Is print callable?: ', callable(print))
print('Is int callable?: ', callable(int))
print('Is Partial Class callable?: ', callable(Partial))
print('Is partial_func callable?: ', callable(partial_func))

print('\n\n-------------------- Implementing a Cache Class --------------------')
'''
A dictionary that can be used to caching.. Also, it will keep a track of cache misses (no of requests that are not in cache dictionary)


 Using defaultdict: Because if 'key' does not exist in a dictionary, the defaultdict will return an instance of what we specify
	as the factory for the defaultdict.

def default_value():
	return 'N/A'

# Here 'default_value' is the factory of 'defaultdict'
d = defaultdict(default_value)
'''

from collections import defaultdict

MISS_COUNTER = 0

def default_value():
	global MISS_COUNTER
	MISS_COUNTER += 1
	return 'N/A'

d = defaultdict(default_value)

d['a'] = 1
print('Requesting an element from d that exist:', d['a'])
print('Requesting an element from d that doesnot exist:', d['b'])
print('Requesting an element from d that doesnot exist:', d['c'])
print('MISS_COUNTER value: ', MISS_COUNTER)

#But the above approach won't work if there are many dictionaries that we are dealing with.
# Let's use a class approach

class DefaultValue:
	def __init__(self, default_value):
		self.default_value = default_value
		self.counter = 0

	def __call__(self):
		self.counter +=1
		return self.default_value

def_1 = DefaultValue(None)
def_2 = DefaultValue(0)
def_3 = DefaultValue('N/A')

cache_1 = defaultdict(def_1)
cache_2 = defaultdict(def_2)
cache_3 = defaultdict(def_3)

print("2 cache miss..: ",cache_1['a'], cache_1['b'])
print('cache_1: ', cache_1)
print('Counter for cache_1 misses: ', def_1.counter)

print("\n1 cache miss..: ",cache_2['a'])
print('cache_2: ', cache_2)
print('Counter for cache_1 misses: ', def_2.counter)

print("\n3 cache miss..: ",cache_3['a'], cache_3['b'], cache_3['c'])
print('cache_3: ', cache_3)
print('Counter for cache_1 misses: ', def_3.counter)


print('\n\n-------------------- Callable class objects to make Classes-as-Decorators --------------------')
'''
Example is only for creating 'Decorators' for regular functions.
Decorators for 'Methods' can be created but they will be part of Descriptors.
'''

import random
from time import perf_counter, sleep
from functools import wraps

# Decoator function that give access to the local variables
def profiler(fn):
	_counter = 0
	_time_elapsed = 0

	@wraps(fn)
	def inner(*args, **kwargs):
		nonlocal _counter, _time_elapsed
		_counter += 1
		start = perf_counter()
		result = fn(*args, **kwargs)
		end = perf_counter()
		_time_elapsed += (end - start)
		return result

	def counter():
		return _counter

	def avg_time():
		return _time_elapsed / _counter

	inner.counter = counter
	inner.avg_time = avg_time
	return inner


random.seed(0)

@profiler
def func1():
	sleep(random.random())

func1()
func1()
print('Func1 counter: ', func1.counter())
print('Func1 avg_time: ', func1.avg_time())

# Now, this can be implemented a little easily with 'class as decorator'.
print('\n-------------------- Classes-as-Decorators --------------------')

class Profiler:
	def __init__(self, fn):
		self.counter = 0
		self.time_elapsed = 0
		self.fn = fn

	def __call__(self, *args, **kwargs):
		self.counter += 1
		start = perf_counter()
		result = self.fn(*args, **kwargs)
		end = perf_counter()
		self.time_elapsed = (end - start)
		return result

	@property
	def avg_time(self):
		return self.time_elapsed / self.counter
	

@Profiler
def func_1(a,b):
	sleep(random.random())
	return (a,b)

# This is similar to
# func_1 = Profiler(func_1)		-> obj = SomeClass(parameter)
print('type of func_1: ', type(func_1))

func_1(10, 20)
func_1('Apple', 'Ball')
print('Additional Functionalities of func_1-> Counter: ', func_1.counter)
print('Additional Functionalities of func_1-> time_elapsed: ', func_1.time_elapsed)
print('Additional Functionalities of func_1-> avg_time: ', func_1.avg_time)