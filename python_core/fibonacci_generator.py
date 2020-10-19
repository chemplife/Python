from timeit import timeit
print('--------- Fibonacci using Recursion ---------')

def fib_recursive(n):
	if n <= 1:
		return 1
	else:
		return fib_recursive(n-1) + fib_recursive(n-2)

print([fib_recursive(n) for n in range(10)])
print('Time elapse: ',timeit('fib_recursive(29)', globals=globals(), number=10))

# Try using cache in Recursion
from functools import lru_cache

print('\nUSING CACHE')

@lru_cache
def fib_recursive_cache(n):
	if n <= 1:
		return 1
	else:
		return fib_recursive(n-1) + fib_recursive(n-2)

print([fib_recursive_cache(n) for n in range(10)])
print('Time elapse: ',timeit('fib_recursive_cache(30)', globals=globals(), number=10))

#But it will also not work after certain recursion depth
# print([fib_recursive_cache(n) for n in range(1000)])

print('\n\n--------- Fibonacci using List Comprehension ---------')

def fib_list_comp(n):
	fib_0 = 1
	fib_1 = 1
	for i in range(n-1):
		fib_0, fib_1 = fib_1, fib_1+fib_0
	return fib_1

print([fib_list_comp(n) for n in range(10)])
#No recursion depth issue. And is fast
print('Time elapse: ',timeit('fib_list_comp(2000)', globals=globals(), number=10))

# Iterator to get to a Fibonacci number
class FibIter:
	def __init__(self, n):
		self.n = n
		self.i = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.i >= self.n:
			raise StopIteration
		else:
			result = fib_list_comp(self.i)
			self.i += 1
			return result

fib_iter = FibIter(7)
print('\nIterate over Fibonacci Numbers using Iterator.')
print([num for num in fib_iter])
print('\nThis is calculating Fibonacci Number from 0 each time.')
print('Time elapse: ', timeit('list(FibIter(5000))', globals=globals(), number=2))

print('\n\n--------- Fibonacci using Generator function instead of Iterator ---------')

# We won't need an Iterator to iterator over the Fibonacci series.
# We can do all that in 1 shot.

def fib_gen_func(n):
	fib_0 = 1
	yield fib_0
	fib_1 = 1
	yield fib_1
	for i in range(n-2):
		fib_0, fib_1 = fib_1, fib_1+fib_0
		yield fib_1

fib_gen = fib_gen_func(7)
print('Iterate using Generator function.')
print([num for num in fib_gen])
print('Time elapse: ', timeit('list(fib_gen_func(5000))', globals=globals(), number=2))

print('\n\n--------- Generators and Iterators Commonalities ---------')

'''
The rules that apply to ITERATORS applies to GENERATORS as well.
'''

def square(num):
	for i in range(num):
		yield i**2

sq = square(5)
# Enumerate is itself an iterator that works in 'Lazy' fashion. It will not evaluate 'sq' until it is requested.
enum = enumerate(sq)
print('Iteration 1:', next(sq))
print('Iteration 2:', next(sq))
# By the time Enumerate picks up, 2 of the 'sq' values are used up.
print('Enumerate 1:', list(enum))

# We can create a custom ITERABLE that calls the Generator function and create an iterator on each call.
class Squares:
	def __init__(self, n):
		self.n = n

	def __iter__(self):
		return square(self.n)

sq = Squares(5)
print('\nList from ITERABLE using Generator for Iterator:')
print([n for n in sq])
print([n for n in sq])

# We can write our Generator function inside the class too.
print('\nGenerator as class function')
class Squares:
	def __init__(self, n):
		self.n = n

	def __iter__(self):
		return Squares.square(self.n)

	@staticmethod
	def square(num):
		for i in range(num):
			yield i**2
sq = Squares(5)
print(list(sq))
print(list(sq))


print('\n\n--------- Generator Expressions ---------')
'''
List Comprehension		-> [....] : Returns list 											: Eager Evaluation : Iterable
Generator Expression 	-> (....) : Returns Generator.. () is another way of saying 'Yield'	: Lazy Evaluation. : Iterator
'''
import dis

l = [i**2 for i in range(7)]
print('Type of l: ', type(l))
print('List: ',l)
print('List printed again: ',l)

g = (i**2 for i in range(7))
print('Type of l: ', type(g))
print('Generator: ',list(g))
print('Generator printed again: ',list(g))


exp = compile('[i**2 for i in range(7)]', filename='<string>', mode='eval')
print(dis.dis(exp))

print('\n\nNested Generator Expressions')
from math import factorial

def combo(n,k):
	return factorial(n)//(factorial(k)*factorial(n-k))

size = 10

pascal = ((combo(n,k) for k in range(n+1)) for n in range(size+1))
# Convert List of generators into a value
print([list(row) for row in pascal])
print('\n\nList nested in Generator Expressions')
# This also works the saem way.
# Like nested generator expresssion, this one too doesn't have to calcualte anything until request by next()
# Outside loop is a generator.
pascal = ([combo(n,k) for k in range(n+1)] for n in range(size+1))
# Convert List of generators into a value
print([row for row in pascal])


# To check memory footprint use: import tracemalloc
# Generator Expression is more Memory efficient than List Comprehension
import tracemalloc

size = 600
def pascal_list(size):
	l = [[combo(n,k) for k in range(n+1)] for n in range(size+1)]
	for row in l:
		for item in row:
			pass
	stats = tracemalloc.take_snapshot().statistics('lineno')
	print('Size impact of List Comprehension: ',stats[0].size, ' bytes')

def pascal_gen(size):
	l = ((combo(n,k) for k in range(n+1)) for n in range(size+1))
	for row in l:
		for item in row:
			pass
	stats = tracemalloc.take_snapshot().statistics('lineno')
	print('Size impact of Generator Expression: ', stats[0].size, ' bytes')

tracemalloc.stop()
tracemalloc.clear_traces()
tracemalloc.start()
print('Size impact of List Comprehension: ',pascal_list(size))

tracemalloc.stop()
tracemalloc.clear_traces()
tracemalloc.start()
print('Size impact of Generator Expression: ',pascal_gen(size))