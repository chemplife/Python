print('------------Scope / Namespace-------------')
a = 10
#globals and locals() will print the namespace
print('Global Namespace: ',globals())
print('Locals() is Globals() in global scope?: ',locals() is globals())
def func():
	global a,b
	a+=1
	b = 100
	c= 50
	print('Global A in local:',a)
	print('Global B in local',b)
	print('Local C: ',c)
	print('Local Namespace: ',locals())

print(a)
func()
print(a)
print(b)

print('------------Closure-------------')

''' When outer() was CREATED, it did not create inner(),
	because the outer() is not called yet to execute the code inside.
	What it did though, it made compiler aware of all the variables inside the outer()
	** compiler doesn't know the values of those variables unless an assignment is made (x=10).
		It just know the existence of 'x'

	When outer() is called, it CREATED inner() when the compiler encounters the 'def inner()'.
	The same thing happens with anything inside inner(), that happened to outer() when compiler first saw 'def outer()'.
	It will see 'x' in there, and since 'x' is not defined inside 'inner()',
		compiler will associate inner() with the 'x' in outer() [which is in namespace 1 level above its own].
		** This association is called as 'CLOSURE'
		** 'x' inside inner() is a 'FREE variable' for inner().
		**** Another way to say: Functions are bound to its FREE Variables via CLOSURE.
		**** This CLOSURE is CREATED when outer() is run (not created/compiled, but run/called)
	Now, when inner() is called and namespace of inner is created, then 'x' will get evaluated to be used.
	Untill then, compiler just knows that 'x' is not defined in inner(), so it must be from a some higher level namespace.
'''
def outer():
	x = 'Python'

	def inner():
		print(x+' Rocks!')

	inner()

outer()

def outer_1(b):
	x = 'Python'

	def inner(a):
		print(x+' Rocks!: '+a+' -> '+b)

	return inner

# Now, inner() is not called inside outer_1(). We are returning it.
# What outer_1() returns in this case is a CLOSURE of inner().
# Meaning, fn now have inner() + association with its FREE variables for use.
# Python won't evaluate 'x' for inner() until it needs it (until inner() is called because then the value will be required.)
# We can access 'x' of outer_1() outside of outer_1().
# Basically, use 'x' outside of the scope of its function.
fn = outer_1('outer_1')
print('Access x outside outer_1()')
fn('inner')
print('Free variables:',fn.__code__.co_freevars)

# This will use the 'cell' object.
# Cell is the intermiate block that has the address of actual value if 'x'
# Under the hood: x.outer_1  and x.inner both points to 'cell', and 'cell' has the address of the value.
# When outer_1() scope ends, x.outer_1 goes away, but x.inner still points to 'cell' so, the value is still accessable.
# x.outer_1 ----->	 ____
#					|Cell|  ------> 'Python'
# x.inner ------->

# And we can have as many functions inside outer_1() using 'x' as their FREE variable, and all of them will point to the same cell.

print('Closure:',fn.__closure__)

print('------------Closure / Class-------------')
# Class Average = a class that gives out the average of all the numbers fed to it at any point in time.
# We can do the same using CLOSURE.

class Average:
	def __init__(self):
		self.total = 0
		self.count = 0

	def add(self, number):
		self.total+= number
		self.count+=1
		return self.total/self.count

def average():
	total = 0
	count = 0
	def add(number):
		nonlocal total, count
		total+=number
		count+=1
		return total/count
	return add

# Class Average and def average(), both does the same thing

a_class = Average()
print('Class average Iter 1:', a_class.add(10))
print('Class average Iter 2:', a_class.add(20))
print('Class average Iter 3:', a_class.add(30))

a_closure = average()
print('Closure average Iter 1:', a_closure(10))
print('Closure average Iter 2:', a_closure(20))
print('Closure average Iter 3:', a_closure(30))

print('---------------Dacorators----------------')
''' The outer function that
		1. take 'function' as argument and,
		2. returns a Closure object
	is called as 'DECORATOR'.
'''
import functools
from functools import wraps

which_func = dict()

# Decorators without @ symbol
def counter_1(fn):
	'''	This decorator function takes a function as argument
	   	and the inner function returns the number of time a function is ran
	'''
	count = 0
	def counter_func(*args, **kwargs):
		'''The inner doc string'''
		nonlocal count
		count+=1
		print('Function = {0}, is being called {1} times'.format(fn.__name__, count))
		which_func[fn.__name__] = count
		return fn(*args, **kwargs)
	return counter_func

def add(*args):
	'''This function add all the positional arguments and returns the sum.'''
	print(functools.reduce(lambda x,y: x+y, list(args)))

def mult(*args):
	'''This function multiply all the positional arguments and returns the product.'''
	print(functools.reduce(lambda x,y: x*y, list(args)))

def fact(num):
	'''This function returns the fatorial of the number fed to it.'''
	print(functools.reduce(lambda x,y: x*y, range(1,num+1)))


print('address of add function before closure:', id(add))
print('address of mult function before closure:', id(mult))
print('address of fact function before closure:', id(fact))

# pass arithmatic functions as arguments and return closure.
# add(), mult(), fact() got DECORATED
# counter_1() is DECORATOR.
add = counter_1(add)
mult = counter_1(mult)
fact = counter_1(fact)

print('address of add function after closure:', id(add))
print('address of mult function after closure:', id(mult))
print('address of fact function after closure:', id(fact))

add(1,2,3,4)
mult(1,2,3,4)
fact(4)

add(1,2,3,4,5,6,7,8)
mult(1,2,3,4,5,6,7,8)
print('Number of function calls:', which_func)

# since add(), mult(), and fact() are closures of counter_func(), their original info is not accessible
print(f'Function info for add ={add.__name__}, mult ={add.__name__}, fact ={add.__name__}')
print(f'Function info for add ={add.__doc__}, mult ={add.__doc__}, fact ={add.__doc__}')


# this is WITH @ symbol
def counter_2(fn):
	'''	This decorator function takes a function as argument
	   	and the inner function returns the number of time a function is ran
	'''
	count = 0
	# wraps fix the metadata of the original function instead of the closure function
	@wraps(fn)
	def counter_func(*args, **kwargs):
		'''the inner doc_String'''
		nonlocal count
		count+=1
		print('Function = {0}, is being called {1} times'.format(fn.__name__, count))
		which_func[fn.__name__] = count
		return fn(*args, **kwargs)
	return counter_func

@counter_2
def add(*args):
	'''This function add all the positional arguments and returns the sum.'''
	print(functools.reduce(lambda x,y: x+y, list(args)))

@counter_2
def mult(*args):
	'''This function multiply all the positional arguments and returns the product.'''
	print(functools.reduce(lambda x,y: x*y, list(args)))

@counter_2
def fact(num):
	'''This function returns the fatorial of the number fed to it.'''
	print(functools.reduce(lambda x,y: x*y, range(1,num+1)))

# pass arithmatic functions as arguments and return closure. ------ NOT NEEDED ANYMORE
#add = counter_1(add)
#mult = counter_1(mult)
#fact = counter_1(fact)

add(1,2,3,4)
mult(1,2,3,4)
fact(4)

add(1,2,3,4,5,6,7,8)
mult(1,2,3,4,5,6,7,8)
print('Number of function calls:', which_func)

# wraps give the metadata of the original function now.
print(f'Function info for add ={add.__name__}, mult ={mult.__name__}, fact ={fact.__name__}')
print(f'Function info for add ={add.__doc__}, mult ={mult.__doc__}, fact ={fact.__doc__}')

print('---------------Parameterized Dacorators----------------')
# Eg: The timer decorator will run the same function 'n' number of times and gives out the average time the function took.

from functools import reduce

# 1. Let's write a regular timer decorator
def timer(fn):
	from time import perf_counter

	def inner(args):
		start = perf_counter()
		fn(args)
		stop = perf_counter()
		elapse = stop - start
		print(f'Function {fn.__name__} took {elapse} sec to run.')

	return inner

@timer
def addition(args):
	print('Sum is: ', reduce(lambda x,y: x+y, range(args)))

addition(10000)

# 2. Let's write a timer decorator that takes average for 2 runs
def timer_hardcode(fn):
	from time import perf_counter

	def inner(args):
		counter = 0
		elapse = 0
		for i in range(2):
			start = perf_counter()
			fn(args)
			stop = perf_counter()
			elapse += (stop - start)
			counter+=1
		elapse_avg = elapse/counter
		print(f'Function {fn.__name__} took {elapse_avg} sec to run.')

	return inner

@timer_hardcode
def addition_2(args):
	print('Sum is: ', reduce(lambda x,y: x+y, range(args)))

addition_2(10000)

# 3. Let's write a timer decorator that takes average for 'n' runs
#	 We need to parameterize the timer decorator to run a certain number of times.
#	 timer_parameter is called as 'DECORATOR_FACTORY'

# 	 DECORATOR_FACTORY: creates and returns a decorator that we want

def timer_parameter(n):
	def timer_hardcode(fn):
		from time import perf_counter

		def inner(args):
			counter = 0
			elapse = 0
			for i in range(n):
				start = perf_counter()
				fn(args)
				stop = perf_counter()
				elapse += (stop - start)
				counter+=1
			elapse_avg = elapse/counter
			print(f'Function {fn.__name__} took {elapse_avg} sec to run.')

		return inner
	return timer_hardcode

# Decorator_Factory syntax: @d_f()
# Decorator syntax:			@d
@timer_parameter(4)
def addition_2(args):
	print('Sum is: ', reduce(lambda x,y: x+y, range(args)))

addition_2(10000)
print('ID:', id(addition_2))
addition_2(10000)
print('ID:', id(addition_2))

print('---------------Parameterized Dacorators inside class----------------')

# __call__ makes the object of the class 'callable'.
class MyClass:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __call__(self, c):
		print(f'a={self.a}, b={self.b}, c={c}')

obj = MyClass(10,20)
# both are same.
obj(30)
obj.__call__(30)

# Since 'obj' is callable, we can treat it a DECORATOR, and MyClass as a DECORATOR_FACTORY
class MyClass:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __call__(self, fn):
		def func(*args):
			print(f'a={self.a}, b={self.b}, args={args}')
			return fn(*args)
		return func

@MyClass(10,20)
def multiply(*args):
	print(functools.reduce(lambda x,y: x*y, list(args)))

multiply(1,2,3,4,5,6,7,8)

print('---------------Dacorats a class----------------')
# Monkey Patching: Adding attributes to a class.
from fractions import Fraction

Fraction.is_integral = lambda self: self.denominator == 1
f1 = Fraction(2,3)
f2 = Fraction(6,3)
print('f1 is_integral?',f1.is_integral())
print('f2 is_integral?',f2.is_integral())

# Passing class in a decorator
def info(self):
	result = []
	result.append("1,2,4")
	result.append('Class: {0}'.format(self.__class__.__name__))
	result.append('Address: {0}'.format(hex(id(self))))
	#vars() is in-built function to return properties of the object. In our case, what's in __init__()
	for k,v in vars(self).items():
		result.append(f'{k}:{v}')

	return result

# return cls will just enable us to do 'add = outer(add)'
# and now, we can add() like we would have but with extra functionality from the decorator
def debug_info(cls):
	cls.debug = info
	return cls

@debug_info
class MyClass:
	def __init__(self, name, db):
		self.name = name
		self.dob = db

	def sayhi(self):
		print('Hi: ', self.name)

obj = MyClass('John', 1992)
print('Monkey patch from decorator:',obj.debug())