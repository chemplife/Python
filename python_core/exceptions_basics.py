'''
EAFP = It is EASY to ASK for FORGIVENESS than ask for PERMISSION

Exceptions are objects (instances) of the 'class' of exception, they belong to.. Like ValueError, NotImplemented, etc..

When Exceptions are raised:
	-> It triggers a special execution 'propogation' workflow
	-> We can intercept that workflow by doing 'Exception Handling'
	-> If the 'Exception' is not handled, it 'propogated' to the caller
		- Eg: if 'Exception' happens in a function and not handled there, it will propogate to the part of code that called that function.
			It will keep on moving up, until it is handled or it reach the module or Application level and if the Exception is left unhandled,
				program terminates.
	-> There is stack trace that keep track of what happens in their propogation workflow.
		- It helps us find the origin of the Exception and every step of the stack.

Compound Statement of (try, except, else, finally.. is used..) 'SILENCE' the Exception.. We can handle it or not.. We just caught it and Silenced it.

Categories of Exceptions:
	1. Compilation Exception:	That happens when the code is compiled (Eg: SyntaxError)
	2. Execution Exception: 	That happens when the program is running (Eg: ValueError, KeyError, StopIteration)

Python's Built-in Exception Classes uses 'Inheritance' to form a 'Class Hierarchy'..
	-> There is a Base Exception for Every Exception..
	-> Including Custom Exceptions.. They need to be inherited from one of the Exception Classes
		-> Base Exception class is 'BaseException'.. But we don't inherit mostly from this class.
			-> Why? Read on..
		->BaseException Class Hierarchy:
			-> SystemExit:			Raised on 'sys.exit()'
			-> KeyboardInterrupt:	Raised on 'Ctrl + c' press
			-> GeneratorExit:		Raised when a Generator or Coroutine is closed
			-> Exception:			Raised by Everything Else..
				-> Our custom Exceptions are generally like ValueError or KeyError,
					which does not fall under any of the SystemExit, KeyboardInterrupt, or GeneratorExit category..
					-> So, we usually Inherit from 'Exception' class which is a subclass of 'BaseException'

Exception-Class includes:
	-> ArithmeticError:
				-> FloatingPointError
				-> ZeroDivisionError
	-> AttributeError
	-> LookupError
				-> IndexError
				-> KeyError
	-> SyntaxError
	-> RuntimeError
	-> TypeError
	-> ValueError
	... There are more..

Now, again: Exceptions are objects.. and they are instances of one of the above mentioned classes..
			which directly, or indirectly inherits from 'BaseException'

Why is Inheritance of Exceptions a good thing?
-> Instance of IndexError, will also be an instance of LookupError, and it will also be an instance of Exception-Class.
	-> So, if I'm trying to catch a LookupError, I'm evidently catching both IndexError and KeyError as well.

Raising an Exception:
	-> raise <Exception-Object> as ex:
		-> Excption-Object:	HAS TO BE from a class directly/indirectly inheriting from 'BaseException'
		-> 'as ex': Optional, if you want to catch the exact Exception for logging or display someother purpose..
		-> ex: just a variable name.. can use anything..
'''

l = [1,2,3]

try:
	l[3]
except IndexError as ex:
	print('IndexError: ', ex.__class__,':', str(ex))

try:
	l[3]
except LookupError as ex:
	print('LookupError: ', ex.__class__,':', str(ex))

print('\n\n---------------------- Propogation Workflow ----------------------\n')

def func_3():
	ex = ValueError('My custom Message..')
	raise ex

def func_2():
	func_3()

def func_1():
	func_2()

# print('Direct call to func_3: ', func_3())
# print('Call func_3 from func_1: ', func_1())
# You'll see the Stack Trace very different in the above 2 cases.

'''
Handling Exceptions:

try:										(REQUIRED)
	code that we want to protect from potential Exceptions

except <ExceptionType> as ex:				(0 or more times)
	Catch only the 'ExceptionType' Exceptions or any subclass of it..
	(rest of the ExceptionTypes propogates through the stack..)

	**
		There can be multiple 'except' block for different types of 'ExceptionTypes'..
		We might want to handle different 'ExceptionTypes' in a different ways..
		
		** Write Multiple 'except' block in ascending order of 'Exception Class Hierarchy'.. (Most Specific -> Least Specific)
			Because if python encounters 'except LookupError' before 'except IndexError',
				it will check if the 'Encountered ExceptionType' is an instance of 'LookupError' or not..
				If it is, the exception will get handled at 'LookupError' Level
			-> Then, there is no point mentioning 'IndexError' AFTER 'LookupError' because the Exception will never reach it..

		SO, ORDER of 'except <ExceptionType> MATTERS A LOT...
	**

		except tuple of multiple ExceptionTypes
	** except (<ExceptionType_1>, <ExceptionType_2>) as ex: -> to handle multiple 'ExceptionTypes' in similar way..
															-> 'ex' will still tell us which 'ExceptionType' it is..


finally:									(0 or 1 time)
	This code block always executes.. whether exception occured or not..
	Eg: you would like to terminate a DB connection after doing some operation if code ran successfully or got an exception..

	** This block runs BEFORE the 'Propogation' STARTS in case of an Exception..


else:										(0 or 1 time)
	This code executes only if 'try' ran notmally without any Exception happening..
	(For Exception check, the 'except' block HAS TO BE there..)
	So, to use 'else', 'except' HAS TO BE there..

** Nesting: We can start an 'Exception Handling block' (try..except.. etc block) in any of code blocks above..

#######################
Bare Exception Handlers: No 'ExceptionType' mentioned..	(WE CANNOT USE 'as' here..)
try:
	piece of code
except:
	handle it..

-> Should not do that unless there is a situation where we don't know how to handle the exception and have to let it propogate..
-> How to get a handle-on this exception?
	-> sys.exc_info()
		-> we have to be in the 'except' block to access the exception_info..
		-> returns a tuple object
			-> (exc_type, exc_value, exc_traceback)

#######################
Each ExceptionType has different properties available to them (depending on which Exception class the ExceptionType belongs to)
But since every ExceptionType belongs to 'class BaseException', they have 2 properties in common:
	-> args:			arguments used to create the Exception Object.
	-> __traceback__:	traceback object. Helps to propogate through the stack to reach the point where the exception happened.
						-> uses 'traceback' module to visualize the stack..
							-> print_tb
							-> print_exception
							-> 'traceback' is the same object returned by sys.exc_info().. the last element of the tuple..

	(Might not need it.. unless we are doing some Really Advance Programming.. like writing Frameworks)
'''

print('\n\n---------------------- Exception Handling ----------------------\n')

try:
	raise ValueError('My Error')
except ValueError as ex:
	print('ValueError: ', ex)
else:
	print("'else' might not show up..")
finally:
	print("Can't Escape 'Finally', can you?")

print('\n')

try:
	a = 10
except ValueError as ex:
	print('ValueError: ', ex)
else:
	print('Else is here..')
finally:
	print("And 'Finally',will always be here..")


print('\n')
# raise error from a 'Bare Exception Handler'
try:
	raise ValueError('My Error')
except:
	# ............ exception intercepted ............
	# Do something here before we make 'propogation' continue.. Eg: log something. 
	print('Some wannabe Error')
	# Uncomment the line below to let the Exception Propogate..
#	raise
else:
	print('Else is here?..')
finally:
	print("Again.. 'Finally',will always be here..")

print('\n')
import sys

try:
	raise ValueError()
except:
	ex = sys.exc_info()
	print('Bare Exception value: ', ex)

print('\n\n---------------------- Example: Exception Handling ----------------------\n')
# We want to accept only 'name' and 'age', and no other data.. also, we want to check if 'Age' is 'int()' type of not.

import json

data_json = '''
{
	"Alex": {"age": 18},
	"Bryan": {"age": 21, "city": "London"},
	"Guido": {"age": "unknown"}
}
'''

data = json.loads(data_json)

class Person:
	__slots__ = 'name', '_age'

	def __init__(self, name):
		self.name = name
		self._age = None

	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self, value):
		if isinstance(value, int) and value >= 0:
			self._age = value
		else:
			raise ValueError('Invalid Age')

	def __repr__(self):
		return f'Person (name = {self. name}, age = {self.age})'

persons = []

for name, attributes in data.items():
	# ********
	# This try-except will finish normally if any exception happened in the 'Nested' try-except-block is handled there..
	# ********
	try:
		p = Person(name)
		for attr_name, attr_value in attributes.items():
			try:
				setattr(p, attr_name, attr_value)
			# Any exception other than AttributeError will propogate up, outside this try-except block.
			# Basically it will go to the try-except block outside this for-loop
			except AttributeError as ex:
				print(f'Ignoring Attribute: {name}:{attr_name} = {attr_value}')
	except ValueError as ex:
		print(f'Data for Person({name}) contains invalid attribute value: {ex}')
	else:
		persons.append(p)

print('Persons List: ', persons)

print('\n\n---------------------- Hiding Exceptions using raise-from ----------------------\n')

# Helpful to not bother user with the implementation Exceptions, when he/she needs to be only need to know what triggered the whole thing.

# We are selecting which Traceback to use..

# without 'from None', users will see Errors in sequence
#	1. KeyError
#	2. TypeError
#	3. ValueError

try:
	raise ValueError()
except ValueError:
	try:
		raise TypeError()
	except TypeError:
		raise KeyError() from None

# with 'from None', users will see only 1 Error..
#	1. KeyError

try:
	raise ValueError()
except ValueError as exc_1:
	try:
		raise TypeError()
	except TypeError as exc_2:
		raise KeyError() from exc_1

# with 'from exc_1', users will see only 2 Errors..
#	1. KeyError
#	2. ValueError