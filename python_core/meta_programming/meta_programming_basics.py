'''
MetaProgramming is a technique in which our programs will treat other programs as their data.
	-> These programs are designed to read, generate, analyze, or transform, and even modify other programs and/or itself while running.
		-> Basically, code can modify code..
		-> Keeps our code DRY	(Don't Repeat Yourself)
			-> Use the existing piece of code..

Some MetaProgramming Techniques:
	-> Decorators:	Using code to modify funcionality of another piece of code
					-> We can Decorate entire class, not just a function.
					-> We can have Decorator-Classes, that can be used to decorate other functions and classes.

	-> Descriptors:	Use code to modify the behavior of dot-notation of classes.
	
	-> Metaclasses:	Used to write more Generic-Code that can be used at many places..
					-> (Like a Library or Framework.. Not at application level.. EVER)
					Used for creating 'type' objects (Classes basically.)
					-> MetaClasses are in essence class(type) factory.

					Can be used to hook into Class-Creation-Cylce (when we use the 'class' keyword to create a class, something do creates it.)
		(They don't play very well with Multiple Inheritance so, to learn it, we will use Single-Inheritance in the beggining.)

		CAUTION:
			MetaClasses are easy to understand, but it is not easy to know 'when to use it'.
			-> If in a case, use of MetaClass is Obvious, "DON'T USE IT THERE..."
			-> Makes the code harder to read and the details can become very complicated very easily.
				-> (If you have a Hammer, doesn't mean everything is a nail..)
			
			UseCases:
				-> Writing Libraries / Frameworks
				-> Mostly not for day-to-day application programs.
'''
print('--------------------------------------------------------- Decorators ---------------------------------------------------------\n')


from functools import wraps

def debugger(fn):
	@wraps(fn)
	def inner(*args, **kwargs):
		print(f'{fn.__qualname__}', args, kwargs)
		return fn(*args, **kwargs)
	return inner

@debugger
def func_1(*args, **kwargs):
	pass

@debugger
def func_2(*args, **kwargs):
	pass

func_1(10,20, kw_1='a', kw_2='b')
func_2([1,2,3])

# Any change we want in the debugger for both of these, we only need to make the change at 1 place..

print('\n\n--------------------------------------------------------- Descriptors ---------------------------------------------------------\n')

class IntegerField:
	def __set_name__(self, owner, name):
		self.name = name

	def __get__(self, instance, owner):
		print('__get__ called..')
		return instance.__dict__.get(self.name, None)

	def __set__(self, instance, value):
		print('__set__ called..')
		if not isinstance(value, int):
			raise TypeError('Must be an Integer Value..')
		instance.__dict__[self.name] = value

class Point:
	x = IntegerField()
	y = IntegerField()

	def __init__(self, x, y):
		self.x = x
		self.y = y

# When the dot-notation happens on 'x or y', Python know that since they are Descriptor-Instances, we need to call the __get__ and __set__ methods.
# This will call __set__() 2 times (1 for 'x' and 1 for 'y')
p = Point(10,20)

# These will call __get__()
print('x= ', p.x)
print('y= ', p.y)

print('\nSet a Non-Integer value for x.')
try:
	p.x = 10.5
except TypeError as ex:
	print('Exception happened: ', ex)

# Any more checks we want for the 'Point Class' attributes, we can make those changes in 1 place..