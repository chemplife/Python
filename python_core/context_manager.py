''' PEP-343
Pattern:
	Get-In / Enter
	Do some work
	Clean-up and Get-Out / Exit

Context Managers are responsible for cleaning up things when we exit.

Context-Management-Protocol:
	__enter__	-> Setup, and optionally return some object
	__exit__	-> clean-up/tear-down and exit
'''

with open('test_files/cars.csv') as file:
	# Do some work
	pass
#Done with the context
'''
with context_manager as object(optional):			-> 'with' calls __enter__().. object holds return value of __enter__()
	do some work
	raise ValueError('Value of error')				-> Raise exception in case something happens. __exit__() will take it.
Done with the Context 								-> This indentation calls __exit__()

Any exception happens inside 'with' block
	-> Silenced: Do nothing about it 			-> __exit__() returns TRUE
	-> If NOT Silenced:							-> __exit__() need 3 arguments:
																			1. exception type (if any, None Otherwise)
																			2. exception value (if any, None Otherwise)
																			3. traceback object (if any, None Otherwise)
													-> __exit__() returns FALSE.

*** 'with' takes the scope of the block where it is running
	Any Variable inside 'with' block is GLOBAL (scope of the block it is in).
	Including the 'object' in 'with' statement.
'''

# Custom Context Manager

class MyContext:
	def __init__(self):
		print('Message from __init__')
		self.obj = None

	def __enter__(self):
		print('Entering Context..')
		self.obj = 'The Return Object from __enter__().'
		return self.obj

	def __exit__(self, exc_type, exc_value, exc_tb):
		print('Exiting Context..')
		if exc_type:
			print(f'**** Error Occurred: {exc_type},\t{exc_value}')

		# False means: DO NOT SUPPRESS ERROR.. Error raises with TraceBack
		return True

with MyContext() as obj:
	print('Inside WITH Block')
	raise ValueError('Test Error Value')

print('\nObject from WITH:', obj)
print('Is Obj in global?:', 'obj' in globals())


# we can change the output location of the program
import sys

class OutToFile:
	def __init__(self, fname):
		self._fname = fname
		self._current_stdout = sys.stdout

	def __enter__(self):
		self._file = open(self._fname, 'w')
		sys.stdout = self._file

	def __exit__(self, exc_type, exc_value, exc_tb):
		sys.stdout = self._current_stdout
		self._file.close()
		return False

# outputs within the 'WITH' block will go to external file
print('\n\n--------------------------- Change output location ---------------------------')
with OutToFile('output_file_context_manager.txt'):
	print('Line 1')
	print('Line 2')

print('Print items in each line:')
with open('output_file_context_manager.txt') as f:
	for r in f:
		print('\t',r, end='')
print('\nJust read lines:')
with open('output_file_context_manager.txt') as f:
	print('\t',f.readlines())


print('\n\n--------------------------- Generator to create Context Manager ---------------------------')

def my_gen():
	try:
		print('Creating context and yielding object..')
		yield [1,2,3,4]
	finally:
		print('exiting context and cleaning up')

gen = my_gen()
lst = next(gen)
print('List from Generator:', lst)
try:
	next(gen)
except StopIteration:
	pass

#Class that has context management protocol to encapsulate this functionality
# (*arga, **kwargs) makes this class very generic. We can pass any generator to it and get a context manager.
class GenCtxMang:
	def __init__(self, gen_func, *args, **kwargs):
		self._gen = gen_func(*args, **kwargs)

	def __enter__(self):
		return next(self._gen)		#	<- Returns what was yielded

	def __exit__(self, exc_type, exc_value, exc_tb):
		try:
			next(self._gen)			#	<- Runs the 'finally' block
		except StopIteration:
			pass
		return False
print('\n')
with GenCtxMang(my_gen) as obj:
	print('Priting fro GenCtxMang class:', obj)

print('\nUsing our custom Generator Conext Manager for reading and writing file..')
def file_op(fname, mode):
	f = open(fname, mode)
	try:
		print('Opening file....')
		yield f 		#	<- Single Yield: the return value of __enter__()
	finally:			# 	<- Cleanup phase
		print('Closing file....')
		f.close()

print('------------ Writing to file ------------')
with GenCtxMang(file_op, 'gen_ctx_test.txt', 'w') as wr:
	wr.writelines('testing....')

print('------------ Reading from file ------------')
with GenCtxMang(file_op, 'gen_ctx_test.txt', 'r') as rd:
	print(rd.readlines())

print('\n\n--------------------------- Context Manager Decorators ---------------------------')
def file_ops(fname, mode):
	f = open(fname, mode)
	try:
		print('Opening file....')
		yield f 		#	<- Single Yield: the return value of __enter__()
	finally:			# 	<- Cleanup phase
		print('Closing file....')
		f.close()

class GenCtx:
	def __init__(self, gen_obj):
		self.gen = gen_obj			#	<- We have to create the generator object first before passing it to class.

	def __enter__(self):
		print('Calling next() to get yielded value from generator..')
		return next(self.gen)		#	<- Returns what was yielded

	def __exit__(self, exc_type, exc_value, exc_tb):
		print('Calling next() to perform cleanup in generator..')
		try:
			next(self.gen)			#	<- Runs the 'finally' block
		except StopIteration:
			pass
		return False

# 'file_gen' is the object of the 'file_ops' Generator.
file_gen = file_ops('gen_ctx_test_2.txt', 'w')
# we pass the generator object 'file_gen' to the GenCtx class.
with GenCtx(file_gen) as fg:
	fg.writelines('Writing for Generator Context Manager Test 2..')


# We are creating a decorator that will create the Generator Objects for us to pass it to our GenCtx class.
def context_manager_dec(gen_func):
	def helper(*args, **kwargs):
		gen = gen_func(*args, **kwargs)
		ctx = GenCtx(gen)
		return ctx
		# we can do -> return GenCtx(gen)
	return helper

'''
Decorator flashback:

@decorator 			-|=>
def my_func()		-|=> my_func = decorator(my_func)

Now, my_func in 'def my_func()' is what the decorator returned, which is 'helper' in this case.
Basically, calling 'my_func()' with any argument, we are actually calling 'helper()' with those argument.

***********
Context Managers we defined to do execting this.
Make it easy for Generators to do the cleanup.
***********
'''
@context_manager_dec
def file_operations(fname, mode):
	f = open(fname, mode)
	try:
		print('Opening file....')
		yield f 		#	<- Single Yield: the return value of __enter__()
	finally:			# 	<- Cleanup phase
		print('Closing file....')
		f.close()

#Now, 'file_operations' is a context manager (because that is what get returned from the 'helper()' function)
with file_operations('gen_ctx_test_2.txt', 'r') as f:
	print('Reading with decorator:', f.readlines())

print('\n\n--------------------------- Python In-Built Context Manager Decorators ---------------------------')

from contextlib import contextmanager, redirect_stdout

@contextmanager
def file_operations_b(fname, mode):
	f = open(fname, mode)
	try:
		print('Opening file....')
		yield f 		#	<- Single Yield: the return value of __enter__()
	finally:			# 	<- Cleanup phase
		print('Closing file....')
		f.close()

#Now, 'file_operations' is a context manager (because that is what get returned from the 'helper()' function)
with file_operations_b('gen_ctx_test_2.txt', 'r') as f:				# 'f' is the same 'f' that was yielded in the helper()
	print('Reading with built-in decorator:', f.readlines())
print("Access 'f' outside 'with:", f)

'''
Redirect_stdout: redirects the output of an execution to the output stream we provide it.
				-> If it is a file we want the output to be printed in, we can't just give it a filename, the way we did earlier.
					-> We have to give it a file object.
'''
print('\n\n--- Redirecting output ---')
with open('gen_ctx_test_2.txt', 'w') as f:
	with redirect_stdout(f):
		print('Look at the bright side of life..')

with file_operations_b('gen_ctx_test_2.txt', 'r') as f:				# 'f' is the same 'f' that was yielded in the helper()
	print('Reading redirected Output:', f.readlines())


'''
GO OVER NESTED CONTEXT MANAGER Program from resources.

contextlib.ExitStack handles multiple context managers nested together.
'''