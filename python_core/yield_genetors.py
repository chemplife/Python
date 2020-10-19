'''
Any function that have 'yield' statement:
	-> Does't return anything by just calling the function.
		-> Instead, it creates a generator object.
	-> On x = next(), Executes the function until it encounters 'yield statement', and whatever is in 'yield' is 'emitted' to x.
		-> we can now perform operations on whatever is being emiited out by 'yield' statement
	-> The state of the function is saved and the function continue to resume wherever it left.
	-> when the function 'return' something instead of yielding, that means it finished running.
		-> StopIteration exception is raised.

A function the uses the 'yield' statement is called generator function.
def my_func():			-> a regular function
	yield a 			-> calling my_func() will return a generator object. A Generator is created with function is CALLED.
	yield b
	yield c

gen = my_func()			-> Created a generator object.
a = next(gen)				-> Generator can implement the 'iterator protocol'.
							So, it executes the body of the function and emits/returns what is in yield.
							The execution pauses until next() is called again. At this time, function resumes
							execution where it left.

After 'yield c', when we do 'next(gen)', since there is nothing left, the function returns StopIteration unless we specify something else.

**** GENERATORS are ITERATORS.
	-> They implement iterator protocol.
'''
import math

# Custom Factorial Iterator

class FactIter:
	def __init__(self, num):
		self.num = num
		self.i = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.i >= self.num:
			raise StopIteration
		else:
			result = math.factorial(self.i)
			self.i += 1
			return result

fact_iter = FactIter(5)
print('Custom Factorial Class:')
print(list(fact_iter))

# Now, since it is an iterator, we cannot reuse it.
print(list(fact_iter))

print('----------------------------------------------------------------------')
# Closure for factorial
def factorial_closure():
	i = 0
	def inner():
		nonlocal i
		result = math.factorial(i)
		i += 1
		return result
	return inner

f = factorial_closure()
print('Factorial using factorial_closure')
print('Call 1',f())
print('Call 2',f())
print('Call 3',f())
# this is infinite

fact_clo_iter = iter(factorial_closure(), math.factorial(5))
print('List of factorial_closure upto 5', list(fact_clo_iter))

# Now, since it is an iterator, we cannot reuse it.
print('List of factorial_closure upto 5', list(fact_clo_iter))

print('----------------------------------------------------------------------')
print('Basic Yield Generator')

def my_func():
	print('1')
	yield 'Flying'
	print('2')
	yield 'My'
	print('3')
	yield 'Plain'

# This will not print anything.
f = my_func()
print('Type of my_func:', type(my_func))
print('Type of object f:', type(f))
print(f"Available methods-> __iter__: {'__iter__' in dir(f)},\n\t\t\t\t\t __next__: {'__next__' in dir(f)}")
print(f'Is iter(f) is f: ', iter(f) is f)

#Now it will print
line = f.__next__()
print('yield Value: ', line)
line_2 = next(f)
print('2nd yield Value: ', line_2)
line_3 = f.__next__()
print('3rd yield Value: ', line_3)
#This will give us the exception.
#line_4 = next(f)
#print('4th yield Value: ', line_4)

def factorial(n):
	for i in range(n):
		yield math.factorial(i)

fact = factorial(5)
print('Type of factorial Fucntion: ', type(factorial))
print('Type of fact: ',type(fact))
print('Factorial using yield:')
for i in range(5):
	# We can do amny things here.....
	print(next(fact), end='\t')
print('\n')

print('Factorial using yield and put in list:')
fact_2 = factorial(5)
s = []
for i in range(5):
	s.append(next(fact_2))
print(s)
